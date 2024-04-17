#In lab task 1
daily_expenses = [80, 100, 90, 120, 110, 130, 70, 150, 140, 160, 200, 180, 190, 210, 220, 250, 240, 230, 270, 260, 280, 300, 320, 310, 340, 330, 350, 370, 360, 380]
weekend_expenses = daily_expenses[-8:]
print("Weekend spendings :",weekend_expenses)
total_weekend_expenses = sum(weekend_expenses)
print("Total expenses", total_weekend_expenses)


#In lab task 2
monthly_sales = (1200, 1500, 1400, 1600, 1800, 1900, 2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300)
second_half_sales = monthly_sales[-15:]
total_sales_second_half = sum(second_half_sales)
print("Total sales for the second half of the month:", total_sales_second_half)


#post lab task
sat_sales = monthly_sales[-2::-7]
sun_sales = monthly_sales[-1::-7]
total_sales_second_half = sum(sat_sales+sun_sales)
print("Total sales for the second half of the month:", total_sales_second_half)
print("")