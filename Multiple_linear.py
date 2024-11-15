import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset with multiple features
data = pd.DataFrame({
    'Feature1': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Feature2': [1.1, 2.0, 2.9, 3.6, 4.5, 5.3, 6.1, 7.0, 7.8, 8.7],
    'Target': [2.5, 3.6, 4.7, 5.5, 6.9, 8.1, 9.3, 10.2, 11.4, 12.8]
})

# Separate features and target
X = data[['Feature1', 'Feature2']]
y = data['Target']

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize and train the Multiple Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Step 4: Make predictions on the test data
y_pred = linear_model.predict(X_test)

# Step 5: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Optional: Plot the predictions vs actual values for a visual check
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linewidth=2, label='Ideal Fit Line')
plt.xlabel("Actual Target")
plt.ylabel("Predicted Target")
plt.title("Multiple Linear Regression: Predicted vs Actual")
plt.legend()
plt.grid(True)
plt.show()
