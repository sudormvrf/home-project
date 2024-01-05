print("Welcome to the rollercoaster!")

while True:
    height_raw = input("What is your height in cm? ")
    try:
        height = int(height_raw)
    except ValueError:
        print(f"\n'{height_raw}' is not a valid number, try again." )
    else:
        break

# print(type(height))
    
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    while True:
        age_raw = input("How old are you? ")
        try:
            age = int(age_raw)
        except ValueError:
            print(f"\n'{age_raw}' is not a valid age! Try again.")
        else:
            break
    if age >= 18:
        if age >= 45 and age <= 55:
            bill = 0
        else:
            bill += 12
    elif age > 11 and age < 18:
        bill += 7    
    else:
        bill += 5
    if bill > 0:
        answer = input("Do you want a photo, Yes or No? ")
        if answer == "Yes" or answer == "yes":
            bill += 3
    print(f"The total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

    