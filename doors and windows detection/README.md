# 🪟 Door and Window Detection using YOLOv8

This project uses YOLOv8 to detect doors and windows from front-view house images. After detection, users can upload new images to replace detected doors and windows to visualize design variations.

---

## 📁 Folder Contents

- `doors_and_windows_detection.ipynb` – Jupyter notebook with training, detection, and replacement logic.
- `DoorAndWindowDetectionDataset.zip` – YOLO-formatted dataset with `door` and `window` annotations.

---

## ⚙️ Features

- Train YOLOv8 on a custom dataset.
- Predict door and window positions in house images.
- Show bounding box dimensions and object counts.
- Interactive UI for replacing objects with uploaded images.

---

## 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
