# 🌾 Crop Yield Prediction System

## 📌 Objective
Build a system that uses machine learning to predict crop yield based on features like rainfall, temperature, soil type, and fertilizer. The data is stored in MongoDB (NoSQL database), and the entire project is coded in Python using **Visual Studio Code**.

## ⚙️ Technologies Used
- Python (VS Code)
- MongoDB (NoSQL)
- Scikit-Learn (Random Forest)
- Matplotlib / Seaborn (for visualization)
- Pymongo (MongoDB-Python Connector)

## 📂 Dataset
Sample dataset with features:
- Rainfall (mm)
- Temperature (°C)
- Soil Type
- Fertilizer Type
- Crop Yield (kg/ha)

## 🧠 ML Algorithm
Used **Random Forest Regressor** for predicting crop yield based on multiple agricultural parameters.

## 🗃️ MongoDB Integration
Crop data is stored in **MongoDB**. Python code connects to the database using `pymongo`.

**MongoDB Screenshot:**

![MongoDB Schema](screenshots/mongodb_schema.png)

## 📊 Sample Output
Input:
- Rainfall: 110 mm
- Temperature: 26°C
- Soil Type: Loamy
- Fertilizer: Organic

**Predicted Crop Yield** = 2150 kg/ha

**Prediction Visualization:**

![Prediction Result](screenshots/prediction_result.png)

## 📈 Model Performance
- Model Accuracy: **85%**
- Fast and scalable

---

## 🛠️ How to Run the Code in VS Code

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/crop-yield-prediction.git
