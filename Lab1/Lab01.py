# In Lab Task 
daily_expenses = [80, 100, 90, 120, 110, 130, 70, 150, 140, 160, 200, 180, 190, 210, 220, 250, 240, 230, 270, 260, 280, 300, 320, 310, 340, 330, 350, 370, 360, 380]

# I am assuming weekends are the top 8 spending days
weekend_expenses = daily_expenses[-8:]
print("Weekend spendings :",weekend_expenses)

# Calculate total expenses for the weekends
total_weekend_expenses = sum(weekend_expenses)
print("Total expenses for the weekends:", total_weekend_expenses)
