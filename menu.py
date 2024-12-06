from opciones.opcion1 import function_opcion1
from opciones.opcion2 import function_opcion2
from opciones.opcion3 import function_opcion3

def my_menu():
    activation_code = True
    print("_"* 110)
    print (" "*30 , "Bienvedido al menu principal")
    print("\n")
    print ("Selecione una de las siguientes opciones, ingrese el número deseado y presione la techa \"enter\" a continuación")
    print("_" * 110)
    while activation_code:
        option = input("1. Abrir opcion 1 \n2. Abrir opción 2 \n3. abrir opcion 3 \n4. Cerrar \nSeleccion -> ")
        match option:
            case "1":
                print("selecciono opcion 1")
                print(function_opcion1())
            case "2":
                print("Selecciono opcion2")
                print(function_opcion2())
            case "3":
                print("Selecciono la opcion 3")
                print(function_opcion3())
            case "4":
                print("Seleccionaste cerrar ADIOS")
                activation_code=False
                break
my_menu()