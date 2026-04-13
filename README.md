# 🏠 House Price Prediction - Machine Learning Project

## 📌 Project Overview

This project focuses on building a **Machine Learning model** to predict house prices based on key features such as:

* Area
* Bedrooms
* Bathrooms
* Location
* Property Type

The goal is to understand how different factors influence house prices and build a model that can make accurate predictions.

---

## 🎯 Objectives

* Perform data preprocessing and cleaning
* Build a Linear Regression model
* Evaluate model performance using metrics
* Visualize predicted vs actual prices
* Interpret important features

---

## 📂 Project Structure

```
week9/
│── house_price_prediction.py
│── house_prices.csv
│── predictions_vs_actual.png
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2️⃣ Run the Project

```bash
python house_price_prediction.py
```

---

## 🧠 Machine Learning Workflow

### 🔹 Data Preparation

* Loaded dataset using pandas
* Handled missing values
* Converted categorical variables (Location, Property Type) using encoding

### 🔹 Model Used

* **Linear Regression (scikit-learn)**

### 🔹 Train-Test Split

* 80% Training
* 20% Testing

---

## 📊 Model Performance

| Metric   | Value          |
| -------- | -------------- |
| MAE      | 2,356,914      |
| MSE      | 93,216,463,483 |
| R² Score | 0.93           |

👉 The model shows **high accuracy** with strong correlation between predicted and actual prices.

---

## 📈 Visualization

The model performance is visualized using:

* **Predicted vs Actual Prices Plot**

This shows how closely the model predictions match real values.

---

## 🔍 Key Insights

* 📌 Area is the most influential factor in price prediction
* 📌 Location significantly impacts house pricing
* 📌 Model performs well for mid-range properties
* 📌 Some variance exists for extreme values

---

## 🧪 Testing Evidence

* Model successfully trained without errors
* Predictions generated correctly
* Evaluation metrics calculated
* Visualization saved as image

---

## 🚀 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Hyperparameter tuning
* Feature scaling & selection
* Deploy model as web app

---

## 💼 Use Cases

* Real estate price prediction
* Investment analysis
* Property valuation systems

---

## 👨‍💻 Author

**Rahul K N**

---

## ⭐ Conclusion

This project demonstrates a complete beginner-friendly Machine Learning pipeline, from data preprocessing to model evaluation and visualization.

✔ Strong foundation for real-world ML projects
✔ Ready to be added to portfolio
