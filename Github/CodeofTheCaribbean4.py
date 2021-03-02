import sys
import math
import random
from random import randrange, choice

class Barco:
    def __init__(self,id,type,x,y,ar1,ar2,ar3,ar4):
        self.id=id
        self.type=type
        self.x=x
        self.y=y
        self.ar1=ar1 #rotation
        self.ar2=ar2 #speed
        self.ar3=ar3 #stock
        self.ar4=ar4 #1-me 0-other

class Baril:
    def __init__(self,id,type,x,y,arg):
        self.id=id
        self.type=type
        self.x=x
        self.y=y
        self.arg=arg #rum

class Canon:
    def __init__(self,id,type,x,y,arg1,arg2):
        self.id=id
        self.type=type
        self.x=x
        self.y=y
        self.arg1=arg1 #who fire
        self.arg2=arg2 #turns

class Mina:
    def __init__(self,id,type,x,y):
        self.id=id
        self.type=type
        self.x=x
        self.y=y

def distancia(Obj1,Obj2):
    r=((Obj1.x-Obj2.x)**2+(Obj1.y-Obj2.y)**2)**0.5
    return r

def direccion(v,xx,yy):
    if (True):#xx==yy:
        if v==0:
            x=1
            y=0
        elif v==1:
            x=0
            y=-1
        elif v==2:
            x=-1
            y=-1
        elif v==3:
            x=-1
            y=0
        elif v==4:
            x=-1
            y=1
        elif v==5:
            x=0
            y=1
        else:
            x=0
            y=0
    else:
        if v==0:
            x=1
            y=0
        elif v==1:
            x=1
            y=-1
        elif v==2:
            x=0
            y=-1
        elif v==3:
            x=-1
            y=0
        elif v==4:
            x=0
            y=1
        elif v==5:
            x=1
            y=1
        else:
            x=0
            y=0
    return x,y

while True:
    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)

    # iniciadores
    mBarcos=[]
    oBarcos=[]
    barriles=[]
    minas=[]
    canones=[]
    QtymBarcos=0
    QtyoBarcos=0
    Qtybarriles=0
    Qtyminas=0
    Qtycanones=0

    for i in range(entity_count):

        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        x = int(inputs[2])
        y = int(inputs[3])
        arg_1 = int(inputs[4])
        arg_2 = int(inputs[5])
        arg_3 = int(inputs[6])
        arg_4 = int(inputs[7])

        if ((entity_type=="SHIP") and (arg_4==1)):
            a1=mBarcos.append(Barco(entity_id,entity_type,x,y,arg_1,arg_2,arg_3,arg_4))
            QtymBarcos+=1
        elif ((entity_type=="SHIP") and (arg_4==0)):
            a2=oBarcos.append(Barco(entity_id,entity_type,x,y,arg_1,arg_2,arg_3,arg_4))
            QtyoBarcos+=1
        elif ((entity_type=="BARREL")):
            a3=barriles.append(Baril(entity_id,entity_type,x,y,arg_1))
            Qtybarriles+=1
        elif (entity_type=="CANNONBALL"):
            a4=canones.append(Canon(entity_id,entity_type,x,y,arg_1,arg_2))
            Qtycanones+=1
        elif (entity_type=="MINE"):
            a5=minas.append(Mina(entity_id,entity_type,x,y))
            Qtyminas+=1
        else:
            a6=0

    if QtymBarcos>0:
        for i in range(QtymBarcos):
            #   Variables de inicio
            x_goal=0
            y_goal=0
            x_fire=0
            y_fire=0
            x_oBar=0
            y_oBar=0
            x_ene=0
            y_ene=0
            x_Mina=0
            y_Mina=0
            d_1=23
            d_2=23
            d_3=23
            d_4=23
            d_5=23
            d_6=23
            x_ran=random.randint(5,15)
            y_ran=random.randint(5,15)
            vel_oBar=0

            Barco1=mBarcos[i]
            x_mibar=mBarcos[i].x
            y_mibar=mBarcos[i].y
            stock_mBar=mBarcos[i].ar3
            vel_prop=mBarcos[i].ar2

            if Qtybarriles>0:
                #
                for j in range(Qtybarriles):
                    Barril1=barriles[j]
                    d_2=distancia(Barco1,Barril1)
                    if d_2<d_1:
                        x_barr=Barril1.x
                        y_barr=Barril1.y
                        d_1=d_2 # distancias barriles
            if QtyoBarcos>0:
                #
                for k in range(QtyoBarcos):
                    Barco2=oBarcos[k]
                    d_4=distancia(Barco1,Barco2)
                    if d_4<d_3:
                        t1=1+d_4//3 #calculo del tiempo
                        t2=1+d_4//3 #calculo del tiempo
                        t11=Barco2.ar2*(direccion(Barco2.ar1,Barco2.x,Barco2.y)[0])*t1 #incrementos distancias
                        t22=Barco2.ar2*(direccion(Barco2.ar1,Barco2.x,Barco2.y)[1])*t2 #incrementos distancias

                        x_oBar=int(Barco2.x+t11)
                        y_oBar=int(Barco2.y+t22)
                        vel_oBar=Barco2.ar2
                        x_ene=Barco2.x+3
                        y_ene=Barco2.y+3
                        d_3=d_4 # distancia barcos
            if Qtyminas>0:
                #
                for p in range (Qtyminas):
                    Mina1=minas[p]
                    d_6=distancia(Barco1,Mina1)
                    if d_5>d_6:
                        x_Mina=Mina1.x
                        y_Mina=Mina1.y
                        d_5=d_6 # distancia minas

            lista_dist=[23,23,d_1,d_2,d_3,d_4,d_5,d_6]
            lista_x=[x_mibar,y_mibar,x_barr,y_barr,x_oBar,y_oBar,x_Mina,y_Mina]
            min_dist=min(lista_dist)
            for ct1 in lista_dist:
                if min_dist==d_1:
                    x_goal=x_barr
                    y_goal=y_barr
                    x_fire=x_oBar
                    y_fire=y_oBar
                    mod=10
                elif min_dist==d_3:
                    x_goal=x_oBar+6
                    y_goal=y_barr+6
                    x_fire=x_oBar
                    y_fire=y_oBar
                    mod=10
                elif min_dist==d_5:
                    x_goal=x_Mina+10
                    y_goal=y_Mina+10
                    x_fire=x_oBar
                    y_fire=y_oBar
                    mod=-10
                elif (False) and (x_mibar<2 or y_mibar<2 or x_mibar<2 or y_mibar>18):
                    x_goal=14
                    y_goal=10
                    x_fire=x_oBar
                    y_fire=y_oBar
                    mod=-10
                else:
                    x_goal=x_ran
                    y_goal=y_ran
                    x_fire=x_oBar
                    y_fire=y_oBar
                    mod=-10


            rem_rum=stock_mBar #stock
            if rem_rum<50:
                mod2=10
            else:
                mod2=-20

            vel_rum=vel_oBar #velocidad
            if vel_rum<2:
                mod3=20
            else:
                mod3=-10

            rd=random.randint(1,100)+mod+0*mod2+0*mod3*0
            if rd>100:
                print("MINE")
            elif rd>50 and rd<=100:
                print("FIRE {} {}".format(x_fire,y_fire))
            elif rd>0 and rd<=50:
                print("MOVE {} {}".format(x_goal,y_goal))
            else:
                print("WAIT")
