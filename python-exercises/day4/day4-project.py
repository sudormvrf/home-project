rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]

win = "You win!"
lose = "You lose!"
draw = "You draw!"

rock_results = [draw, lose, win]
paper_results = [win, draw, lose]
scissor_results = [lose, win, draw]

results_map = [rock_results, paper_results, scissor_results]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
computer_choice = random.randint(0, 2)

decision = results_map[player_choice][computer_choice]

print(f"{choices[player_choice]}")
print("Computer chose:")
print(f"{choices[computer_choice]}")
print(f"{decision}")
