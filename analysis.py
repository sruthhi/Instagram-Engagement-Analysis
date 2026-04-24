import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('Instagram_Analytics.csv')

# 2. Data Cleaning & Preparation
df['upload_date'] = pd.to_datetime(df['upload_date'])
df['Day'] = df['upload_date'].dt.day_name()

# --- RMIT SPECIFIC CALCULATIONS ---

# Calculation 1: Total Engagement (Sum of interactions)
df['Total_Engagement'] = df['likes'] + df['comments'] + df['shares']

# Calculation 2: Influence Score (Weighted Engagement Model)
# Weighted: Likes (40%), Comments (30%), Shares (30%)
df['Influence_Score'] = (df['likes'] * 0.4) + (df['comments'] * 0.3) + (df['shares'] * 0.3)

print("✅ Data Cleaned & Advanced Metrics (Influence Score) Calculated!")

# --- ANALYSIS PIVOTS ---

# 1. Best Content Type (by Average Engagement Rate)
avg_engagement_by_type = df.groupby('media_type')['engagement_rate'].mean().sort_values(ascending=False)

# 2. Traffic Source Performance (The "Impressive" Pivot)
traffic_performance = df.groupby('traffic_source')['engagement_rate'].mean().sort_values(ascending=False)

# 3. Totals for Breakdown
totals = {
    'Likes': df['likes'].sum(),
    'Comments': df['comments'].sum(),
    'Shares': df['shares'].sum()
}

# --- VISUALIZATIONS ---

# Chart 1: Engagement Rate Over Time (Efficiency Metric)
plt.figure(figsize=(10, 6))
rate_over_time = df.groupby(df['upload_date'].dt.date)['engagement_rate'].mean()
rate_over_time.plot(color='#3498db', linewidth=2, marker='o', markersize=4)
plt.title('Average Engagement Rate Trends')
plt.xlabel('Date')
plt.ylabel('Engagement Rate (%)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('engagement_rate_over_time.png')

# Chart 2: Engagement by Content Type (Bar Chart)
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_engagement_by_type.index, y=avg_engagement_by_type.values, palette='magma')
plt.title('Avg Engagement Rate by Content Type')
plt.ylabel('Avg Engagement Rate (%)')
plt.tight_layout()
plt.savefig('engagement_by_content_type.png')

# Chart 3: Influence Breakdown (Pie Chart)
plt.figure(figsize=(7, 7))
plt.pie(totals.values(), labels=totals.keys(), autopct='%1.1f%%', startangle=140, colors=['#ff7f0e', '#1f77b4', '#2ca02c'])
plt.title('Total Interaction Breakdown')
plt.tight_layout()
plt.savefig('engagement_breakdown.png')

# 4. NEW: Traffic Source Performance (Bar Chart)
plt.figure(figsize=(8, 5))
sns.barplot(x=traffic_performance.index, y=traffic_performance.values, palette='viridis')
plt.title('Engagement Rate by Traffic Source')
plt.ylabel('Avg Engagement Rate (%)')
plt.tight_layout()
plt.savefig('traffic_source_performance.png')

# 6. Export Final Processed Data
df.to_csv('Processed_Instagram_Analytics.csv', index=False)
print("📂 Exported: Processed_Instagram_Analytics.csv with Influence Scores")

print("\n--- Summary Results for Portfolio ---")
print(f"Top Content Type: {avg_engagement_by_type.idxmax()}")
print(f"Top Traffic Source: {traffic_performance.idxmax()}")