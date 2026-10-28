#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sp.py — tien xu ly dau vao cho Agent-SeedingPlant-Kangnam.

Hai viec:
  hoi-thoai  B3 — boc hoi thoai thanh ma O-01..O-12, nac 5A, chan dung, dem tan suat
  so-lieu    B2 — tinh CPI/CPL/CPB, phan ra CPL, cham noi dung 3 bac

Script lam phan DEM va phan TINH. Phan HIEU NGU CANH van la viec cua agent.

    python tools/sp.py hoi-thoai hoithoai.csv
    python tools/sp.py hoi-thoai --sheet-id <ID> --gid <GID>
    python tools/sp.py so-lieu ads-t45.csv --lead-tu CRM
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import statistics
import sys
import unicodedata
import urllib.request
from pathlib import Path

# ────────────────────────────────────────────────────────────── tien ich

def bo_dau(s: str) -> str:
    """Bo dau tieng Viet + ha chu thuong, de so khop tu khoa."""
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower().strip()


def so(x) -> float:
    """Doc mot o thanh so. '18,2tr' / '412k' / '1.234' deu doc duoc."""
    t = bo_dau(x).replace(" ", "")
    if not t:
        return 0.0
    nhan = 1.0
    if t.endswith("tr"):
        nhan, t = 1_000_000.0, t[:-2]
    elif t.endswith("ty"):
        nhan, t = 1_000_000_000.0, t[:-2]
    elif t.endswith("k"):
        nhan, t = 1_000.0, t[:-1]
    t = re.sub(r"[^0-9,.\-]", "", t)
    if not t:
        return 0.0
    # 1.234,5 -> 1234.5  |  1,234.5 -> 1234.5
    if "," in t and "." in t:
        t = t.replace("." if t.rfind(",") > t.rfind(".") else ",", "")
    t = t.replace(",", ".")
    try:
        return float(t) * nhan
    except ValueError:
        return 0.0


def tien(v: float) -> str:
    if v >= 1_000_000_000:
        return f"{v / 1_000_000_000:,.2f} ty".replace(".", ",")
    if v >= 1_000_000:
        return f"{v / 1_000_000:,.1f}tr".replace(".", ",")
    if v >= 1_000:
        return f"{v / 1_000:,.0f}k"
    return f"{v:,.0f}"


def phan_tram(v: float) -> str:
    return f"{v * 100:.1f}%".replace(".", ",")


def lech(moi: float, goc: float) -> str:
    if goc == 0:
        return "n/a"
    d = (moi - goc) / goc
    return f"{d * 100:+.0f}%"


# ────────────────────────────────────────────────── doc file / google sheet

def doc_bang(duong_dan: str | None, sheet_id: str | None,
             gid: str | None, ten_tab: str | None) -> list[list[str]]:
    if sheet_id:
        url = (f"https://docs.google.com/spreadsheets/d/{sheet_id}"
               f"/export?format=csv&gid={gid or '0'}")
        with urllib.request.urlopen(url, timeout=60) as r:
            raw = r.read().decode("utf-8", errors="replace")
        return list(csv.reader(io.StringIO(raw)))

    if not duong_dan:
        sys.exit("Thieu file hoac --sheet-id.")
    p = Path(duong_dan)
    if not p.exists():
        sys.exit(f"Khong thay file: {p}")

    if p.suffix.lower() in (".xlsx", ".xlsm"):
        try:
            from openpyxl import load_workbook
        except ImportError:
            sys.exit("Thieu openpyxl -> pip install openpyxl")
        wb = load_workbook(p, read_only=True, data_only=True)
        ws = wb[ten_tab] if ten_tab and ten_tab in wb.sheetnames else wb[wb.sheetnames[0]]
        return [["" if c is None else str(c) for c in hang]
                for hang in ws.iter_rows(values_only=True)]

    raw = p.read_text(encoding="utf-8", errors="replace")
    dau = ";" if raw.count(";") > raw.count(",") else ","
    return list(csv.reader(io.StringIO(raw), delimiter=dau))


def tim_tieu_de(bang: list[list[str]], tu_khoa: list[str]) -> int:
    """Tra chi so hang tieu de — hang dau tien chua >=2 tu khoa."""
    for i, hang in enumerate(bang[:40]):
        gop = bo_dau(" | ".join(hang))
        if sum(1 for t in tu_khoa if t in gop) >= 2:
            return i
    return 0


def map_cot(tieu_de: list[str], can: dict[str, list[str]]) -> dict[str, int]:
    ra: dict[str, int] = {}
    chuan = [bo_dau(c) for c in tieu_de]
    for khoa, tu in can.items():
        for i, c in enumerate(chuan):
            if c and any(t in c for t in tu):
                ra[khoa] = i
                break
    return ra


# ───────────────────────────────────────────────── B3 · boc hoi thoai

# sp-C §2 — 12 ma phan doi. Thu tu quan trong: ma dung TRUOC thang khi trung tu khoa.
MA_O: list[tuple[str, str, tuple[str, ...]]] = [
    ("O-12", "Benh nen, suc khoe",
     ("tieu duong", "huyet ap", "tim mach", "mau kho dong", "cho con bu",
      "mang thai", "co thai", "benh nen", "di ung thuoc", "viem gan", "dang uong thuoc")),
    ("O-07", "Bao hanh & trach nhiem",
     ("bao hanh", "hong thi ai chiu", "ai chiu trach nhiem", "cam ket gi",
      "lam lai co mat tien")),
    ("O-11", "Nguoi nha phan doi",
     ("chong em", "chong minh", "me em", "bo me", "gia dinh khong cho",
      "khong cho lam", "giau gia dinh", "ba xa", "vo em")),
    ("O-10", "So sanh doi thu",
     ("ben kia", "cho khac", "noi khac", "re hon", "so voi", "thammy khac",
      "vien khac", "benh vien khac")),
    ("O-09", "Thoi gian, o xa, lich",
     ("o tinh", "o xa", "ve nuoc", "viet kieu", "cuoi tuan", "chu nhat",
      "bao lau thi ve", "may ngay o lai", "dat lich khi nao", "bay ve",
      "o my", "o uc", "o nhat", "o han")),
    ("O-05", "Nghi tay nghe bac si",
     ("bac si nao", "ai mo", "ai lam", "bac nao mo", "tay nghe", "bac si gioi",
      "bs nao", "co mo nhieu", "kinh nghiem bao nhieu", "bac si truong khoa",
      "bac si mo", "ai theo doi", "bac si phu trach", "bac si truc tiep",
      "co phai bac si")),
    ("O-06", "Nghi dia chi, uy tin",
     ("giay phep", "uy tin", "benh vien hay spa", "co dam bao", "co hop phap",
      "dia chi", "co phai benh vien", "chinh hang")),
    ("O-04", "Dau, sung lau, nghi viec",
     ("dau khong", "co dau", "sung", "bao lau lanh", "may ngay di lam",
      "nghi may ngay", "hoi phuc", "kieng", "cat chi", "vao form",
      "bao lau het", "bao lau thi", "khi nao het", "theo doi sau mo")),
    ("O-03", "So lo sua, khong tu nhien",
     ("lo sua", "trong gia", "co nhan ra", "tu nhien khong", "gia tao",
      "nguoi ta biet", "fake")),
    ("O-02", "So ket qua xau hon",
     ("xau hon", "so hong", "bien chung", "that bai", "hong roi", "loi",
      "co sao khong", "rui ro", "nguy hiem khong")),
    ("O-01", "Gia & phat sinh",
     ("bao nhieu tien", "gia bao nhieu", "chi phi", "tron goi", "phat sinh",
      "bao nhieu a", "may trieu", "tra gop", "uu dai", "khuyen mai", "giam gia")),
    ("O-08", "Khong biet minh can gi",
     ("em the nay", "minh the nay", "nhu em co", "gui anh", "xem giup",
      "tu van giup", "co lam duoc", "co duoc khong", "nen lam gi", "hop khong",
      "co phu hop", "danh gia giup", "sua lai duoc", "lam lai duoc",
      "con sua duoc", "con sua lai", "nghet mui", "hop guong mat",
      "muon giong", "giong chi", "doi van", "ham tai", "nen chon")),
]

# sp-C §3 — nac 5A suy tu cau hoi dau tien.
NAC: list[tuple[str, tuple[str, ...]]] = [
    ("A5", ("kieng gi", "tai kham", "sau mo", "cham soc sau", "da lam roi roi")),
    ("A4", ("con suat", "dat lich", "t7 nay", "mai di duoc", "hom nay co",
            "uu dai den bao gio", "chot lich", "bao gio co sale",
            "cuoi tuan co lam", "chu nhat co lam", "sap lich", "con cho khong")),
    ("A3", ("bao nhieu tien", "gia bao nhieu", "chi phi", "dau khong", "bao hanh",
            "bac si nao", "ai mo", "may ngay di lam", "tron goi", "tra gop")),
    ("A2", ("cong nghe", "phuong phap", "ky thuat", "dang nao", "sun nao",
            "cau truc", "loai nao", "o dau uy tin", "khac nhau the nao",
            "muon giong", "giong chi", "hop dang nao", "co may loai",
            "lam kieu gi", "benh vien hay spa", "giay phep")),
    ("A1", ()),  # mac dinh
]

# sp-C §4 — chan dung.
CHAN_DUNG: list[tuple[str, str, tuple[str, ...]]] = [
    ("CD6", "Kho, benh ly",
     ("nghet mui", "viem xoang", "sup mi", "co rut", "vach ngan", "benh ly",
      "viem", "lech vach", "kho tho")),
    ("CD3", "Sua lai",
     ("da nang", "nang roi", "lam roi", "sua lai", "ben kia lam hong",
      "nam truoc lam", "thao ra", "lan truoc", "da cat mi roi", "lam lai")),
    ("CD5", "Phong thuy",
     ("phong thuy", "tuong so", "van", "su nghiep", "tai loc", "hop tuoi",
      "xem tuong", "doi van")),
    ("CD2", "Hot Face",
     ("giong chi", "giong co", "hot girl", "trend", "idol", "dien vien",
      "ca si", "nhu trong anh", "tiktoker")),
    ("CD4", "Nam gioi",
     ("nam lam", "con trai", "anh muon", "dan ong", "nam gioi", "cho nam")),
    ("CD1", "Khuyet diem", ()),  # mac dinh
]

COT_HT = {
    "ma": ["conversation id", "ma hoi thoai", "ma ht", "id"],
    "nguoi": ["sender", "nguoi gui", "nguoi nhan", "tu"],
    "noi_dung": ["message", "noi dung", "tin nhan", "khach hoi", "cau hoi"],
    "tra_loi": ["tra loi", "truc page", "page", "reply", "phan hoi"],
    "ket_cuc": ["ket cuc", "ket qua", "trang thai", "status"],
}


def gan_ma_o(cau: str) -> tuple[str, str]:
    c = bo_dau(cau)
    for ma, ten, tu in MA_O:
        if any(t in c for t in tu):
            return ma, ten
    return "O-00", "Chua phan loai"


def gan_nac(cau: str) -> str:
    c = bo_dau(cau)
    for nac, tu in NAC:
        if tu and any(t in c for t in tu):
            return nac
    return "A1"


def gan_chan_dung(cau: str) -> tuple[str, str]:
    c = bo_dau(cau)
    for ma, ten, tu in CHAN_DUNG:
        if tu and any(t in c for t in tu):
            return ma, ten
    return "CD1", "Khuyet diem"


def tach_hoi_thoai_tho(van_ban: str) -> list[str]:
    """Dan tho dang 'KH: ...' / 'Khach: ...' -> lay cac dong cua KHACH."""
    ra = []
    for d in van_ban.splitlines():
        d = d.strip()
        m = re.match(r"^(kh|khach|khach hang|k)\s*[:\-]\s*(.+)$", bo_dau(d))
        if m:
            ra.append(d.split(":", 1)[1].strip() if ":" in d else d)
    return ra


def chay_hoi_thoai(args) -> None:
    cau_hoi: list[tuple[str, str, str]] = []  # (ma_ht, cau dau tien, tra loi)

    if args.file and Path(args.file).suffix.lower() in (".txt", ".md"):
        tho = Path(args.file).read_text(encoding="utf-8", errors="replace")
        for i, c in enumerate(tach_hoi_thoai_tho(tho), 1):
            cau_hoi.append((f"HT-{i:03d}", c, ""))
    else:
        bang = doc_bang(args.file, args.sheet_id, args.gid, args.sheet)
        i_td = tim_tieu_de(bang, ["message", "noi dung", "khach hoi", "cau hoi",
                                  "conversation", "tin nhan"])
        if i_td >= len(bang):
            sys.exit("File rong.")
        cot = map_cot(bang[i_td], COT_HT)
        if "noi_dung" not in cot:
            sys.exit("Khong tim duoc cot noi dung tin nhan. Xem sp-B §3.")

        da_co: set[str] = set()
        stt = 0
        for hang in bang[i_td + 1:]:
            if not any(str(o).strip() for o in hang):
                continue
            lay = lambda k: (hang[cot[k]] if k in cot and cot[k] < len(hang) else "")
            ma = str(lay("ma")).strip()
            noi = str(lay("noi_dung")).strip()
            if not noi:
                continue
            # chi lay TIN NHAN DAU TIEN cua moi hoi thoai (sp-B §3)
            if ma:
                if ma in da_co:
                    continue
                da_co.add(ma)
            else:
                stt += 1
                ma = f"HT-{stt:03d}"
            cau_hoi.append((ma, noi, str(lay("tra_loi")).strip()))

    if not cau_hoi:
        sys.exit("Khong boc duoc cau hoi nao. Xem sp-B §3 ve dinh dang dau vao.")

    dem_o: dict[str, int] = {ma: 0 for ma, _, _ in MA_O}
    dem_o["O-00"] = 0
    dem_nac: dict[str, int] = {}
    dem_cd: dict[str, int] = {}
    dong: list[dict] = []

    for ma_ht, cau, tra in cau_hoi:
        ma_o, ten_o = gan_ma_o(cau)
        nac = gan_nac(cau)
        cd, ten_cd = gan_chan_dung(cau)
        dem_o[ma_o] = dem_o.get(ma_o, 0) + 1
        dem_nac[nac] = dem_nac.get(nac, 0) + 1
        dem_cd[cd] = dem_cd.get(cd, 0) + 1
        dong.append({"ma_ht": ma_ht, "ma_o": ma_o, "ten_o": ten_o, "nac": nac,
                     "chan_dung": cd, "cau": cau, "dai_tra_loi": len(tra)})

    n = len(dong)
    goc = Path(__file__).resolve().parent.parent
    ra = Path(args.out) if args.out else goc / "out" / "insight-hoi-thoai.csv"
    ra.parent.mkdir(parents=True, exist_ok=True)
    with ra.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["MA HT", "MA O", "TEN MA O", "NAC 5A", "CHAN DUNG",
                    "CAU HOI DAU TIEN", "DO DAI TRA LOI TRUC PAGE"])
        for d in dong:
            w.writerow([d["ma_ht"], d["ma_o"], d["ten_o"], d["nac"],
                        d["chan_dung"], d["cau"], d["dai_tra_loi"]])

    print(f"\n  DOC DUOC : {n} hoi thoai")
    print(f"  GHI RA   : {ra.relative_to(goc) if goc in ra.parents else ra}\n")

    print("  DEM MA PHAN DOI (sp-C §2) — nguong ra viec: >=15 tuyen rieng, 8-14 mot hook\n")
    ten_theo_ma = {ma: ten for ma, ten, _ in MA_O} | {"O-00": "Chua phan loai"}
    # sp-C §5 — nguong tinh THEO TI LE /100, khong theo so dem tho.
    # Mau <50 thi KHONG dung nguong tuyet doi (sp-C §5) -> de trong cot viec.
    for ma in [m for m, _, _ in MA_O] + ["O-00"]:
        c = dem_o.get(ma, 0)
        pc = c / n * 100 if n else 0
        if n < 50:
            viec, sao = "", ""
        else:
            viec = ("TUYEN RIENG" if pc >= 15 else "MOT HOOK" if pc >= 8
                    else "ghi nhan" if pc >= 5 else "-")
            sao = " <<" if pc >= 8 else ""
        print(f"    {ma}  {c:>3}  {pc:>5.1f}%  {ten_theo_ma[ma]:<28} {viec}{sao}")
    if n < 50:
        print("    (cot viec de trong — mau <50, xep hang tuong doi thoi)")

    if n and dem_o.get("O-00", 0) / n > 0.10:
        print(f"\n  ! O-00 = {dem_o['O-00'] / n * 100:.0f}% (>10%) — danh sach 12 ma"
              " can bo sung. BAO LAI, dung tu them ma.")

    print("\n  PHAN BO NAC 5A")
    for nac in ("A1", "A2", "A3", "A4", "A5"):
        c = dem_nac.get(nac, 0)
        print(f"    {nac}  {c:>3}  {c / n * 100 if n else 0:>5.1f}%")
    if n and dem_nac.get("A3", 0) / n > 0.60:
        print("    ! >60% roi vao A3 — pheu dang THIEU NOI DUNG A1-A2 (sp-C §3)")

    print("\n  PHAN BO CHAN DUNG")
    ten_cd = {ma: ten for ma, ten, _ in CHAN_DUNG}
    for ma in ("CD1", "CD2", "CD3", "CD4", "CD5", "CD6"):
        c = dem_cd.get(ma, 0)
        print(f"    {ma}  {c:>3}  {c / n * 100 if n else 0:>5.1f}%  {ten_cd[ma]}")

    # sp-C §7 — tin hieu tang hai
    dai = [d for d in dong if d["dai_tra_loi"] >= 300]
    if dai:
        print(f"\n  TANG HAI: {len(dai)} hoi thoai co truc page go TRA LOI DAI (>=300 ky tu)")
        print("    -> viec nay dang le clip lam. Xem sp-C §7.")

    if n < 50:
        print(f"\n  ! MAU NHO ({n} < 50) — KHONG dung nguong tuyet doi,"
              " chi xep hang tuong doi.")

    print("\n  ⛔ Script cham theo TU KHOA. Agent VAN PHAI doc lai de hieu ngu canh.")
    print("  ⛔ Da KHONG ghi ten/SDT ra file — nhung hay kiem lai cot CAU HOI.\n")


# ───────────────────────────────────────────────────── B2 · doc so lieu

COT_SO = {
    "ten": ["ten ad", "ad name", "noi dung", "ma noi dung", "ten quang cao"],
    "hook": ["hook", "cau hook", "tieu de"],
    "chi": ["chi tieu", "amount spent", "spend", "chi phi", "so tien"],
    "imp": ["impression", "hien thi", "luot hien"],
    "reach": ["reach", "tiep can"],
    "click": ["click", "nhap", "luot nhan"],
    "inbox": ["inbox", "hoi thoai", "messaging", "tin nhan bat dau"],
    "lead": ["lead", "so lieu", "khach hang tiem nang", "sdt"],
    "booking": ["booking", "dat lich", "lich hen"],
    "bac_si": ["bac si", "bs"],
    "nac": ["nac", "5a", "giai doan"],
    "chan_dung": ["chan dung", "cd", "tep"],
    "format": ["format", "dinh dang", "ma l"],
}


def chay_so_lieu(args) -> None:
    bang = doc_bang(args.file, args.sheet_id, args.gid, args.sheet)
    i_td = tim_tieu_de(bang, ["chi tieu", "spend", "impression", "click",
                              "lead", "ten ad", "ad name"])
    if i_td >= len(bang):
        sys.exit("File rong.")
    cot = map_cot(bang[i_td], COT_SO)

    thieu = [k for k in ("chi", "imp", "click") if k not in cot]
    if thieu:
        sys.exit(f"Thieu cot bat buoc: {', '.join(thieu)}. Xem sp-B §4.")
    if "hook" not in cot:
        print("\n  ! FILE KHONG CO COT 'HOOK' — chi cham duoc theo TEN AD,"
              " do tin THAP.\n    Can khoi Ads bo sung cot HOOK (sp-B §4).")

    dong: list[dict] = []
    for hang in bang[i_td + 1:]:
        if not any(str(o).strip() for o in hang):
            continue
        lay = lambda k: (hang[cot[k]] if k in cot and cot[k] < len(hang) else "")
        chi = so(lay("chi"))
        imp = so(lay("imp"))
        if chi <= 0 and imp <= 0:
            continue
        click, inbox = so(lay("click")), so(lay("inbox"))
        lead, booking = so(lay("lead")), so(lay("booking"))
        reach = so(lay("reach"))
        dong.append({
            "ten": str(lay("ten")).strip() or "(khong ten)",
            "hook": str(lay("hook")).strip(),
            "bac_si": str(lay("bac_si")).strip(),
            "nac": str(lay("nac")).strip(),
            "chan_dung": str(lay("chan_dung")).strip(),
            "format": str(lay("format")).strip(),
            "chi": chi, "imp": imp, "click": click, "inbox": inbox,
            "lead": lead, "booking": booking, "reach": reach,
            "cpm": chi / imp * 1000 if imp else 0.0,
            "ctr": click / imp if imp else 0.0,
            "cpi": chi / inbox if inbox else 0.0,
            "cpl": chi / lead if lead else 0.0,
            "cpb": chi / booking if booking else 0.0,
            "freq": imp / reach if reach else 0.0,
            "c2i": inbox / click if click else 0.0,
            "i2l": lead / inbox if inbox else 0.0,
        })

    if not dong:
        sys.exit("Khong doc duoc dong du lieu nao.")

    med = lambda k: statistics.median([d[k] for d in dong if d[k] > 0] or [0])
    m_ctr, m_cpl, m_cpm = med("ctr"), med("cpl"), med("cpm")

    du_mau = lambda d: d["imp"] >= 1000 and d["lead"] >= 7
    for d in dong:
        if not du_mau(d):
            d["cham"] = "- CHUA DU MAU"
        elif d["ctr"] >= m_ctr and (d["cpl"] <= m_cpl or d["cpl"] == 0):
            d["cham"] = "TOT"
        elif m_ctr and d["ctr"] <= m_ctr * 0.7 and m_cpm and abs(d["cpm"] - m_cpm) <= m_cpm * 0.15:
            d["cham"] = "KEM"
        else:
            d["cham"] = "TB"
        d["bao_hoa"] = (d["freq"] >= 2.5 and m_ctr and d["ctr"] < m_ctr * 0.8)

    t_chi = sum(d["chi"] for d in dong)
    t_imp = sum(d["imp"] for d in dong)
    t_click = sum(d["click"] for d in dong)
    t_inbox = sum(d["inbox"] for d in dong)
    t_lead = sum(d["lead"] for d in dong)
    t_book = sum(d["booking"] for d in dong)

    goc = Path(__file__).resolve().parent.parent
    ra = Path(args.out) if args.out else goc / "out" / "cham-noi-dung.csv"
    ra.parent.mkdir(parents=True, exist_ok=True)
    with ra.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["TEN", "HOOK", "BAC SI", "NAC", "CHAN DUNG", "FORMAT",
                    "CHI", "IMP", "CLICK", "INBOX", "LEAD", "BOOKING",
                    "CPM", "CTR", "CPI", "CPL", "CPB", "FREQ",
                    "CHAM", "BAO HOA", "DU MAU"])
        for d in dong:
            w.writerow([d["ten"], d["hook"], d["bac_si"], d["nac"], d["chan_dung"],
                        d["format"], round(d["chi"]), round(d["imp"]),
                        round(d["click"]), round(d["inbox"]), round(d["lead"]),
                        round(d["booking"]), round(d["cpm"]),
                        f"{d['ctr'] * 100:.2f}%", round(d["cpi"]), round(d["cpl"]),
                        round(d["cpb"]), f"{d['freq']:.2f}", d["cham"],
                        "x" if d["bao_hoa"] else "", "x" if du_mau(d) else ""])

    print(f"\n  KY        : {args.ky or '[CHUA GHI — BAT BUOC, xem cong A]'}")
    print(f"  LEAD DEM  : {args.lead_tu}")
    print(f"  DOC DUOC  : {len(dong)} dong")
    print(f"  GHI RA    : {ra.relative_to(goc) if goc in ra.parents else ra}\n")

    print("  TONG KY")
    print(f"    Chi      {tien(t_chi)}")
    print(f"    CPM      {tien(t_chi / t_imp * 1000 if t_imp else 0)}"
          f"      CTR  {phan_tram(t_click / t_imp if t_imp else 0)}")
    print(f"    CPI      {tien(t_chi / t_inbox if t_inbox else 0)}"
          f"      ({round(t_inbox)} inbox)")
    print(f"    CPL      {tien(t_chi / t_lead if t_lead else 0)}"
          f"      ({round(t_lead)} lead / {tien(t_chi)})")
    print(f"    CPB      {tien(t_chi / t_book if t_book else 0)}"
          f"      ({round(t_book)} booking)")

    print("\n  PHAN RA CPL (sp-D §2) — so voi median cung ky")
    print(f"    CPM          median {tien(m_cpm)}")
    print(f"    CTR          median {phan_tram(m_ctr)}")
    print(f"    click->inbox {phan_tram(t_inbox / t_click if t_click else 0)}")
    print(f"    inbox->lead  {phan_tram(t_lead / t_inbox if t_inbox else 0)}")
    print("    -> ⛔ Script KHONG co median 7 ngay. Agent phai phan ra voi median that")
    print("       roi KET LUAN: 'tuan nay CO / KHONG phai van de noi dung' (sp-D §2).")

    dem = {}
    for d in dong:
        dem[d["cham"]] = dem.get(d["cham"], 0) + 1
    print(f"\n  CHAM NOI DUNG : TOT {dem.get('TOT', 0)}  ·  TB {dem.get('TB', 0)}"
          f"  ·  KEM {dem.get('KEM', 0)}  ·  chua du mau {dem.get('- CHUA DU MAU', 0)}")
    for d in dong:
        if d["cham"] == "KEM":
            print(f"      [KEM] {d['ten'][:38]:<38} {(d['hook'] or '(khong co cot hook)')[:46]}")

    bh = [d for d in dong if d["bao_hoa"]]
    if bh:
        print(f"\n  BAO HOA : {len(bh)} dong (frequency >=2,5 kem CTR giam)")

    phu = [d for d in dong if t_chi and d["chi"] / t_chi >= 0.60]
    if phu:
        print(f"  PHU THUOC 1 CREATIVE : {phu[0]['ten'][:40]} chiem"
              f" {phu[0]['chi'] / t_chi * 100:.0f}% chi")

    print("\n  ⛔ KIEM TRUOC KHI KET LUAN (sp-D §4):")
    print("     - dang so cuoi tuan voi ngay thuong?  -> HUY ket luan")
    print("     - ngay dau sau khi uu dai ket thuc?   -> GIAI THICH, khong quy trach nhiem")
    print("     - CPM tang >=30% o >=70% ad set?       -> do la THI TRUONG")
    print("     - ad nao vua bi tu choi?               -> khong dem ra cham noi dung\n")


# ────────────────────────────────────────────────────────────────── main

def main() -> None:
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser(
        prog="sp.py", description="Tien xu ly dau vao cho Agent-SeedingPlant-Kangnam")
    sub = p.add_subparsers(dest="viec", required=True)

    def chung(sp):
        sp.add_argument("file", nargs="?", help="File .csv .xlsx .txt")
        sp.add_argument("--sheet-id", help="Google Spreadsheet ID")
        sp.add_argument("--gid", help="gid cua tab")
        sp.add_argument("--sheet", help="Ten tab trong file xlsx")
        sp.add_argument("--out", help="Noi ghi ket qua")

    a = sub.add_parser("hoi-thoai", help="B3 — boc hoi thoai thanh ma O")
    chung(a)

    b = sub.add_parser("so-lieu", help="B2 — tinh chi so, cham noi dung")
    chung(b)
    b.add_argument("--ky", help="Ky so lieu, vd 07-13/10")
    b.add_argument("--lead-tu", default="CHUA GHI", choices=["Meta", "CRM", "CHUA GHI"],
                   help="Lead dem theo Meta hay CRM — BAT BUOC ghi (cong A)")

    args = p.parse_args()
    if args.viec == "hoi-thoai":
        chay_hoi_thoai(args)
    else:
        chay_so_lieu(args)


if __name__ == "__main__":
    main()
