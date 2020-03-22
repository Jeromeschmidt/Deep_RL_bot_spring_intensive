import ttt
import connect4


choice = " "

while choice.lower() != "q":
    choice = input("Enter 1 to play tik-tack-toe or 2 to play connect 4 or q to quit: ")
    if choice == "1":
        ttt.Game().play()
    elif choice == "2":
        connect4.Game().play()
