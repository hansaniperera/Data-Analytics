import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Sample_Data_for_Activity (1).csv', header=0)
df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df["Normal_Distribution"])

plt.figure(figsize=(12, 6))

# First subplot: Normal vs Uniform
plt.subplot(1, 3, 1)
plt.scatter(df["Normal_Distribution"], df["Uniform_Distribution"], color='b', alpha=0.7)
plt.xlabel("Normal Distribution")
plt.ylabel("Uniform Distribution")
plt.title("Normal vs Uniform")
plt.grid(True)
plt.legend(["Normal vs Uniform"])

# Second subplot: Normal vs Exponential
plt.subplot(1, 3, 2)
plt.scatter(df["Normal_Distribution"], df["Exponential_Distribution"], color='g', alpha=0.7)
plt.xlabel("Normal Distribution")
plt.ylabel("Exponential Distribution")
plt.title("Normal vs Exponential")
plt.grid(True)
plt.legend(["Normal vs Exponential"])

# Third subplot: Normal vs Poisson
plt.subplot(1, 3, 3)
plt.scatter(df["Normal_Distribution"], df["Poisson_Distribution"], color='r', alpha=0.7)
plt.xlabel("Normal Distribution")
plt.ylabel("Poisson Distribution")
plt.title("Normal vs Poisson")
plt.grid(True)
plt.legend(["Normal vs Poisson"])

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()

# Why use scatter plot: This data set seem to be results of 4 different distributions for set of events. Therefore
# we could compare how the outcome of each distribution for each event where we could identify how the data is
# distributed and any patterns or clusters