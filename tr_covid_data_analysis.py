import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını oku
df = pd.read_excel('tr_covid.xlsx')
df_bolgelere_gore = pd.read_excel('bolgelere_gore_hasta_sayisi.xlsx')


# Plotting the line chart for 'Yeni Hasta'
plt.plot(df['Tarih'], df['Yeni Hasta'])

# Customize the chart
plt.xlabel('Date')
plt.ylabel('New Case')
plt.title('New Case Numbers Over Time')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Calculate time and new patient rate using data
df['Tarih'] = pd.to_datetime(df['Tarih'])
df['Toplam Test'] = df['Yeni Test'].cumsum()

# Calculate the time required for 80,000,000 people to be tested
total_tests = df['Toplam Test'].iloc[-1]
p_number = 80000000
time = df['Tarih'].iloc[-1] + pd.DateOffset(days=(p_number - total_tests) / df['Yeni Test'].iloc[-1])
print("Time required for 80,000,000 people to be tested:", time)

# Remove the "Tarih" column from the DataFrame
df_bolgelere_gore = df_bolgelere_gore.drop(columns='Tarih')

# Calculate total cases for each region
region_totals = df_bolgelere_gore.sum()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(region_totals, labels=region_totals.index, autopct='%1.1f%%')
plt.title('Total Cases by Region')
plt.axis('equal')
plt.show()







