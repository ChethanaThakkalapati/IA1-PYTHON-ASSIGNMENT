cost_hour = 0.51

cost_day = cost_hour * 24
cost_week = cost_day * 7
cost_month = cost_day * 30  # assuming 30-day month

money = 918

days_possible = money / cost_day


print("Cost to operate per day: $", cost_day)
print("Cost to operate per week: $", cost_week)
print("Cost to operate per month: $", cost_month)
print("Days you can operate with $918:", days_possible)
