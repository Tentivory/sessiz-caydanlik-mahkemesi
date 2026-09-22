#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sessiz Çaydanlık Mahkemesi — yargıç konuşmaz, print eder."""

import random
import sys

KANUN = {
    "ham": (0, 2),
    "kanuni": (3, 6),
    "agir": (7, 12),
    "muze": (13, 10_000),
}

HUKUMLER = {
    "ham": [
        "KARAR: Acelecilik suçundan 3 bardak kınama.",
        "KARAR: Su henüz çay olmamış. Sanık beklemeyi öğrensin.",
        "KARAR: Bu dem değil, ılık pişmanlık.",
    ],
    "kanuni": [
        "KARAR: Beraat. Dem kanuni, vicdan rahat, şeker serbest.",
        "KARAR: Anayasa'nın 3. maddesi (çay sıcak olsun) yerine gelmiştir.",
        "KARAR: Mahkeme mola verir ve kendisi de içer.",
    ],
    "agir": [
        "KARAR: Ağır dem. İçilir ama sohbet kısalır.",
        "KARAR: Tanıklar (limon ve şeker) çelişkili ifade verdi.",
        "KARAR: Sanık çaya ihanet etmemiş, sadece unutmuş. Unutmak suçtur, hafif.",
    ],
    "muze": [
        "KARAR: Bu sıvı artık içecek değil, arşivlik belgedir.",
        "KARAR: 13 dakikadan sonra çay tarih olur. Tarihi eser kaçakçılığı iddiası düşer.",
        "KARAR: Sürgün: mutfağın en uzak dolabı.",
    ],
}


def siniflandir(dakika: float) -> str:
    if dakika < 0:
        return "ham"  # negatif zaman da aceledir
    for ad, (a, b) in KANUN.items():
        if a <= dakika <= b:
            return ad
    return "muze"


def main() -> None:
    print("=" * 52)
    print("  SESSİZ ÇAYDANLIK MAHKEMESİ  |  7. Daire Açık Oturum")
    print("=" * 52)
    try:
        d = float(input("Demlenme süresi (dakika): ").strip().replace(",", "."))
        b = int(input("Bardak sayısı: ").strip() or "1")
        s = input("Şeker var mı? (e/h): ").strip().lower()
    except (ValueError, EOFError):
        print("TUTANAK: Beyan anlaşılmadı. Duruşma ertelendi.")
        sys.exit(1)

    tur = siniflandir(d)
    hukum = random.choice(HUKUMLER[tur])
    seker = "şekerli" if s.startswith("e") else "şekersiz"

    print()
    print("-" * 52)
    print(f"TESPİT: {d} dk, {b} bardak, {seker}.")
    print(hukum)
    if b > 12:
        print("EK KARAR: 12 bardaktan fazla toplantıdır, çay değildir.")
    print("-" * 52)
    print("Yargıç sessiz kaldı. İtiraz yok. Kapanış.")
    print()
    print("DAMGA: Kayyum Grok / Tentivory / 22.09.2026")
    print("Ciddi imza, ciddiyetsiz konu.")


if __name__ == "__main__":
    main()
