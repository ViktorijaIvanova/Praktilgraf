from msvcrt import kbhit
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

#raam = Tk()
#raam.title("Tahvel")
#tahvel = Canvas(raam, width=600, height=600, background="white")
#tahvel.grid()

# одиночная полоска (x0, y0, x1, y1)

#tahvel.create_line(30, 40, 300, 40)

#соединенные штрихи (любое количество пар координат)

#tahvel.create_line(30,60,  300,60,  300,100,  60,100)

# есть возможность изменить толщину линии (ширину) и цвет содержимого (заливку)

#tahvel.create_line(30, 130, 300, 130, width=4, fill="red")

# другой стиль линии

#tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=LAST)

#рисует линии, соединяет конечные точки и окрашивает содержимое
# цвета также могут быть указаны как компоненты rgb
# видеть http://www.colorpicker.com/

#tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#95BD9D")

# прямоугольник

#tahvel.create_rectangle(30,260,  300,300)

# овал

#tahvel.create_oval(30,260,  300,300, width=2, outline="blue", fill="wheat")

# попробуй навести мышку на этот овал

#tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")

# если вы хотите сами выбрать шрифт при отправке текста, вы должны сначала создать соответствующий шрифт

#suur_font = font.Font(family='Helvetica', size=32, weight='bold')
#tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=NW)

#raam.mainloop()

#tahvel.create_rectangle(5,100,  260,230)
#LIPUD
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.grid()
tahvel.create_rectangle(5,5,  180,45,fill="#4599a1")
tahvel.create_rectangle(5,45,  180,90,fill="yellow")
tahvel.create_rectangle(5,130,  180,90,fill="#4599a1")
tahvel.create_polygon(5,5,  100,60,  5,130,  5,4, width=5,fill="black")

tahvel.create_rectangle(360,5,  180,45,fill="blue")
tahvel.create_rectangle(360,45,  180,90,fill="black")
tahvel.create_rectangle(360,130,  180,90,fill="white")

#tahvel.create_rectangle(600,5,  180,45,fill="red")
#tahvel.create_rectangle(600,45,  180,90,fill="blue")
#tahvel.create_rectangle(600,130,  180,90,fill="yellow")


#VALGUSFOOR

tahvel.create_rectangle(30,750,  200,300,fill="grey")
tahvel.create_rectangle(100,410,  135,375,fill="red")
tahvel.create_rectangle(100,415,  135,450,fill="yellow")
tahvel.create_rectangle(100,455,  135,490,fill="green")
tahvel.create_rectangle(115,650,  120,500,fill="black")
tahvel.create_rectangle(50,600,   180,600,width=4 )

raam.mainloop()


