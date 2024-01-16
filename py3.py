from guizero import App, PushButton, Text

app = App(layout="grid")
resultado = 0
operacion = ""
oper1 = 0
oper2 = 0

def aculumar_operador(valor):
    global oper1, oper2
    if (oper1 == 0):
        oper1 = valor
    else:
        oper2 = valor

def limpiar():
    global textbox_result
    textbox_result.value = "0"

def calcular():
    global operacion, resultado, oper1, oper2
    if(operacion == "+"):
       resultado = int(oper1) + int(oper2) 
    if(operacion == "-"):
       resultado = int(oper1) + int(oper2)
    oper1 = 0
    oper2 = 0
    print(resultado)
    textbox_result.value = resultado


def restar():
    global operacion
    operacion = "-"

def sumar():
    global operacion
    operacion = "+"

b09 = PushButton(app, command=aculumar_operador, text="9", args=["9"], grid=[2,2])
b06 = PushButton(app, command=aculumar_operador, text="6", args=["6"], grid=[2,1])
b03 = PushButton(app, command=aculumar_operador, text="3", args=["3"], grid=[2,0])
b08 = PushButton(app, command=aculumar_operador, text="8", args=["8"], grid=[1,2])
b05 = PushButton(app, command=aculumar_operador, text="5", args=["5"], grid=[1,1])
b02 = PushButton(app, command=aculumar_operador, text="2", args=["2"], grid=[1,0])
b07 = PushButton(app, command=aculumar_operador, text="7", args=["7"], grid=[0,2])
b04 = PushButton(app, command=aculumar_operador, text="4", args=["4"], grid=[0,1])
b01 = PushButton(app, command=aculumar_operador, text="1", args=["1"], grid=[0,0])


bmas = PushButton(app, command=sumar, text="+", args=[], grid=[3,2])
bmenos = PushButton(app, command=restar, text="-", args=[], grid=[3,1])
bigual = PushButton(app, command=calcular, text="=", args=[], grid=[3,0])

blimpiar = PushButton(app, command=limpiar, text="C", args=[], grid=[3,4])


textbox_result = Text(app, text="0", grid=[0,4,3,4])

# b_bottom = PushButton(app, print_pos, text="span the bottom", grid=[0,2,2,1])

app.display()