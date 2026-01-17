import pandas as pd
import numpy as np
import os

# إنشاء مجلد data إذا مش موجود
if not os.path.exists("../data"):
    os.makedirs("../data")

# إنشاء البيانات الوهمية
regions = ["North", "South", "East", "West"]
users = np.random.randint(50, 500, size=100)  # عدد المستخدمين لكل سجل
region_data = np.random.choice(regions, size=100)
bandwidth = np.random.uniform(1.0, 100.0, size=100)  # استهلاك بالـ GB
peak_time = np.random.choice(["Morning", "Afternoon", "Evening", "Night"], size=100)

df = pd.DataFrame({
    "Region": region_data,
    "Users": users,
    "Bandwidth_GB": bandwidth,
    "Peak_Time": peak_time
})

# حفظ البيانات
df.to_csv("../data/internet_usage_data.csv", index=False)
print("Data generated and saved to ../data/internet_usage_data.csv")
