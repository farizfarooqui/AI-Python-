print('********************* In Lab Task 01 *****************************')

daily_expenses = [80, 100, 90, 120, 110, 130, 70, 150, 140, 160, 200, 180, 190, 210, 220, 250, 240, 230, 270, 260, 280, 300, 320, 310, 340, 330, 350, 370, 360, 380]

# i am assuming weekends are the top 8 spending days
weekend_expenses = daily_expenses[-8:]
print("Weekend spendings :",weekend_expenses)

# Calculate total expenses for the weekends
total_weekend_expenses = sum(weekend_expenses)
print("Total expenses for the weekends:", total_weekend_expenses)

print("")
print('********************* In Lab Task 02 *****************************')

monthly_sales = (1200, 1500, 1400, 1600, 1800, 1900, 2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300)

#second half of the month using negative indexing
second_half_sales = monthly_sales[-15:]
total_sales_second_half = sum(second_half_sales)
print("Total sales for the second half of the month:", total_sales_second_half)
print("")


print('********************* Post lab task *****************************')

sales_data = [1200, 1500, 1400, 1600, 1800, 1900, 2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300]

# i am assuming weekends have higher sales compared to weekdays, considering days with sales figures higher than the average sales as weekends
average_sales = sum(sales_data) / len(sales_data)
print("Average sales : " , average_sales)
weekend_days = [day for day, sales in enumerate(sales_data) if sales > average_sales]

# extract sales figures for the identified weekend days
weekend_sales = [sales_data[i] for i in weekend_days]
print("Weedend sales :" , weekend_sales)
total_weekend_sales = sum(weekend_sales)
print("Total Sales for the Weekends:", total_weekend_sales)
