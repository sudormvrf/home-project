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
        print("Your price is $12.")
    elif age > 11 and age < 18:
        print("Your price is $7.")
    else:
        print("Your price is $5.")
else:
    print("Sorry, you have to grow taller before you can ride.")
