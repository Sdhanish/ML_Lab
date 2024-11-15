import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report
import matplotlib.pyplot as plt 

data = pd.read_csv('C:\\Users\\User\\Desktop\\dataset\\sample_knn_data.csv')
X = data[['Feature1','Feature2']]
y = data['Class']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))


plt.figure(figsize=(10, 6))
# Plot the training and test data points, colored by class
sns.scatterplot(x='Feature1', y='Feature2', hue='Class', data=data, palette='coolwarm', s=50)
plt.title("KNN Classification Results")
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(title='Class')
plt.grid(True)
plt.show()
