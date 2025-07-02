import cv2
from ultralytics import YOLO
from gtts import gTTS
import playsound
import os
import time

# YOLOv8 modelini yükle
model = YOLO("yolov8n.pt")

# İngilizce → Türkçe çeviri sözlüğü
etiket_cevir = {
    "person": "insan",
    "car": "araba",
    "dog": "köpek",
    "cat": "kedi",
    "bicycle": "bisiklet",
    "airplane": "uçak",
    "bus": "otobüs",
    "train": "tren",
    "truck": "kamyon",
    "motorbike": "motosiklet",
    "apple": "elma",
    "book": "kitap",
    "cell phone": "telefon",
    "chair": "sandalye"
}

# Türkçe sesle nesne ismini okuma fonksiyonu
def turkce_ses_oku(metin):
    tts = gTTS(text=metin, lang='tr')
    dosya = "gecici_ses.mp3"
    tts.save(dosya)
    playsound.playsound(dosya)
    os.remove(dosya)

# Kamera başlat
cap = cv2.VideoCapture(0)

last_spoken = ""
last_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]
    frame_copy = frame.copy()

    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]
        turkce_label = etiket_cevir.get(label, label)

        if conf > 0.5:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame_copy, turkce_label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Aynı nesne tekrar tekrar söylenmesin
            if turkce_label != last_spoken or time.time() - last_time > 2:
                try:
                    turkce_ses_oku(turkce_label)
                except:
                    pass  # ses çalarken oluşabilecek hataları atla
                last_spoken = turkce_label
                last_time = time.time()

    cv2.imshow("YOLOv8 Türkçe Sesli Nesne Tanıma", frame_copy)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
