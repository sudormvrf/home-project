# The Love Calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.lower()

# true = name1.count("t")
# true += name1.count("r")
# true += name1.count("u")
# true += name1.count("e")
# true += name2.count("t")
# true += name2.count("r")
# true += name2.count("u")
# true += name2.count("e")

name2 = name2.lower()

# love = name2.count("l")
# love += name2.count("o")
# love += name2.count("v")
# love += name2.count("e")
# love += name1.count("l")
# love += name1.count("o")
# love += name1.count("v")
# love += name1.count("e")

a = [name1, name2]
true = 0
love = 0
z = 0
for i in a:
    for [x] in "true":
        true += a[z].count(x)
    for [y] in "love":
        love += a[z].count(y)
    z += 1

love_score = int(str(true)+str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
