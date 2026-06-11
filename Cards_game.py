#♦️♥️♠️♣️
import random
import os
corazon=[(1,'♥️'),(2,'♥️'),(3,'♥️'),(4,'♥️'),(5,'♥️'),(6,'♥️'),(7,'♥️'),(8,'♥️'),(9,'♥️'),(10,'♥️'),(10,'♥️'),(10,'♥️'),(10,'♥️')]
diamante=[(1,'♦️'),(2,'♦️'),(3,'♦️'),(4,'♦️'),(5,'♦️'),(6,'♦️'),(7,'♦️'),(8,'♦️'),(9,'♦️'),(10,'♦️'),(10,'♦️'),(10,'♦️'),(10,'♦️')]
pica=[(1,'♠️'),(2,'♠️'),(3,'♠️'),(4,'♠️'),(5,'♠️'),(6,'♠️'),(7,'♠️'),(8,'♠️'),(9,'♠️'),(10,'♠️'),(10,'♠️'),(10,'♠️'),(10,'♠️')]
trebol=[(1,'♣️'),(2,'♣️'),(3,'♣️'),(4,'♣️'),(5,'♣️'),(6,'♣️'),(7,'♣️'),(8,'♣️'),(9,'♣️'),(10,'♣️'),(10,'♣️'),(10,'♣️'),(10,'♣️')]
baraja=corazon+diamante+pica+trebol#guardamos todo en baraja
mano=[]#array dinamico
descarte=[]#tambien dinamico
def tomarcarta():
    global baraja#lo que hay en baraja estará en todos lados, no es local
    pos=random.randint(0,len(baraja)-1)#carta al azar
    carta=baraja[pos]#guardamos la carta
    baraja.pop(pos)#pop elimina la carta de la baraja y la presta en otro lado
    return carta

def jugar():
    global mano, descarte, baraja#baraja ya era global, pero x
    print("dame un numero para adivinar(si te pasas perderás >B) )")
    numero=int(input(""))#lo apropiado es que sea siempre un 21
    suma=0
    while suma<numero:
        suma=0
        mano.append(tomarcarta())#mano guarda cada carta que haya salido
        os.system('cls' if os.name=='nt' else 'clear')
        print("tu mano es: ",end="")#tengo duda con ese end
        for i in range(len(mano)):
            print(mano[i][0],mano[i][1],end="  ")#mostramos carta
            suma=suma+mano[i][0]#hacemos la sumatoria de las cartas
        print("")
        print("La suma de tus cartas es: ",suma)
        if suma>numero:
            print("perdiste")#cuando se pasa de la cuenta
        else:
            print("Quieres otra carta?(y/n)")
            des=input("")
            if des=="n" or des=="N":#para volver a jugar 
                break
            if (baraja==[]):
                print("esta vacia la baraja")
                baraja=descarte
                descarte=[]#el descarte se vacía y rellena la baraja de nuevo
print("Bienvenido al juego de cartas ")
juego=True
while juego:
    jugar()
    print(mano)
    print(baraja)#el juego es llamar las funciones anteriores
    descarte=descarte+mano#se llena el descarte
    print(descarte)
    mano=[]
    print("Quieres seguir jugando?(y/n)")
    decision=input("")
    if decision=="n" or decision=="N":
        juego=False#para salir