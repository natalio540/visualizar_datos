
import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv('climacordoba.csv',header=0)



def inicio():
    print("Promedio de temperatura y lluvias de la Ciudad de Cordoba")
    print("si desea conocer las temperatura media ingrese 1")
    print("si desea conocer las temperatura maxima ingrese 2")
    print("si desea conocer las temperatura minima ingrese 3")
    print("si desea conocer el total de lluvias por año ingrese 4")
    opcion=int(input())
    if opcion==1:
        return temperaturas_medias()
    elif opcion==2:
        return temperaturas_maximas() 
    elif opcion==3:
        return temperaturas_minimas()
    elif opcion==4:
        return total_lluvias()

def temperaturas_medias():
    lista_ano=[]
    for x in datos['Año']:
        x=int(x)
        lista_ano.append(x)

    lista_tmedia=[]
    for x in datos['Tmedia']:
        x=float(x)
        lista_tmedia.append(x)
    
    plt.bar(lista_ano,lista_tmedia)
    plt.xlim(1973,2015)
    plt.ylim(0,30)
    plt.minorticks_on()
    plt.title("Temperatura Media de Córdoba")
    plt.xlabel("Años")
    plt.ylabel("Temperatura Media")
    plt.show()

    pregunta=input("Desea conocer otra informacion? ")
    if pregunta == "si" or pregunta == "SI":
        return inicio()
    else:
        print("Programa Finalizado")    
    

def temperaturas_maximas():

    lista_ano=[]
    for x in datos['Año']:
        x=int(x)
        lista_ano.append(x)
    
    lista_tmaxima=[]
    for x in datos['tmax']:
        x=float(x)
        lista_tmaxima.append(x)
    
    plt.bar(lista_ano,lista_tmaxima)
    plt.xlim(1973,2015)
    plt.ylim(0,40)
    plt.minorticks_on()
    plt.title("Promedio de Temperaturas Máximas de Córdoba")
    plt.xlabel("Años")
    plt.ylabel("Temperatura Máxima")
    plt.show()

    pregunta=input("Desea conocer otra informacion? ")
    if pregunta == "si" or pregunta == "SI":
        return inicio()
    else:
        print("Programa Finalizado")  


def temperaturas_minimas():
    lista_ano=[]
    for x in datos['Año']:
        x=int(x)
        lista_ano.append(x)
    
    lista_tminima=[]
    for x in datos['Tmin']:
        x=float(x)
        lista_tminima.append(x)
    
    plt.bar(lista_ano,lista_tminima)
    plt.xlim(1973,2015)
    plt.ylim(0,20)
    plt.minorticks_on()
    plt.title("Promedio de Temperaturas Minimas de Córdoba")
    plt.xlabel("Años")
    plt.ylabel("Temeraturas Mínimas")
    plt.show() 

    pregunta=input("Desea conocer otra informacion? ")
    if pregunta == "si" or pregunta == "SI":
        return inicio()
    else:
        print("Programa Finalizado")  


def total_lluvias():
    lista_ano=[]
    for x in datos['Año']:
        x=int(x)
        lista_ano.append(x)
    
    lista_tlluvias=[]
    for x in datos['lluvias']:
        x=float(x)
        lista_tlluvias.append(x)
    
    plt.bar(lista_ano,lista_tlluvias)
    plt.xlim(1973,2015)
    plt.ylim(0,1000)
    plt.minorticks_on()
    plt.title("Promedio de Lluvias por Año")
    plt.xlabel("Años")
    plt.ylabel("Lluvias")
    plt.show()

    pregunta=input("Desea conocer otra informacion? ")
    if pregunta == "si" or pregunta == "SI":
        return inicio()
    else:
        print("Programa Finalizado")  

inicio()

