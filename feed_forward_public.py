from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Build the Feedforward Neural Network (MLP)
# Hidden layer sizes can be adjusted (e.g., (10, 10) for two hidden layers with 10 neurons each)
mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

# Step 4: Train the model
mlp.fit(X_train, y_train)

# Step 5: Make predictions on the test data
y_pred = mlp.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Optional: Plot the training loss curve
plt.plot(mlp.loss_curve_) # the model’s error reduction over iterations
plt.title('Training Loss Curve')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.show()
