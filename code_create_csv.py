import csv

# Data to be written to the CSV file
data = [
    [5.1, 3.5, 'Iris-setosa'],
    [4.9, 3.0, 'Iris-setosa'],
    [4.7, 3.2, 'Iris-setosa'],
    [4.6, 3.1, 'Iris-setosa'],
    [5.0, 3.6, 'Iris-versicolor'],
    [5.4, 3.9, 'Iris-versicolor'],
    [5.5, 3.5, 'Iris-versicolor'],
    [5.7, 3.8, 'Iris-versicolor'],
    [6.3, 3.3, 'Iris-virginica'],
    [6.5, 3.0, 'Iris-virginica'],
    [6.7, 3.1, 'Iris-virginica'],
    [6.9, 3.1, 'Iris-virginica']
]

# Column headers
headers = ['Feature1', 'Feature2', 'Class']

# Create and write to CSV
with open('sample_knn_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the header row
    writer.writerows(data)  # Write the data rows

print("CSV file 'sample_knn_data.csv' created successfully.")
