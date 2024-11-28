def get_shot(guesses):
    """Prompt the user for a shot and return the shot as a (column, row) tuple."""
    while True:
        try:
            shot = input("Please enter your guess (e.g., B5): ").upper()
            
            if len(shot) != 2:
                print("Invalid input! Please enter a letter followed by a number (e.g., B5).")
                continue

            column = shot[0]
            row = int(shot[1])

            if column not in "ABCDEFG" or row not in range(1, 8):
                print("Invalid column or row. Please enter a valid guess (e.g., B5).")
                continue

            if (column, row) in guesses:
                print("You've already guessed this spot!")
                continue

            return column, row  
        except ValueError:
            print("Incorrect entry, please enter a letter and a number (e.g., B5).")

def show_board(hit, miss, comp):
    """Display the board showing hits, misses, and remaining boats."""
    print("     Battleship  ")
    print("   A B C D E F G")  
    
    for row in range(1, 8):
        row_display = ""
        for column in "ABCDEFG":
            ch = "_ "
            if (column, row) in miss:
                ch = "x " 
            elif (column, row) in hit:
                ch = "o "  
            elif (column, row) in comp:
                ch = "O "  
            row_display += ch
        print(f"{row}  {row_display}")  

def check_shot(shot, boat1, boat2, hit, miss, comp):
    """Check if the shot hits any boats and update the lists accordingly."""
    if shot in boat1:
        boat1.remove(shot)
        hit.append(shot)
        if len(boat1) == 0:
            print("Boat 1 is sunk!")
            comp.extend(hit)  
    elif shot in boat2:
        boat2.remove(shot)
        hit.append(shot)
        if len(boat2) == 0:
            print("Boat 2 is sunk!")
            comp.extend(hit)
    else:
        miss.append(shot)
    return hit, miss, comp, boat1, boat2


boat1 = [("B", 5), ("C", 5), ("D", 5)]  
boat2 = [("A", 2), ("A", 3), ("A", 4)]  

hit = []  
miss = [] 
comp = []  


for i in range(10):
    guesses = hit + miss + comp  
    shot = get_shot(guesses)  
    hit, miss, comp, boat1, boat2 = check_shot(shot, boat1, boat2, hit, miss, comp)  
    show_board(hit, miss, comp)  

 
    if len(boat1) == 0 and len(boat2) == 0:
        print("You have won!")
        break

print("Congratulations, you have finished the game!")


