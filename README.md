# 🗑️ Garbage Classification using EfficientNet and Gradio

A deep learning project to classify waste images into 6 categories:  
**cardboard, glass, metal, paper, plastic, trash** using **EfficientNetV2B2** and deployed with **Gradio**.

---

## 📂 Dataset
Used the [TrashType Image Dataset](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification) from Kaggle.  
It contains 6 classes of garbage images.

---

## 🧠 Model
- Base model: `EfficientNetV2B2` (transfer learning from ImageNet)
- Image size: 124x124
- Preprocessing: `Rescaling(1./255)`
- Fine-tuned using `Adam` with class weights
- Final accuracy: >90% on validation set

---

## 🌐 Web App (Gradio)
Live demo: [Try it on Hugging Face Spaces](https://huggingface.co/spaces/JaishnaCodz/Garbage-Classification)

Upload any trash image and see the predicted category with top confidence scores.

---

## 📦 Tech Stack
- Python, TensorFlow, NumPy
- Transfer Learning (EfficientNet)
- Gradio (Web UI)
- Google Colab, Hugging Face Spaces

---

## 🚀 How to Run Locally
```bash
pip install gradio tensorflow
python app.py
