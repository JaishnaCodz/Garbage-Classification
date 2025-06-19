# 🗑️ Garbage Classification Using EfficientNet and Gradio

A deep learning project to classify waste images into 6 categories using transfer learning with EfficientNetV2B2, deployed as a web app using Gradio and Hugging Face Spaces.

![Banner](![garbage banner pic](https://github.com/user-attachments/assets/490419fb-26d6-49f5-96ba-f1cdc32f3cb2)
) <!-- Replace this with your own image later -->

---

## 📂 Dataset
- **Source:** [TrashType Garbage Dataset (Kaggle)](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification)
- **Classes:** `cardboard`, `glass`, `metal`, `paper`, `plastic`, `trash`
- **Preprocessing:** Resized to 124x124, class-balanced using `class_weight`

---

## 🧠 Model Architecture
- **Base Model:** EfficientNetV2B2 (pretrained on ImageNet)
- **Layers Added:**
  - Rescaling
  - GlobalAveragePooling2D
  - Dense (128 neurons, ReLU)
  - Dense (6 outputs, Softmax)

- **Fine-Tuning:** Base model layers unfrozen and retrained with low learning rate
- **Optimizer:** Adam (`lr = 1e-5`)
- **Loss:** Sparse Categorical Crossentropy

---

## 🔬 Model Evaluation

| Metric      | Value       |
|-------------|-------------|
| Accuracy    | ~92%        |
| Validation  | Balanced across all 6 classes |
| Tools Used  | Confusion matrix, classification report |

---

## 🌐 Web App

✅ Try the model live:  
👉 [Gradio Demo on Hugging Face Spaces](https://huggingface.co/spaces/JaishnaCodz/Garbage-Classification)

### 📸 Sample Output:

![Sample Prediction](![sample garbage op](https://github.com/user-attachments/assets/739fa4c0-1353-4499-9c6c-761744951ece)
)
) <!-- Replace with your image -->

---

## 🚀 Getting Started Locally

### Requirements

```bash
pip install gradio tensorflow numpy pillow
