from random import randrange
from replit import clear

# To keep output clean
def refresh():
	clear()
	print("""Welcome one an all for a quick game of...
"Rock, Paper, Scissors!"

The rules are simple,
  - You and your opponent will both pick between
    the three choices. The first being rock, the
    second is paper and the third choice of scissors.

  - There are three ways to win, so choose wisely:
     1. Rock beats scissors
     2. Paper beats Rock
     3. Scissors beats paper
""")

# Bot dictionary
choices = {
  1 : "Rock",
  2 : "Paper",
  3 : "Scissors"
}
# Snarky comments based on bot & user choice
result = {
	"Rock : Rock" : "I guess neither of you are that smart, you tied.",
	"Rock : Paper" : "Just can't catch a break can you? You lose.",
	"Rock : Scissors" : "Congradulations! By slim luck you won.",
	"Paper : Rock" : "Be honest, you cheated didn't you? Either way, you win.",
	"Paper : Paper" : "That's the way the cookie crumbles, right into a tie.",
	"Paper : Scissors" : "The fates are cruel. They forged your loss long ago.",
	"Scissors : Rock" : "Uh oh, how unfortunate. You miserably lost.",
	"Scissors : Paper" : "It pains me to say this, you won.",
	"Scissors : Scissors" : "Wow...nice tie and that's not a compliment."
}

# Program Start:
refresh()
bot_choice = choices[randrange(1, 4)]
user_choice = input("""Enter your choice of "Rock", "Paper" or "Scissors": """).lower().capitalize()
# Keeping output clean while making sure user's answer is viable
while (user_choice != "Rock" and user_choice != "Paper" and user_choice != "Scissors"):
	refresh()
	print(f'''"{user_choice}" is unfortunately not a choice. Please try again.''')
	user_choice = input("""Enter your choice of "Rock", "Paper" or "Scissors": """).lower().capitalize()

# Clean up and print results
refresh()
print(f"You picked {user_choice}!")
print(f"Your opponent picked {bot_choice}!")
print()
key = (f"{user_choice} : {bot_choice}")
print(result[key])