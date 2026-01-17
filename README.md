# Internet Usage Analysis

**Description:**  
Analysis of internet usage per region with synthetic data, Python scripts, and visualizations.  
This project simulates internet bandwidth usage across different regions and provides insights through charts and statistics.

---

## Project Structure

internet-usage-analysis/
├── data/ # Contains the synthetic CSV data
├── scripts/ # Python scripts for data generation and analysis
│ ├── generate_internet_data.py
│ └── analyze_internet_usage.py
├── visuals/ # Generated charts/visualizations
└── README.md # Project explanation


---

## Features

- Generates synthetic internet usage data for multiple regions.
- Analyzes the number of users and bandwidth usage.
- Calculates average bandwidth per region.
- Visualizes data through:
  - Histogram of bandwidth distribution
  - Bar chart of average bandwidth per region
- Fully automated using Python (Pandas, Matplotlib).

---

## Tools & Technologies

- **Python 3.x**
- **Pandas** for data handling
- **Matplotlib** for visualizations
- **Git & GitHub** for version control

---

## How to Run

1. **Generate synthetic data:**

```bash
cd scripts
python generate_internet_data.py

Outcome / Results

CSV file: data/internet_usage_data.csv

Visualizations: visuals/bandwidth_distribution.png and visuals/average_bandwidth_per_region.png

Insights: average bandwidth per region, usage distribution, peak usage times.


