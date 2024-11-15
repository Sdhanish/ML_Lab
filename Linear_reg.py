import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create a sample dataset
# This dataset has one feature (independent variable) and one target (dependent variable)
data = pd.DataFrame({
    'Feature': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Target': [1.5, 2.0, 2.7, 3.8, 5.1, 5.9, 7.1, 8.1, 9.2, 10.3]
})

# Separate features and target
X = data[['Feature']]  # Note that X should be a 2D array (DataFrame format is used here)
y = data['Target']

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize and train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Step 4: Make predictions on the test data
y_pred = linear_model.predict(X_test)

# Step 5: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Step 6: Visualize the data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, linear_model.predict(X), color='red', label='Regression Line')
plt.title ("Simple Linear Regression")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.grid(True)
plt.show()
