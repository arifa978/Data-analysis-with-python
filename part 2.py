import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('tourist_record.csv')
file_path = "tourist_record.csv"
df = pd.read_csv(file_path)

#scatterplot
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Number_of_Companions'], y=df['Total_Travel_Cost'], hue=df['Accommodation_Type'])
plt.title('Total Travel Cost vs. Number of Companions')
plt.xlabel('Number of Companions')
plt.ylabel('Total Travel Cost')
plt.show()

# Pie chart: Distribution of the first 15 'latitude' categories
P_Value_counts = data['City_Visited'][:15].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(P_Value_counts, labels= P_Value_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('City_Visited (First 5 Data Points)')
plt.show()

# Line chart
plt.figure(figsize=(10, 6))
plt.plot(data['Number_of_Companions'][:15], label='Number_of_Companions', marker='o')
plt.title('tourist_record (First 10 Data Points)')
plt.xlabel('Number_of_Companions')
plt.ylabel('Total_Travel_Cost')
plt.legend()
plt.grid(True)
plt.show()

# Histogram: Distribution of 'longitude'
plt.figure(figsize=(8, 6))
plt.hist(data['Mode_of_Travel'], bins=15, color='blue', edgecolor='black')
plt.title('')
plt.xlabel('Mode_of_Travel')
plt.ylabel('Travel_Duration_Days')
#plt.grid(True)
plt.show()