import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Read the sales data from a CSV file
df = pd.read_csv('sales_data.csv')

# Convert the 'Date' column to datetime if needed
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month and year from the 'Date' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Calculate the total sales
df['Total_Sales'] = df['Quantity'] * df['Price']

# Print the df
print(df)

# Group the data by month and calculate the total sales for each month
monthly_sales = df.groupby(['Year', 'Month', 'Date']).agg({'Total_Sales': 'sum'}).reset_index()

# Map month integers to abbreviated names
monthly_sales['Month'] = monthly_sales['Month'].apply(lambda x: calendar.month_abbr[x])

# Print the monthly_sales
print(monthly_sales)

# Plot the monthly sales
plt.plot(monthly_sales['Month'], monthly_sales['Total_Sales'], marker='o')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales')
plt.show()

# Save the monthly_sales DataFrame to a CSV file
monthly_sales.to_csv('monthly_sales.csv', index=False)
