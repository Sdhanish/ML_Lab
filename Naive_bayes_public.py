import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target labels

# Create a DataFrame for easier visualization
df = pd.DataFrame(data=X, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in y]

# Display the first few rows of the DataFrame
print("Iris Dataset:")
print(df.head())

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Naïve Bayes classifier
gnb = GaussianNB()

# Fit the classifier to the training data
gnb.fit(X_train, y_train)

# Make predictions on the test data
y_pred = gnb.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print(f'Accuracy of Naïve Bayes classifier: {accuracy * 100:.2f}%')
print("\nClassification Report:\n", classification_report(y_test, y_pred))
