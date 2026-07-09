# Üretim Verimlilik ve Analiz Sistemi

Python ve SQLite kullanılarak geliştirilmiş, üretim verilerini kaydeden ve analiz eden bir konsol uygulaması.

## Özellikler
- Üretim kaydı ekleme (ürün, miktar, hata sayısı, tarih)
- Tüm kayıtları listeleme
- Ürüne göre toplam üretim analizi (GROUP BY)
- Hata oranı yüksek ürünleri tespit etme (HAVING)
- Ortalamanın altında üretim yapılan günleri bulma (SUBQUERY)

## Kullanılan Teknolojiler
- Python 3
- SQLite3
- SQL: SELECT, INSERT, GROUP BY, HAVING, SUBQUERY, ORDER BY

## Nasıl Çalıştırılır
```bash
python uretim_analiz.py
```

## Öğrenilen Konular
Bu proje ile SQL'de GROUP BY (gruplama), HAVING (grup filtreleme) ve SUBQUERY (alt sorgu) kullanımını gerçek bir senaryo üzerinde uyguladım.