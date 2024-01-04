
#Bill Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 18, 20, or 25? "))
num_people = int(input("How many people to split the bill? "))

to_pay_bill = (bill / num_people)
to_pay_tip = (bill / num_people) * (tip_percent/100)
to_pay = "{:.2f}".format(to_pay_bill+to_pay_tip)

print(f"Each person should pay: ${to_pay}")
