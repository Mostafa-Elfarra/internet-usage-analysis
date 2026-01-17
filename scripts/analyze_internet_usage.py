import pandas as pd
import matplotlib.pyplot as plt
import os

# إنشاء مجلد visuals إذا مش موجود
if not os.path.exists("../visuals"):
    os.makedirs("../visuals")

# قراءة البيانات
df = pd.read_csv("../data/internet_usage_data.csv")

# 1️⃣ إحصائيات أساسية
print("Basic Statistics:")
print(df.describe())
print("\nUsers per Region:")
print(df.groupby("Region")["Users"].sum())
print("\nAverage Bandwidth per Region:")
print(df.groupby("Region")["Bandwidth_GB"].mean())

# 2️⃣ رسم توزيع الاستهلاك (Histogram)
plt.figure(figsize=(8,5))
plt.hist(df["Bandwidth_GB"], bins=15, color="skyblue", edgecolor="black")
plt.title("Bandwidth Usage Distribution (GB)")
plt.xlabel("Bandwidth (GB)")
plt.ylabel("Number of Records")
plt.savefig("../visuals/bandwidth_distribution.png")
plt.close()

# 3️⃣ رسم متوسط الاستهلاك لكل منطقة (Bar Chart)
avg_bandwidth = df.groupby("Region")["Bandwidth_GB"].mean()
avg_bandwidth.plot(kind="bar", color="orange", figsize=(7,5), title="Average Bandwidth per Region")
plt.ylabel("Average Bandwidth (GB)")
plt.savefig("../visuals/average_bandwidth_per_region.png")
plt.close()

print("Analysis complete! Visuals saved in ../visuals/")
