#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:17:18 2020
@author: Felana Rakotovao Andriamahefa
Projet de Vasarely 
"""
import turtle
from math import cos,sin,pi
from deformation import deformation # Etape 2:appel de la  module deformation 

def hexagone(point,longueur,col,centre,rayon):#Etape 1: definition de la fonction hexagone
    """
    La fonction peint un hexagone déformé en traçant des lignes droites entre le centre 
    et les extrémités dont la position est calculée avec la fonction deformation
    """
    turtle.hideturtle()
    turtle.speed(50) #vitesse d'éxecution du  dessin

    turtle.up()
    turtle.color('')
    C_x =point[0] #coordonnée du centre de l'hexagone correspondant aux bord de la fenêtre
    C_y = point[1]#(inf_gauche,sup_droite)
    pc=(C_x,C_y,0)
    pcprim=deformation(pc,centre,rayon)#deformation du centre par la fonctio deformation
    turtle.goto(pcprim[0],pcprim[1])# deplacement de la tortue au point d'origine deformé 
    
    turtle.down()
    """
    Dessin de la première face du pavé
    """ 
   
    turtle.color(col[0])#couleur de la première face 
    turtle.begin_fill()#commencer le remplissage
            
    X1=longueur*cos(0)+C_x
    Y1=longueur*sin(0)+C_y
    p=(X1,Y1,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    X1=longueur*cos(pi/3)+C_x
    Y1=longueur*sin(pi/3)+C_y
    p=(X1,Y1,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
   
    
    X1=longueur*cos(2*pi/3)+C_x
    Y1=longueur*sin(2*pi/3)+C_y
    p=(X1,Y1,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    turtle.goto(pcprim[0],pcprim[1])
    
    turtle.end_fill()  
                  
    """
    Dessin de la deuxième face du pavé
    """
    
        
    turtle.color(col[1])
    turtle.begin_fill()
    
    turtle.goto(pcprim[0],pcprim[1])
    
    X2=longueur*cos(2*pi/3)+C_x
    Y2=longueur*sin(2*pi/3)+C_y
    p=(X2,Y2,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    X2=-longueur+C_x
    Y2=0.0+C_y
    p=(X2,Y2,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    X2=longueur*cos(4*pi/3)+C_x
    Y2=longueur*sin(4*pi/3)+C_y
    p=(X2,Y2,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    turtle.goto(pcprim[0],pcprim[1])
    
    turtle.end_fill()
    
    """
    Dessin de la troisième face du pavé          
    """
    
            
    turtle.color(col[2])
    turtle.begin_fill()
    
    turtle.goto(pcprim[0],pcprim[1])
    
    X3=longueur*cos(4*pi/3)+C_x
    Y3=longueur*sin(4*pi/3)+C_y
    p=(X3,Y3,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    X3=longueur*cos(5*pi/3)+C_x
    Y3=longueur*sin(5*pi/3)+C_y
    p=(X3,Y3,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    X3=longueur*cos(0)+C_x
    Y3=longueur*sin(0)+C_y
    p=(X3,Y3,0)
    pprim=deformation(p,centre,rayon)
    turtle.goto(pprim[0],pprim[1])
    
    turtle.goto(pcprim[0],pcprim[1])
    
    
    turtle.end_fill()





def pavage (inf_gauche, sup_droit, longueur,col,centre,rayon): #Etape 3: definittion de la fonction pavage
    """La fonction pavage peint les hexagones déformés dont les centres,
    avant déformation, se trouvent à l’intérieur de la fenêtre (bords inclus) 
    avec l’hexagone en bas à gauche, avant déformation, 
    centré sur le point (inf_gauche, inf_gauche). 
    Pour cela, elle utilise la fonction hexagone.
    """
    alpha=pi/3
    x=inf_gauche # absisse centre du traçage du pavé ligne
    y=inf_gauche#ordoonee centre du traçage du  pavé ligne 
    point=(x,y,0)
    premier_x_pair=int(longueur*(1+cos(alpha)))#l'abscisse du nouveau centre decalé par rapport à l'origine
    y_interligne=int(longueur*sin(alpha))#decalage des pavé suivant l'ordonnee
    pas=3*longueur
    ligne=1

    while y<sup_droite:
    
        if ligne%2!=0:
            x=inf_gauche
    
        else:
            x=inf_gauche+premier_x_pair
            
        
        while x<sup_droite:
            point = (x,y)
            hexagone(point, longueur, col,centre,rayon)
            x+=pas
            
                
        ligne+=1
        y = y+y_interligne
        
    
#Etape 4 :code principal qui fait appel à la fonction pavage 
inf_gauche = -305
print('Coordonnée du point inférieur gauche de la fenêtre (val,val) :',inf_gauche)
sup_droite = 300
print('Coordonnée du point supérieur droit de la fenêtre (val,val) :',sup_droite)
longueur = 10
print('Longueur d''une arête:',longueur)
col1='blue' 
col2= "cyan" 
col3= 'green' 
col=(col1,col2,col3)
print('Couleur des faces de l''hexagone :',col)
centre=(0,0,0)
print('Coordonnée de la sphère de deformation:',centre)
rayon=250
print('Rayon du sphère de déformation :', rayon)
pavage (inf_gauche, sup_droite, longueur,col,centre,rayon)

turtle.getcanvas().postscript(file="pavage.eps")
turtle.done()    
turtle.Screen().exitonclick()



























