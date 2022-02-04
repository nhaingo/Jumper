from random_word import Random_word
"""
attrubites:
    picture
    random_word
    guess

methods:
    start game
    _take_turn
    _display_terminal_output
    __int__


"""
'''This generates the number of blanks to match the random word'''
random_word = Random_word()
word = random_word.generate_word()
# print(word)

blanks = []

for i in range(len(word)):
    blanks.append('_ ')

#this removes all the brackets and commas then prints it. 
print(*blanks, sep='')





'''find position of a given character(s) in a string and return it as a list '''

#get the random word
s = word

#change this to be the letter the user guessed.
c = 'n'

lst = []
for pos,char in enumerate(s):
    if(char == c):
        lst.append(pos)
print(lst)

#get the values out of the list
for i in lst:
    blanks[i] = c
    
    print(i)

'''replace the blank with the letter guessed'''

#blanks[lst] = c
print(*blanks, sep='')