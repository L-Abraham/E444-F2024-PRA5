import pandas as pd
import matplotlib.pyplot as plt

#load data
df = pd.read_csv("latency_results.csv")

# calc average latency
avg_latency = df.groupby("Test Case")["Response Time (ms)"].mean()
print(avg_latency)

#create boxplot
plt.figure(figsize=(10, 6))
df.boxplot(column="Response Time (ms)", by="Test Case", grid=False)
plt.title("Latency Performance for Each Test Case")
plt.suptitle("")
plt.xlabel("Test Case")
plt.ylabel("Response Time (ms)")
plt.show()

