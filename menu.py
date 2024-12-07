from opciones.opcion1 import function_opcion1
from opciones.opcion2 import function_opcion2
from opciones.opcion3 import function_opcion3

def my_menu():
    activation_code = True
    print("_" * 110)
    print(" "*30, "Bienvenido al menú principal")
    print("\n")
    print("Seleccione una de las siguientes opciones, ingrese el número deseado y presione la tecla \"enter\" a continuación")
    print("_" * 110)
    while activation_code:
         
        option = input("""
              1: Abrir opción 1
              2: Abrir opción 2
              3: Abrir opción 3
              4: Cerrar
              Seleccion ->
                """)
        match option:
            case "1":
                function_opcion1()
            case "2":
                function_opcion2()
            case "3":
                function_opcion3()
            case "4":
                print("Seleccionaste cerrar. ¡ADIOS!")
                activation_code = False
                break

if __name__ == "__main__":
    my_menu()
