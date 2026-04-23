import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
# Ensure 'Instagram_Analytics.csv' is in the same folder as this script
df = pd.read_csv('Instagram_Analytics.csv')

# 2. Data Cleaning & Preparation
# Convert date column to actual datetime objects
df['upload_date'] = pd.to_datetime(df['upload_date'])

# Create Total Engagement Column (Likes + Comments + Shares)
df['Engagement'] = df['likes'] + df['comments'] + df['shares']

# Extract Day of the week for analysis
df['Day'] = df['upload_date'].dt.day_name()

print("✅ Data Loaded and Cleaned Successfully!")

# 3. Analysis: Engagement by Content Type
engagement_by_type = df.groupby('media_type')['Engagement'].sum().sort_values(ascending=False)

# 4. Analysis: Engagement by Day
engagement_by_day = df.groupby('Day')['Engagement'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# 5. Totals for Pie Chart
totals = {
    'Likes': df['likes'].sum(),
    'Comments': df['comments'].sum(),
    'Shares': df['shares'].sum()
}

# --- VISUALIZATIONS ---

# Chart 1: Engagement Over Time
plt.figure(figsize=(10, 6))
engagement_over_time = df.groupby(df['upload_date'].dt.date)['Engagement'].sum()
engagement_over_time.plot(color='blue', linewidth=2)
plt.title('Daily Engagement Trends')
plt.xlabel('Date')
plt.ylabel('Total Engagement')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('engagement_over_time.png')
print("📈 Saved: engagement_over_time.png")

# Chart 2: Engagement by Content Type
plt.figure(figsize=(8, 5))
sns.barplot(x=engagement_by_type.index, y=engagement_by_type.values, palette='viridis')
plt.title('Total Engagement by Content Type')
plt.ylabel('Engagement Count')
plt.tight_layout()
plt.savefig('engagement_by_content_type.png')
print("📈 Saved: engagement_by_content_type.png")

# Chart 3: Likes vs Comments vs Shares
plt.figure(figsize=(7, 7))
plt.pie(totals.values(), labels=totals.keys(), autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Engagement Breakdown')
plt.tight_layout()
plt.savefig('engagement_breakdown.png')
print("📈 Saved: engagement_breakdown.png")

# 6. Export Processed Data
df.to_csv('Processed_Instagram_Analytics.csv', index=False)
print("📂 Exported: Processed_Instagram_Analytics.csv")

print("\n--- Summary Statistics ---")
print(engagement_by_type)