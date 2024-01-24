"""
    1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this
"""

monthly_expense = [2200, 2350, 2600, 2130, 2190]
month_map = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May" 
}
print(f"In Feb, how many dollars you spent extra compare to January: {monthly_expense[1] - monthly_expense[0]}")
print(f"Find out your total expense in first quarter (first three months) of the year: {monthly_expense[0] + monthly_expense[1] + monthly_expense[2]}")
print(f"Find out if you spent exactly 2000 dollars in any month:")
for i in monthly_expense:
    if i == 2000:
        print("I spent exactly 2000 dollars in {month_map[i]}")

print(f"June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.")