#Step 4
from replit import clear
import random
import hangman_words
import hangman_art

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
#Testing code
print(hangman_art.logo)
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    flag=True
    #Check guessed letter
    if guess in display:
      print("You already guessed for this letter! Try another one! ")
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
          
          display[position] = letter
          flag=False
          
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    #Join all the elements in the list and turn it into a String.
          
    if flag:
      
      print("Your guess was incorrect thus subtracting a chance by 1")
      
      lives-=1
      print(hangman_art.stages[lives])
      print(f"{lives} are left!")
      if lives==0:
        print("You loose")
        break
        
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

