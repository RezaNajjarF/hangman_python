

def draw_stick_man():
    print(
        ''' 
            ______
            |    |
            |    O
            |   /|\\
            |   / \\
            |
            |

        ''')

def take_guess():
    for letter in range(len(the_word)):
        if the_word[letter] == guess:
            found_letters[letter]='['+guess+']'
            found_lettersB.append(' ')
    

def end_game():
    
    if attemps==0:
        return (True,'LOSE!')
    elif len(found_lettersB)==len(the_word):
        return (True,'WON!')
    else:
        return (False,'LOSE!')
    
the_word=input('enter your word? ')
found_letters=[]
found_lettersB=[]
for _ in the_word:
    found_letters.append('[ ]')
attemps=int(input('how many attemps can your opponent have? '))
end=False
finished='LOSE!'
test=1

    

print('\n\n\n\n\n\n\n\n\n\n')
while end==False:

    draw_stick_man()
    print(found_letters)
    end,finished=end_game()
    if end==True:break
    print('you have %s attemps left'%attemps)
    guess=input('what is your guess? ')
    if guess==the_word:
        end=True
        finished='WON!'
    elif 0<len(guess)<2:
        take_guess()

        
    

    attemps-=1

    
print('\n\n\n\n\nyou %s\n\n\n\n\n'%finished)

    