# 🧠 YOLOv8 Nesne Tanıma (Türkçe Sesli Bildirimli)

Bu proje, **YOLOv8 nesne tanıma algoritması** kullanarak gerçek zamanlı kamera görüntüsü üzerinden nesne tespiti yapar ve algılanan nesneleri **Türkçe sesli bildirim** ile kullanıcıya iletir.  
Proje Python diliyle yazılmış olup OpenCV, gTTS ve Ultralytics kütüphaneleri kullanılmıştır.

---

## 🎯 Proje Amacı

Görüntü işleme ve yapay zeka alanında çalışmak isteyen öğrenciler ve geliştiriciler için:

- Gerçek zamanlı nesne tespiti pratiği kazanmak
- YOLOv8 kullanımını öğrenmek
- Görsel çıktıyı sesli bildirime dönüştürmek
- Türkçe sesli sistemlerle uygulama geliştirmek

---

## ✨ Özellikler

- 📷 Gerçek zamanlı video akışı üzerinden nesne algılama
- 🧠 YOLOv8 ile yüksek doğruluklu nesne tespiti
- 🗣️ Türkçe sesli çıktı (Google Text-to-Speech - `gTTS`)
- 🔧 Basit ve modüler Python kod yapısı
- 💻 Donanımsal olarak CPU üzerinde çalışabilir

---

## 🔍 Kullanılan Teknolojiler ve Kütüphaneler

| Teknoloji    | Açıklama                              |
|--------------|----------------------------------------|
| Python 3.x   | Ana programlama dili                   |
| Ultralytics YOLOv8 | Derin öğrenme tabanlı nesne tespiti |
| OpenCV       | Kamera ve görüntü işleme               |
| NumPy        | Sayısal işlemler ve veri yapıları      |
| gTTS         | Türkçe sesli çıktı (metinden konuşma)  |

---

## 📁 Dosya Yapısı
YOLOv8-Nesne-Tanima-Turkce-Sesli/
├── Nesne_Tanima.py # Ana uygulama (kamera, YOLO, sesli çıktı)
├── yolov8n.pt # YOLOv8 modeli (indirilmeli)
├── requirements.txt # Gerekli Python kütüphaneleri
├── README.md # Proje tanıtımı ve kullanım kılavuzu
└── .gitignore # Yüklenmemesi gereken dosyalar listesi

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Gerekli Kütüphaneleri Kur
```bash
pip install -r requirements.txt
 ```
### Alternatif olarak:
```bash
pip install ultralytics opencv-python gtts numpy
 ```
### 2. YOLOv8 Modelini İndir
🔗 Yöntem 1 – Ultralytics sitesinden:
https://github.com/ultralytics/ultralytics sayfasına git

yolov8n.pt dosyasını indir

🔗 Yöntem 2 – Komut satırıyla:
```bash

yolo download model=yolov8n.pt
 ```
🔁 Dosya adı: yolov8n.pt
📁 İndirilen dosyayı proje klasörüne koy (örneğin Nesne_Tanima.py ile aynı klasöre).

### 🚀 Kullanım
```bash

python Nesne_Tanima.py
```
 - Kamera açılır

- Algılanan nesneler ekranda kutu içinde gösterilir

- Algılanan nesne adı Türkçe olarak sesli söylenir

Örnek: "Araba yüzde 87 oranında algılandı"

## 👤 Geliştirici Bilgisi
👨‍💻 Ad: Emir Aksu

🎓 Üniversite: Karabük Üniversitesi

📚 Bölüm: Yapay Zeka Operatörlüğü

🌐 GitHub: https://github.com/Emir-aks74

📌 İlgi Alanları: Görüntü işleme, sesli AI uygulamaları, yapay zeka tabanlı etkileşim sistemleri

🎯 Hedef Kitle: Üniversite öğrencileri, teknoloji meraklıları, AI öğrenmek isteyen herkes


---

## 💡 Geliştirme Önerileri
📱 Mobil uygulama sürümü (Kivy / Flutter ile)

🔇 Offline ses için pyttsx3 entegrasyonu

🧭 Görme engelliler için yönlendirme sistemine entegre

📊 Algılanan nesneleri zaman damgası ile loglama

🌐 Web tabanlı versiyon (Flask, Streamlit vs.)

