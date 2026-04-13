import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("🚀 Starting House Price Prediction...")

# ================================
# 1. LOAD DATA
# ================================

df = pd.read_csv(r"C:\Users\Dell\OneDrive\Documents\devoloper arena\week8\house_prices.csv")

print("\n✅ Data Loaded")
print(df.head())

# ================================
# 2. CLEAN DATA
# ================================

df.columns = df.columns.str.lower()

# Convert categorical to numbers
df = pd.get_dummies(df, drop_first=True)

# ================================
# 3. DEFINE FEATURES & TARGET
# ================================

X = df.drop('price', axis=1)
y = df['price']

# ================================
# 4. TRAIN-TEST SPLIT
# ================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 5. TRAIN MODEL
# ================================

model = LinearRegression()
model.fit(X_train, y_train)

print("\n✅ Model Trained")

# ================================
# 6. PREDICTIONS
# ================================

y_pred = model.predict(X_test)

# ================================
# 7. EVALUATION
# ================================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print("========================")
print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("R² Score:", round(r2, 2))

# ================================
# 8. VISUALIZATION
# ================================

plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Predicted vs Actual Prices")
plt.savefig("predictions_vs_actual.png")

print("\n📈 Plot saved: predictions_vs_actual.png")

# ================================
# 9. FEATURE IMPORTANCE
# ================================

importance = pd.Series(model.coef_, index=X.columns)
print("\n🔥 Important Features:")
print(importance.sort_values(ascending=False))

print("\n✅ WEEK 9 COMPLETED SUCCESSFULLY")