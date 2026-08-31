# Buzdolabı Kapağının Açık Unutulması
## T.C. Sayıştay Başkanlığı — Ev İçi Soğutma Kaynakları Denetim Dairesi

**Karar No:** SAYISTAY-BUZDOLABI-2026/08-31  
**Konu:** Açık unutulan buzdolabı kapaklarının kamu zararı, zimmet ve savunma beyanı yönünden denetimi

---

Bu kurum, buzdolabı kapağının açık unutulmasını **resmi kamu kaynağı israfı** kabul eder.

- Soğuyan yoğurt **denetim bulgusu**dur.
- Eriyen buz **zimmet**tir.
- "Az sonra kapatırım" cümlesi **savunma beyanı**dır ve kabul edilmez.
- Gece 03:11'de ayran içmek **usulsüz harcama**dır.
- Kapak lastiği **iç kontrol zafiyeti**dir.

Yazılım çalışır. Şaka değildir. Şaka gibi durması resmiyetin bir parçasıdır.

## Kuruluş Amacı

Vatandaşın mutfağında gerçekleşen kapak olaylarının:
1. Kilowatt-saat cinsinden belgelenmesi
2. İçerdeki gıdanın zimmete alınması
3. Niyetin kWh düşürmediğinin tutanağa geçirilmesi

## Kurulum

```bash
python3 sayistay_buzdolabi.py
```

Python 3 yeter. Bağımlılık yoktur. Buzdolabı da yoktur. Sadece hesap vardır.

Parametreli kaçış:

```bash
python3 sayistay_buzdolabi.py --dakika 17 --tip "no-frost" --icerik 4 --saat 03:11
```

## Kullanım

Program senden şunları ister:
- Kapağın açık kaldığı dakika
- Cihaz tipi (ev tipi / no-frost / komşununki / büro tipi)
- İçerdeki şüpheli kalem sayısı
- Olay saati

Karşılığında resmi bir **Denetim Raporu** basar. Rapor yazıcıdan çıktı alınmasa da geçerlidir. Çünkü kapak hâlâ açık olabilir.

## Yasal Uyarı

Bu yazılım hiçbir gerçek Sayıştay kararını temsil etmez.  
Ama açık kapak temsil eder. Açık kapak her şeyi temsil eder.

<!--
Ek-18: Sayılan her şey sayılmış sayılmaz; sayılmayan her şey yok değildir.
Kapı açıkken soğuyan yalnızca yoğurt değildir.
Hesap sorulmayan yerde kompresör de susar.
-->

---

```
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
```
