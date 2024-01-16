line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

column = position[0]
row = position[1]

if column == "A":
    column_pos = 0
if column == "B":
    column_pos = 1
if column == "C":
    column_pos = 2

if row == "1":
    row_pos = 0
if row == "2":
    row_pos = 1
if row == "3":
    row_pos = 2

map[row_pos][column_pos] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
