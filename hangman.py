import random
import hangmanlogo
import wordlist  
random_list = random.choice(wordlist.word_list)
print(random_list)
display = ['_'] * len(random_list)
lives = 8
print(display)
while True:
        guess = input("guess a letter\n").lower()
        for position in range(len(random_list)):
                if guess == random_list[position]:
                        display[position] = guess
                        print(display)
        if"".join(display) == random_list:
                print("you win")
                break
        from hangmanstage import stages
        if guess not in random_list:
                lives -= 1
                print(stages[lives])
                if lives == 0:
                        print("you lose")
                        break

   
 
    
    
        


    
    
    
