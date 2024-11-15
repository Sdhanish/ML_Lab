import pandas as pd
# Create a dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
            }
# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
# Display the DataFrame
print("DataFrame:")
print(df)
# Display the structure of the DataFrame
print("\nDataFrame Structure:")
print(df.info())

# Display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())
