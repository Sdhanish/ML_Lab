import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create a simple synthetic dataset
# This dataset has two features and two classes
data = pd.DataFrame({
    'Feature1': [2.5, 3.0, 3.5, 3.7, 4.0, 4.5, 5.1, 5.5, 5.9, 6.3, 6.5, 7.0, 7.2, 8.0, 8.5, 8.7, 9.0, 9.2, 10.0, 10.5],
    'Feature2': [1.2, 1.5, 2.0, 2.3, 2.7, 3.0, 3.5, 3.8, 4.1, 4.3, 4.6, 5.0, 5.2, 5.5, 5.9, 6.2, 6.4, 6.8, 7.0, 7.5],
    'Target': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# Separate features and target
X = data[['Feature1', 'Feature2']]
y = data['Target']

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize and train the SVM model
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Step 4: Make predictions on the test data
y_pred = svm_model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Optional: Visualize the decision boundary
plt.figure(figsize=(10, 6))
plt.scatter(X['Feature1'], X['Feature2'], c=y, cmap='coolwarm', s=50)
plt.title("SVM Classification with Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Plot decision boundary
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create grid to plot the decision boundary
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50), np.linspace(ylim[0], ylim[1], 50))
Z = svm_model.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary and margins
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
plt.show()
