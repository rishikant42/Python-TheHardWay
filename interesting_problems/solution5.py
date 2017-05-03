import random

def rotate(line, guess):
    if guess in line:
        last_char = guess[-1]
        line.remove(guess)
        for word in line:
            if word.startswith(last_char):
	        return word
    else:
        return False
       
def main(filename):
    line = open(filename).read()
    line = line.split()

    # select first random word
    guess = random.choice(line)
    
    while guess:
        print "Player 1 ==> ", guess
        player = "player 1 win "
	guess = rotate(line, guess)
        if guess:
	    print "Player 2 ==> " , guess
            player = "player 2 win "
            guess = rotate(line, guess)
         

    print player


if __name__ == "__main__":
    main('Pokemon.txt')
