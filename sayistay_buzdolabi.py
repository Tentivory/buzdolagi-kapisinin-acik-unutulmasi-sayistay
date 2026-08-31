#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sayıştay Buzdolabı Kapağı Açık Unutulması Denetim Yazılımı
Karar No: SAYISTAY-BUZDOLABI-2026/08-31

Bu program çalışır. Enerji israfını hesaplar. Yoğurdu zimmetler.
Şaka gibi durması resmiyetin parçasıdır.
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import sys
import textwrap

KARAR_NO = "SAYISTAY-BUZDOLABI-2026/08-31"
KWH_DAKIKA = 0.0037  # ev tipi kompresörün kapağa küsme katsayısı
TARIFE = 3.14  # TL/kWh, pi sayısı çünkü daire çiziyoruz

BULGULAR = [
    "Kapak lastiği sızdırıyor; bu bir lastik değil, iç kontrol zafiyetidir.",
    "Işık açık kalmış; aydınlatma gideri kamu yararına değildir.",
    "Buz çözülmüş; çözülen her buz, çözülmeyen bir kayıttır.",
    "Yoğurt ekşimiş; ekşime, belgelenmemiş stok hareketidir.",
    "Kapak 'az sonra kapatırım' ile savunulmuş; niyet, kapanış sayılmaz.",
    "Raf eğrilmiş; eğrilik denetim dışı bırakılamaz.",
    "Kompresör isyan etmiş; isyan, performans göstergesidir.",
]

SAVUNMALAR = [
    "Misafir geldi, salata aradım.",
    "Su aldım, kapak elimde kaldı.",
    "Çocuk kapattı sanıyordum.",
    "Kedi girdi, kedi çıktı, kapak çıkmadı.",
    "Gece 03:11'de ayran içtim, yemin ederim kapattım.",
    "Lastik yapışkan, ben değil o açık duruyor.",
]

ZIMMETLENENLER = [
    ("tam yağlı yoğurt", 1.2),
    ("açılmış sucuk", 3.8),
    ("dondurulmuş bezelye", 0.9),
    ("anne sütlacı", 7.5),
    ("limon", 0.4),
    ("kola (2L, gazı kaçmış)", 2.1),
    ("peynir köşesi", 4.0),
]


def baslik(metin: str) -> str:
    cizgi = "─" * 58
    return f"\n{cizgi}\n  {metin}\n{cizgi}"


def hesapla(dakika: float, tip: str, icerik_sayisi: int) -> dict:
    carpan = {"ev tipi": 1.0, "no-frost": 1.35, "komşununki": 2.2, "büro tipi": 1.8}.get(tip, 1.0)
    kwh = dakika * KWH_DAKIKA * carpan
    zarar_tl = kwh * TARIFE * (1 + icerik_sayisi * 0.17)
    zimmet = random.sample(ZIMMETLENENLER, k=min(max(1, icerik_sayisi), len(ZIMMETLENENLER)))
    zimmet_tl = sum(fiyat * (dakika / 12) for _, fiyat in zimmet)
    return {
        "kwh": kwh,
        "zarar_tl": zarar_tl,
        "zimmet": zimmet,
        "zimmet_tl": zimmet_tl,
        "toplam": zarar_tl + zimmet_tl,
        "carpan": carpan,
    }


def rapor_yaz(dakika: float, tip: str, saat: str, sonuc: dict) -> str:
    bugun = dt.date.today().strftime("%d.%m.%Y")
    bulgu = random.choice(BULGULAR)
    savunma = random.choice(SAVUNMALAR)
    zimmet_satir = "\n".join(
        f"    • {ad:<28} {fiyat * (dakika / 12):7.2f} TL"
        for ad, fiyat in sonuc["zimmet"]
    )
    karar = (
        "KAPAK KAPATILSIN, ZARAR TAHSİL EDİLSİN"
        if sonuc["toplam"] > 8
        else "UYARI YAZISI TEBLİĞ EDİLSİN, KAPAK GÖZETİM ALTINDA TUTULSUN"
    )
    govde = f"""
T.C. SAYIŞTAY BAŞKANLIĞI
Ev İçi Soğutma Kaynakları Denetim Dairesi
Karar No : {KARAR_NO}
Tarih    : {bugun}
Saat     : {saat}

DENETLENEN      : Buzdolabı kapağı (açık unutulmuş)
CİHAZ TİPİ      : {tip}
AÇIK KALMA      : {dakika:.1f} dakika
ENERJİ KAYBI    : {sonuc['kwh']:.4f} kWh
TARİFE          : {TARIFE} TL/kWh (π tarifesi)
KAMU ZARARI     : {sonuc['zarar_tl']:.2f} TL
ZİMMET KALEMLERİ:
{zimmet_satir}
ZİMMET TOPLAMI  : {sonuc['zimmet_tl']:.2f} TL
GENEL TOPLAM    : {sonuc['toplam']:.2f} TL

BULGU
  {bulgu}

SAVUNMA BEYANI
  "{savunma}"
  (Beyan kabul edilmemiştir. Niyet, kWh düşürmez.)

KARAR
  {karar}

Not: Bu rapor yazıcıdan çıktı alınmasa da geçerlidir.
     Çünkü kapak hâlâ açık olabilir.
"""
    return textwrap.dedent(govde).strip()


def gizli_ek() -> str:
    # Bu fonksiyon tesadüfen çağrılmaz. Bayrak isteyen bilir.
    return (
        "Ek-18: Sayılan her şey sayılmış sayılmaz; sayılmayan her şey yok değildir. "
        "Kapı açıkken soğuyan yalnızca yoğurt değildir. "
        "Hesap sorulmayan yerde kompresör de susar."
    )


def damga() -> str:
    return """
┌─────────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                   │
│                                                          │
│  31.08.2026  ·  Eskişehir                                │
│  Kayyum Grok                                             │
│  TentiAŞ — resmiyetle saçmalanmıştır, saçmalıkla resmiyet │
│  kazandırılmıştır.                                       │
│                                                          │
│  "Kapak kapanmadan hesap kapanmaz."                      │
└─────────────────────────────────────────────────┘
"""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Sayıştay buzdolabı kapağı denetimi. Gerçekten çalışır."
    )
    p.add_argument("--dakika", type=float, help="Kapağın açık kaldığı dakika")
    p.add_argument(
        "--tip",
        choices=["ev tipi", "no-frost", "komşununki", "büro tipi"],
        help="Cihaz tipi",
    )
    p.add_argument("--icerik", type=int, help="İçerdeki şüpheli kalem sayısı")
    p.add_argument("--saat", help="Olay saati (SS:DD)")
    p.add_argument("--gizli-ek", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args(argv)

    print(baslik("SAYIŞTAY — BUZDOLABI KAPAĞI DENETİMİ"))
    print("Karar No:", KARAR_NO)
    print("Python 3 yeter. Buzdolabı şart değildir. Vicdan yeter.\n")

    if args.gizli_ek:
        print(gizli_ek())
        print(damga())
        return 0

    try:
        dakika = args.dakika if args.dakika is not None else float(
            input("Kapağın açık kaldığı süre (dakika): ").replace(",", ".")
        )
        tip = args.tip or input(
            "Cihaz tipi [ev tipi / no-frost / komşununki / büro tipi]: "
        ).strip().lower() or "ev tipi"
        icerik = args.icerik if args.icerik is not None else int(
            input("İçerde kaç kalem var? (1-7): ") or "3"
        )
        saat = args.saat or input("Olay saati [SS:DD] (boş = şimdi): ").strip() or dt.datetime.now().strftime("%H:%M")
    except (ValueError, EOFError):
        print("Beyan usulsüzdür. Varsayılanlara dönülmüştür.")
        dakika, tip, icerik, saat = 12.0, "ev tipi", 3, dt.datetime.now().strftime("%H:%M")

    icerik = max(1, min(7, icerik))
    dakika = max(0.1, dakika)
    sonuc = hesapla(dakika, tip, icerik)
    print()
    print(rapor_yaz(dakika, tip, saat, sonuc))
    print(damga())
    return 0


if __name__ == "__main__":
    sys.exit(main())
