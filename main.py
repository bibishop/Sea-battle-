print("Welcome to Sea battle game ")
m=input("What is your name")
print("Welcome to the game"+m)
def show_board(hit,miss,comp):
    print("   Battleship  ")
    print("   A B C D E F G")
    place=0
    for x in range(7):
        row=""
        for i in range(7):
            ch="_ "
            if place in miss :
                ch="x "
            elif place in hit :
                ch="o "
            elif place in comp:
                ch="O "
                
            row=row+ch
        print(x,"",row)
print(show_board)
hit=[21,22]
miss=[20,21,12,13]
comp=[23]


show_board(hit,miss,comp)
