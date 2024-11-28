def get_shot(guesses):
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess (0-48): ")
            shot = int(shot)
            if shot < 0 or shot > 48:
                print("Invalid number, please try again.")
            elif shot in guesses:
                print("You've already guessed this spot!")
            else:
                ok = "Yes"
                break
        except ValueError:
            print("Incorrect entry, please enter a number between 0 and 48:")
    return shot

def show_board(hit, miss, comp):
    print("     Battleship  ")
    print("   A B C D E F G")
    
    place = 0
    for x in range(7):
        row = ""
        for i in range(7):
            ch = "_ "
            if place in miss:
                ch = "x "
            elif place in hit:
                ch = "o "
            elif place in comp:
                ch = "O "
            row = row + ch
            place = place + 1
        print(x, "", row)
def check_shot(boat1,hit,miss,comp):
    if shot in boat1:
        hit.append(shot)
    else :
        miss.append(shot)
    return hit,miss,comp
boat1=[45,46,47]
hit = []  # List of hit positions
miss = []  # List of missed positions
comp = []  # List of computer's ship positions (not shown to player)
guesses = hit + miss + comp  # All positions that have been guessed
shot=get_shot(guesses)
hit,miss,comp=check_shot(boat1,hit,miss,comp)
show_board(hit, miss, comp)


