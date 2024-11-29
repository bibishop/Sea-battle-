import random
print("Welocome to Sea battle game from Bolotova K.")
n=input("What is your name :")
def place_ships():
   
    def is_valid_position(ship, all_ships):
   
        for segment in ship:
            if segment in all_ships:
                return False

            col, row = segment
            adjacent_positions = [
                (col + dx, row + dy)
                for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                if 0 <= col + dx <= 6 and 0 <= row + dy <= 6
            ]
            if any(pos in all_ships for pos in adjacent_positions):
                return False
        return True

    def generate_ship(size):
        """Generate a valid ship of a given size."""
        while True:

            orientation = random.choice(['H', 'V']) 
            if orientation == 'H':  
                col_start = random.randint(0, 6 - size + 1)
                row_start = random.randint(0, 6)
                ship = [(col_start + i, row_start) for i in range(size)]
            else: 
                col_start = random.randint(0, 6)
                row_start = random.randint(0, 6 - size + 1)
                ship = [(col_start, row_start + i) for i in range(size)]

            if is_valid_position(ship, all_ships):
                return ship

    all_ships = []
    ships = []

  
    ship1 = generate_ship(3)
    ships.append(ship1)
    all_ships.extend(ship1)

 
    for _ in range(2):
        ship = generate_ship(2)
        ships.append(ship)
        all_ships.extend(ship)

   
    for _ in range(4):
        ship = generate_ship(1)
        ships.append(ship)
        all_ships.extend(ship)

    return ships

def show_board(hit, miss, comp):
   
    print("     Battleship  ")
    print("   0 1 2 3 4 5 6")
    
    for row in range(7):
        line = f"{row}  "
        for col in range(7):
            position = (col, row)
            if position in miss:
                line += "x "
            elif position in hit:
                line += "o "
            elif position in comp:
                line += "~ "
            else:
                line += ". "
        print(line)

def get_shot(guesses):
  
    while True:
        try:
            shot = input("Enter your guess as two numbers (row column, e.g., '2 3'): ")
            parts = shot.strip().split()
            if len(parts) != 2:
                raise ValueError("You must enter two numbers separated by a space.")
            
            row, col = int(parts[0]), int(parts[1])
            
            if not (0 <= col <= 6 and 0 <= row <= 6):
                print("Coordinates are out of bounds. Try again.")
            elif (col, row) in guesses:
                print("You've already guessed this spot!")
            else:
                return (col, row)
        except ValueError as e:
            print("Invalid input. Please try again.")

def check_shot(shot, ships, hit, miss, comp):
    """Check the player's shot and update the game state."""
    for ship in ships:
        if shot in ship:
            ship.remove(shot)
            hit.append(shot)
            if len(ship) == 0:
                comp.extend(ship)
                print("You sunk a ship!")
            return hit, miss, comp, ships
    miss.append(shot)
    return hit, miss, comp, ships


ships = place_ships()
hit = []
miss = []
comp = []


for _ in range(50): 
    guesses = hit + miss + comp
    show_board(hit, miss, comp)
    shot = get_shot(guesses)
    hit, miss, comp, ships = check_shot(shot, ships, hit, miss, comp)

    if all(len(ship) == 0 for ship in ships):
        show_board(hit, miss, comp)
        print("You have won!")
        break

print("Congratulations, you have finished the game!")


