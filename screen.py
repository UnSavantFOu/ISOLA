# coding: utf-8
from player import *
from tkinter import *
from math import sqrt



def draw(root, panel, map, player1, player2):
    if (movable(player1, player2) and movable(player2, player1)):
        for i in range(len(map)):
            for a in range(len(map[0])):
                if (map[i][a] == 0):
                    panel.create_rectangle(40*i, 40*a, 40*i+40,40*a+40, fill="#f1c40f")
                elif (map[i][a] == -1):
                    panel.create_rectangle(40*i, 40*a, 40*i+40,40*a+40, fill="#34495e")
                
                if (player1.px == i and player1.py == a):
                    panel.create_rectangle(40*i, 40*a, 40*i+40,40*a+40, fill="#e74c3c")
                elif (player2.px == i and player2.py == a):
                    panel.create_rectangle(40*i, 40*a, 40*i+40,40*a+40, fill="#3498db")
                
                panel.create_rectangle(40*i, 40*a, 40*i+40,40*a+40)
    else:
        print("term")
        panel.create_rectangle(0, 0, 280, 400, fill="#27ae60")
        if (not movable(player1, player2)):
            winner = "Joueur 2"
        else:
            winner = "Joueur 1"
        panel.create_text(138, 149, font="Courier", text="Le "+winner+" a gagné !")
    

#print(root.winfo_screenwidth()) #Pour récupérer la taille de l'écran de l'utilisateur
#print(root.winfo_screenheight()) #J'ai hésité à mettre ça

def onClick(event):
    global status
    if (status.startswith("waiting")):
        
        if (event.x//40 > 0 and event.x//40 < 40*7 and event.y > 0 and event.y < 40*10):
            if (map[event.x//40][event.y//40] == 0):
                if (status.endswith("1")):
                    dist = sqrt((event.x//40 - player1.px)**2 + (event.y//40 - player1.py)**2)
                    if (dist<2):
                        status = "place1"
                        player1.px = event.x//40
                        player1.py = event.y//40 
                        draw(root, panel, map, player1, player2)
                        

                if (status.endswith("2")):
                    dist = sqrt((event.x//40 - player2.px)**2 + (event.y//40 - player2.py)**2)
                    if (dist<2):
                        status = "place2"
                        player2.px = event.x//40
                        player2.py = event.y//40
                        draw(root, panel, map, player1, player2)
    elif (status.startswith("place")):

        if (event.x//40 > 0 and event.x//40 < 40*7 and event.y > 0 and event.y < 40*10):
            if (map[event.x//40][event.y//40] == 0):
                if (not player1.px == event.x//40 or not player1.py == event.y//40):
                    if (not player2.px == event.x//40 or not player2.py == event.y//40):
                        map[event.x//40][event.y//40] = -1
                        draw(root, panel, map, player1, player2)
                        if (status.endswith("1")):
                            status = "waiting2"
                        else:
                            status = "waiting1"
            
def movable(player, other_player):
    n=0
    for i in range(-1,2):
        for a in range(-1,2):
            if (i+player.px >= 0 and i+player.px < len(map)):
                if (a+player.py >= 0 and a+player.py < len(map[0])):
                    if (not a == 0 or not i == 0):
                        if (map[i+player.px][a+player.py] == 0):
                            if (not other_player.px == i+player.px or not other_player.py == a+player.py):
                                n+=1
    
    if (n==0):
        return False
    else:
        return True
    

player1 = Player(3,0)
player2 = Player(3,9)

status = "waiting1"

root = Tk()

#Configuration de la page
root.title("Isola")
root.geometry("720x480")
root["bg"] = "#95a5a6"
root.bind("<Escape>", lambda e: e.widget.quit())
root.bind("<Button-1>", onClick)

#Titre
title = Label(root, text="Isola", bg="#95a5a6")
title.config(font=("Courier",34))
title.pack()

#Création de la zone de dessin
panel = Canvas(root, width=277, height=397, background="#f1c40f", borderwidth=0)

map = [[0 for i in range(10)] for a in range(7)]
draw(root, panel, map, player1, player2)

panel.pack()
panel.place(x=220,y=40)


root.mainloop()