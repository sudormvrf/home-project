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
else:
    print("Sorry, you have to grow taller before you can ride.")
