
################ Data cleaning the Iris dataset #################
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd

# Use the correct file path
file_path = './iris/iris.data'  # Ensure the path is correct and accessible

# Define column names
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Read the iris.data file
try:
    iris_data = pd.read_csv(file_path, header=None, names=columns)
    print(iris_data)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# load iris dataset
iris = datasets.load_iris()
# Since this is a bunch, create a dataframe
iris_df=pd.DataFrame(iris.data)
iris_df['class']=iris.target

iris_df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
#### ===> TASK 1: here - add two more lines of the code to find the number and mean of missing data

missing_values = iris_df.isnull().sum()
missing_mean = iris_df.mean()
print("Missing Values: ", missing_values)
print("missing_mean: ", missing_mean)

cleaned_data = iris_df.dropna(how="all", inplace=True) # remove any empty lines


iris_X=iris_df.iloc[:5,[0,1,2,3]]
print(iris_X)

### TASK2: Here - Write a short readme to explain above code and how we can calculate the corrolation amoung featuers with description

plt.figure(figsize=(8,6))
iris_corr = iris_df.corr()
sns.heatmap(iris_corr, annot=True)
plt.show()