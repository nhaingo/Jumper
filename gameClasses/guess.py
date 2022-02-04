"""
Attributes:
    word: the word the player is trying to guess. 
    puzzle: starts with banks and fills in letters as correctly guessed. 
    guesses: list of letters that have been guessed. 
    num_wrong_guesses:
    game_status: enum [playing, win, lose]

Methods:
    set_word(word)
    _compare: compare guess to chosen word
    get_input: verify letter
    get_previous_choices:
    display_puzzle:
    display_guesses:
    get_num_wrong:
    get_game_status:
"""