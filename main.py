
import ttt
import connect4


choice = int(input("Press 1 to play tik-tack-toe or 2 to play connect 4: "))

if choice == 1:
    ttt.Game().play()
else:
    connect4.Game().play()
