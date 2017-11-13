#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com
# Graphics - Logo IFC


from graphics import *

baner = GraphWin('IFC',450,180)

circulo = Circle(Point(30,30), 20)
circulo.setFill('red')
circulo.draw(baner)

retangulo = Rectangle(Point(35,35),Point(70,70))
retangulo.setFill('green')
retangulo.draw(baner)
retangulo.move(-23, 20)

retangulo2 = retangulo.clone()
retangulo2.move(0,40)
retangulo2.draw(baner)

retangulo3 = retangulo.clone()
retangulo3.move(0,80)
retangulo3.draw(baner)

retangulo4 = retangulo.clone()
retangulo4.move(40,0)
retangulo4.draw(baner)

retangulo5 = retangulo2.clone()
retangulo5.move(40,0)
retangulo5.draw(baner)

retangulo6 = retangulo3.clone()
retangulo6.move(40,0)
retangulo6.draw(baner)

retangulo7 = retangulo2.clone()
retangulo7.move(80,0)
retangulo7.draw(baner)

retangulo8 = retangulo4.clone()
retangulo8.move(0,-40)
retangulo8.draw(baner)

retangulo9 = retangulo8.clone()
retangulo9.move(40,0)
retangulo9.draw(baner)

texto = Text(Point(100, 100), 'INSTITUTO FEDERAL DE')
texto.draw(baner)
texto.move(130,0)

texto2 = Text(Point(100, 100), 'EDUCAÇÃO, CIÊNCIA E TECNOLOGIA')
texto2.draw(baner)
texto2.move(180,20)

texto3 = Text(Point(200,200), 'CATARINENSE')
texto3.setFill('green')
texto3.draw(baner)
texto3.move(-5,-50)

texto4 = Text(Point(150,180), 'Câmpus Araquari')
texto4.setFill('green')
texto4.draw(baner)
texto4.move(50, -14)


sair = input("Tecle enter para sair!")

print(sair)



