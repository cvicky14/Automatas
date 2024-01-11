import tkinter as tk
import tkinter

class Automatas:

  def identificador(cadena):
      estado = 1
      contador = 0
      while contador < len(cadena):
        simbolo = str(cadena[contador])
        #if anidados
        if estado == 1:
          if simbolo.isalpha():
            estado = 3
          elif simbolo == "_":
            estado = 3
          elif simbolo >= "0" and simbolo <="9":
            estado = 2
          else:
            break

        elif estado == 2:
          break

        elif estado ==3:
          if simbolo.isalpha():
            estado = 3
          elif simbolo >="0" and simbolo <="9":
            estado = 3
          else:
            return ""

        contador +=1
      #estado aceptable
      if estado != 3:
        return "la cadena: "+cadena+" es INVALIDA\n"
      else:
        return ""
    
  def numeroReal(cadena):
    estado = 1 
    for simbolo in cadena:
      #if anidados
      if estado==1: 
        if simbolo >="0" and simbolo <="9": 
          estado = 2     
        elif simbolo == "+" and simbolo == "-": 
          estado = 2    
        else: 
          break

      if estado == 2: 
        if simbolo >="0" and simbolo <="9": 
          estado = 2 
        elif simbolo == ".": 
          estado = 3 
        elif simbolo == "E": 
          estado = 5 
        else: 
          break

      if estado==3: 
        if simbolo >="0" and simbolo <="9": 
          estado = 4 
        else: 
          break 

      if estado==4: 
        if simbolo >="0" and simbolo <="9": 
          estado = 4 
        elif simbolo =="E": 
          estado = 5 
        else: 
          break 

      if estado ==5: 
        if simbolo >= "0" and simbolo <= "9": 
          estado = 7   
        elif simbolo == "+" and simbolo == "-": 
          estado = 6   
        else:
          break

      if estado ==6: 
        if simbolo >= "0" and simbolo <= "9": 
          estado = 7

      if estado ==7: 
        if simbolo >= "0" and simbolo <= "9": 
          estado = 7
    #estados aceptables
    if estado != 2 and estado != 4 and estado != 7:
      return "la cadena: "+cadena+" es INVALIDA\n"
    else:
      return ""

  def NumeroHexadecimal(cadena):
    estado = 0
    contador = 0
    while contador < len(cadena):
      simbolo = str(cadena[contador])
      #if anidados
      if estado == 0:
        if simbolo == "λ":
          estado = 0
        elif simbolo == "0":
          estado = 1
        else:
          break

      elif estado == 1:
        if simbolo == "x" or simbolo == "X":
          estado = 2
        else:
          break

      elif estado == 2:
        if simbolo >= "A" and simbolo <= "F" or simbolo >= "a" and simbolo <= "f":
          estado = 3
        elif simbolo >="0" and simbolo <="9":
          estado = 3
        else:
          break

      elif estado == 3:
        if simbolo >= "A" and simbolo <= "F" or simbolo >= "a" and simbolo <= "f":
          estado = 4
        elif simbolo >="0" and simbolo <="9":
          estado = 4
        else:
          break

      elif estado == 4:
        if simbolo >= "A" and simbolo <= "F" or simbolo >= "a" and simbolo <= "f":
          estado = 3
        elif simbolo >="0" and simbolo <="9":
          estado = 3
        else:
          break

      contador += 1
    #estados aceptables con cerradura de kleene
    if estado != 3 and estado !=4:
      return "La cadena: " +cadena+ " es INVALIDA\n"
    else:
      return ""

  def AlfabetoCeroUno(cadena):
    estado = 0
    contador = 0
    while contador < len(cadena):
      simbolo = str(cadena[contador])
      #if anidados
      if estado == 0:
        if simbolo == "0":
          estado = 1
        elif simbolo == "1":
          estado = 3
        else:
          break

      elif estado == 1:
        if simbolo == "0":
          estado = 2
        elif simbolo == "1":
          estado = 3
        else:
          break

      elif estado == 2:
        if simbolo == "0" or simbolo == "1":
          estado = 2
        else:
          break

      elif estado == 3:
        if simbolo == "0" or simbolo == "1":
          estado = 3
        else:
          break

      contador += 1
    #estados aceptables
    if estado != 1 and estado !=3:
      return "La cadena: " +cadena+ " es INVALIDA\n"
    else:
      return ""

  def AlfabetoABC(cadena):
    estado = 0
    contador = 0
    while contador < len(cadena):
      simbolo = str(cadena[contador])
      #if anidados
      if estado == 0:
        if simbolo == "a":
          estado = 1
        elif simbolo == "b" and simbolo == "c":
          estado = 5
        else:
          break

      elif estado == 1:
        if simbolo == "c":
          estado = 2
        elif simbolo == "a" and simbolo == "b":
          estado = 5
        else:
          break

      elif estado == 2:
        if simbolo == "a":
          estado = 3
        elif simbolo == "b" and simbolo == "c":
          estado = 2
        else:
          break

      elif estado == 3:
        if simbolo == "a":
          estado = 3
        elif simbolo == "b":
          estado = 4
        elif simbolo == "c":
          estado = 2
        else:
          break

      elif estado == 4:
        if simbolo == "a":
           estado = 3
        elif simbolo == "b" and simbolo == "c":
          estado = 2
        else:
          break

      elif estado == 5:
        if simbolo == "a" and simbolo == "b" and simbolo == "c":
          estado = 5
        else:
          break

      contador += 1
    #estado aceptable con cerradura de kleene
    if estado != 4:
      return "La cadena: " +cadena+ " es INVALIDA\n"
    else:
      return ""

  def DecimalNatural(cadena):
    estado = 0
    contador = 0
    while contador < len(cadena):
      simbolo = str(cadena[contador])
      #if anidados
      if estado == 0:
        if simbolo == "λ":
            estado = 0
        elif simbolo == "0":
            estado = 1
        elif simbolo.isdigit():
            estado = 2
        elif simbolo == ".":
            estado = 3
        else:
            break

      elif estado == 1:
        if simbolo == ".":
            estado = 3
        else:
            break

      elif estado == 2:
        if simbolo.isdigit():
            estado = 2
        elif simbolo == ".":
            estado = 3
        else:
            break

      elif estado == 3:
        if simbolo.isdigit():
            estado = 4
        else:
            break

      elif estado == 4:
        break

      contador += 1
    #estados aceptables (estado 2 con cerradura de kleene)
    if estado != 2 and  estado !=4:
      return "La cadena: " +cadena+ " es INVALIDA\n"
    else:
      return ""


#Clases para leer los automatas
def leerAutomata1():
  a=cajaCadena.get(1.0, "end-1c")
  b=str(a)
  c=b.split("\n")
  contador=0
  while contador <len(c):
    Respuesta = Automatas.identificador(c[contador])
    cajaError.insert(tk.INSERT, Respuesta)
    contador += 1

def leerAutomata2():
  a=cajaCadena.get(1.0, "end-1c")
  b=str(a)
  c=b.split("\n")
  contador=0
  while contador <len(c):
    Respuesta = Automatas.numeroReal(c[contador])
    cajaError.insert(tk.INSERT, Respuesta)
    contador += 1

def leerAutomata3():
  a=cajaCadena.get(1.0, "end-1c")
  b=str(a)
  c=b.split("\n")
  contador=0
  while contador <len(c):
    Respuesta = Automatas.NumeroHexadecimal(c[contador])
    cajaError.insert(tk.INSERT, Respuesta)
    contador += 1

def leerAutomata4():
  a=cajaCadena.get(1.0, "end-1c")
  b=str(a)
  c=b.split("\n")
  contador=0
  while contador <len(c):
    Respuesta = Automatas.AlfabetoCeroUno(c[contador])
    cajaError.insert(tk.INSERT, Respuesta)
    contador += 1

def leerAutomata5():
  a=cajaCadena.get(1.0, "end-1c")
  b=str(a)
  c=b.split("\n")
  contador=0
  while contador <len(c):
    Respuesta = Automatas.AlfabetoABC(c[contador])
    cajaError.insert(tk.INSERT, Respuesta)
    contador += 1

def leerAutomata6():
  a=cajaCadena.get(1.0, "end-1c")
  b=str(a)
  c=b.split("\n")
  contador=0
  while contador <len(c):
    Respuesta = Automatas.DecimalNatural(c[contador])
    cajaError.insert(tk.INSERT, Respuesta)
    contador += 1


#clase de limpiar y salir del menu
def limpiarPantalla():
  cajaError.delete("1.0", "end")
  cajaCadena.delete("1.0", "end")

def salir():
  ventana.destroy()

ventana=tk.Tk()
ventana.title("Proyecto Automatas y Lenguajes Formales")
ventana.geometry('850x600')
ventana.configure(background="aliceblue")

#menu desplegable
menubarra = tk.Menu(ventana)
columna = tk.Menu(menubarra, tearoff=0)
columna.add_command(label="Automatas")
columna.entryconfig(1, state="disabled")
columna.add_command(label="Identificador", command=leerAutomata1)
columna.add_command(label="Número real", command=leerAutomata2)
columna.add_command(label="Número Hexadecimal", command=leerAutomata3)
columna.add_command(label="Alfabeto 01", command=leerAutomata4)
columna.add_command(label="Alfabeto ABC", command=leerAutomata5)
columna.add_command(label="Decimal/Natural", command=leerAutomata6)
columna.add_separator()
columna.add_command(label="Salir", command=salir)
menubarra.add_cascade(label="Opciones", menu=columna)
ventana.config(menu = menubarra)

#caja de cadena
cajaCadena = tkinter.Text(ventana)
cajaCadena.grid(row=0, column=0, padx=5, pady=5)
desplasar1 = tkinter.Scrollbar(ventana, command=cajaCadena.yview)
desplasar1.grid(row=0,column=1, padx=5, pady=5, sticky="nsew")

#caja de error
cajaError = tkinter.Text(ventana, width=80, height=10)
cajaError.grid(row=1, column=0, padx=5, pady=5)
cajaError.config(foreground="red")
desplasar2 = tkinter.Scrollbar(ventana, command=cajaError.yview)
desplasar2.grid(row=1,column=1, padx=5, pady=5, sticky="nsew")

#boton para limpiar
botonLimpiar = tkinter.Button(ventana, text = "Limpiar\nPantalla", width=10, height=8, command=limpiarPantalla)
botonLimpiar.grid(row=0, column=3, padx=5, pady=5)
botonLimpiar.configure(background='skyblue')

ventana.mainloop()