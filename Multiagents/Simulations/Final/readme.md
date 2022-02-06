# Apocalipsis Zombie 🧟🧟
En esta simulación hay un número de zombies y de personas no infectadas en una habitación. <br>
En cada step: 
- Los zombies y personas no infectadas se mueven una celda (a una de las 8 celdas vecinas)
- Si un zombie se encuentra en la misma celda que una persona no infectada, la persona no infectada se convierte en zombie
- Si una persona no infectada llega a una pared (norte, sur, este u oeste) sobrevive y deja de moverse

La simulación termina una vez que se haya alcanzado el número máximo de steps o cuando todos los sobrevivientes se encuentren en una pared.