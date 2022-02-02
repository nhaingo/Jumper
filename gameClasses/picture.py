from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE


class Picture:   
    def __init__(self):
    # 2) Create the class constructor. Use the following method comment.
        """Constructs a new Picture.

        Args:
            self (Picture): An instance of Picture.
        """
        self.image =[[" _____"],
                    ["/","_____","\ "],
                    ["\ ","    /"],
                    [" \ ",   "  /"],
                    ["   O"],["  /|\ "],["  / \ "]] 
    #def display_image(self,image): ==> To insert and print in the result (terminal services)
        #print(image)
    

    def draw_zero_wrong(self):
        print('  _____  ')
        print(' /_____\\')
        print(' \\     /')
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')

    def draw_one_wrong(self):
        print(' /_____\\')
        print(' \\     /')
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')
    def draw_two_wrong(self):
        print(' \\     /')
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')
    def draw_three_wrong(self):
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')
    def draw_four_wrong(self):
        print('    X')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')


        
#for testing:
# jumper = Picture()
# jumper.draw_zero_wrong()
# jumper.draw_one_wrong()
# jumper.draw_two_wrong()
# jumper.draw_three_wrong()
# jumper.draw_four_wrong()