import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/Users/zainab/Desktop/orders copy.csv')

orders_by_city = data['city'].value_counts()

# Convert to DataFrame for better display control
orders_by_city_df = orders_by_city.reset_index()
orders_by_city_df.columns = ['City', 'Order Count']

# Display all rows
pd.set_option('display.max_rows', None)



# Select top 10 cities
top_10_cities = orders_by_city_df.head(10)
# Visualization
plt.figure(figsize=(12, 8))
plt.bar(top_10_cities['City'], top_10_cities['Order Count'], color='skyblue')
plt.title('Top 10 Cities by Number of Orders')
plt.xlabel('City')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right')  # Rotate city names for better readability
plt.tight_layout()  # Adjust layout to fit everything nicely
#plt.show()


#revenue for each year
# Extract the year from the date column
data['order_date'] = pd.to_datetime(data['order_date'], format='%d/%m/%Y')

data['year'] = data['order_date'].dt.year

# Calculate the yearly revenue
yearly_revenue = data.groupby('year')['total_order_value'].sum()



plt.figure(figsize=(10, 6))
yearly_revenue.plot(kind='bar' ,  color='pink')
plt.title('yearly revenu ')
plt.xlabel('Year')
plt.ylabel('Revenue(SAR)')
plt.show()

