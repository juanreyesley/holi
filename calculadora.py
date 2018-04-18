import turtle

def dibujarBoton(n,x,y):
    """
    Descripcion: Procedimiento que hace los botones de la calculadora
    Entradas: Ninguna
    Salidas: Dibuja los botones de la calculadora 
    """
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color("gray")
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.penup()
    turtle.goto(x+25,y-40)
    turtle.write(n,align="center",font=("Arial",20,"normal"))
    turtle.end_fill()

def dibujarCalculadora():
    """
    Descripcion: Procedimiento que dibuja la calculadora
    Entradas: Ninguna
    Salida: Dibujo en el mundo de la tortuga
    """
    turtle.reset()
    turtle.speed(20)
    turtle.hideturtle()

    # Dibuja la parte exterior
    turtle.color("teal")
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.pensize(3)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(200)
    turtle.end_fill()


    dibujarBoton(1,-160,-50)
    dibujarBoton(2,-85,-50)
    dibujarBoton(3,-15,-50)
    dibujarBoton(4,-160,20)
    dibujarBoton(5,-85,20)
    dibujarBoton(6,-15,20)
    dibujarBoton(7,-160,80)
    dibujarBoton(8,-85,80)
    dibujarBoton(9,-15,80)
    dibujarBoton(0,-160,-120)
    dibujarBoton(".",-85,-120)
    dibujarBoton("=",-15,-120)
    dibujarBoton("x",60,80)
    dibujarBoton("/",60,20)
    dibujarBoton("+",60,-50)
    dibujarBoton("-",60,-120)
    dibujarBoton("C",125,80)

    
def DibujarDisPlay():
    """
    Descripcion: Procedimiento para dibujar el display de la calculadora en el mundo de la tortuga
    Entrada: Ninguna
    Salida: Dibuja el display de la calculadora en el mundo de la tortuga 
    """
    
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color("white")
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(360)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-150,110)
    turtle.setheading(0)
    

a = ""
b = ""
op = ""
r = ""

def haceClick(x,y):
    """
    Descripcion: Procedimiento para definir los numero y las operaciones que sale en la calculadora
    Entrada: Hace click en la pantalla para elegir un numero y una operacion 
    Salida: Muestra en el mundo de la tortuga el numero y la operacion que desea el usuario 
    """
    
    global a,b,op,r
    
    if(x > -160 and x < -110 and y < 80 and y > 30 and turtle.xcor()<180):
        turtle.write(7,move=True, align="center", font=("Arial",25,"bold"))        
        turtle.forward(10)
        if op == "":
            a = a + "7"
        else:
            b = b + "7"
    else:
        if(x > -85 and x < -35 and y < 80 and y > 30 and turtle.xcor()<180):
            turtle.write(8,move=True, align="center", font=("Arial",25,"bold"))
            turtle.forward(10)
            if op == "":
                a = a + "8"
            else:
                b = b + "8"
        else:
            if(x > -15 and x < 35 and y < 80 and y > 30 and turtle.xcor()<180):
                turtle.write(9,move=True, align="center", font=("Arial",25,"bold"))
                turtle.forward(10)
                if op == "":
                    a = a + "9"
                else:
                    b = b + "9"
            else:
                if(x > -160 and x < -110 and y < 20 and y > -30 and turtle.xcor()<180):
                    turtle.write(4,move=True, align="center", font=("Arial",25,"bold"))
                    turtle.forward(10)
                    if op == "":
                        a = a + "4"
                    else:
                        b = b + "4"
                else:
                    if(x > -85 and x < -35 and y < 20 and y > -30 and turtle.xcor()<180):
                        turtle.write(5,move=True, align="center", font=("Arial",25,"bold"))
                        turtle.forward(10)
                        if op == "":
                            a = a + "5"
                        else:
                            b = b + "5"
                    else:
                        if(x > -15 and x < 35 and y < 20 and y > -30 and turtle.xcor()<180):
                            turtle.write(6,move=True, align="center", font=("Arial",25,"bold"))
                            turtle.forward(10)
                            if op == "":
                                a = a + "6"
                            else:
                                b = b + "6"
                        else:
                            if(x > -160 and x < -110 and y < -50 and y > -100 and turtle.xcor()<180):
                                turtle.write(1,move=True, align="center", font=("Arial",25,"bold"))
                                turtle.forward(10)
                                if op == "":
                                    a = a + "1"
                                else:
                                    b = b + "1"
                            else:
                                if(x > -85 and x < -35 and y < -50 and y > -100 and turtle.xcor()<180):
                                    turtle.write(2,move=True, align="center", font=("Arial",25,"bold"))
                                    turtle.forward(10)
                                    if op == "":
                                        a = a + "2"
                                    else:
                                        b = b + "2"
                                else:
                                    if(x > -15 and x < 35 and y < -50 and y > -100 and turtle.xcor()<180):
                                        turtle.write(3,move=True, align="center", font=("Arial",25,"bold"))
                                        turtle.forward(10)
                                        if op == "":
                                            a = a + "3"
                                        else:
                                            b = b + "3"
                                    else:
                                        if(x > -160 and x < -110 and y < -120 and y > -170 and turtle.xcor()<180):
                                            turtle.write(0,move=True, align="center", font=("Arial",25,"bold"))
                                            turtle.forward(10)
                                            if op == "":
                                                a = a + "0"
                                            else:
                                                b = b + "0"
                                        else:
                                            if(x > -85 and x < -35 and y < -120 and y > -170 and turtle.xcor()<180):
                                                turtle.write(".",move=True, align="center", font=("Arial",25,"bold"))
                                                turtle.forward(10)
                                                if op == "":
                                                    a = a + "."
                                                else:
                                                    b = b + "."
                                            else:
                                                if(x > -15 and x < 35 and y < -120 and y > -170 and turtle.xcor()<180):
                                                    turtle.write("=",move=True, align="center", font=("Arial",25,"bold"))
                                                    turtle.forward(10)
                                                    a = float (a)
                                                    b = float (b)
                                                    DibujarDisPlay()
                                                    if op == "-":
                                                        r = a - b
                                                    else:
                                                        if op == "+":
                                                            r = a + b
                                                        else:
                                                            if op == "x":
                                                                r = a * b
                                                            else:
                                                                if op == "/":
                                                                    r = a / b
                                                    turtle.write(r, font=("Arial",25,"bold"))
                                                else:
                                                    if(x > 60 and x < 110 and y < -120 and y > -170 and turtle.xcor()<180):
                                                        turtle.write("-",move=True, align="center", font=("Arial",25,"bold"))
                                                        turtle.forward(10)
                                                        op = "-"
                                                    else:
                                                        if(x > 60 and x < 110 and y < 80 and y > 30 and turtle.xcor()<180):
                                                            turtle.write("x",move=True, align="center", font=("Arial",25,"bold"))
                                                            turtle.forward(10)
                                                            op = "x"
                                                        else:
                                                            if(x > 60 and x < 110 and y < 20 and y > -30 and turtle.xcor()<180):
                                                                turtle.write("/",move=True, align="center", font=("Arial",25,"bold"))
                                                                turtle.forward(10)
                                                                op = "/"
                                                            else:
                                                                if(x > 60 and x < 110 and y < -50 and y > -100 and turtle.xcor()<180):
                                                                    turtle.write("+",move=True, align="center", font=("Arial",25,"bold"))
                                                                    turtle.forward(10)
                                                                    op = "+"
                                                                else:
                                                                    if(x > 125 and x < 175 and y < 80 and y > 30):
                                                                        DibujarDisPlay()
                                                                        a = ""
                                                                        b = ""
                                                                        op = ""
                                                                        r = ""
                                                                
    
def  calculadora():
    """
    Descripcion: Programa que hace una calculadora
    Entradas: El usuario ingresara datos por medio del mouse
    Salida: Por pantalla se apreciara el resutlado
    """

    dibujarCalculadora()
    DibujarDisPlay()
    
    turtle.onscreenclick(haceClick)
    
calculadora()
