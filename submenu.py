def my_submenu():
    activation_code = True
    print("_" * 110)
    print(" " * 30, "SUBMENÚ")
    while activation_code:
        option = input("""
              1. Volver al menú principal
              2. Cerrar Submenú
              Seleccion -> """)
        match option:
            case "1":
                print("Regresando al menú principal...")
                return  # Exit submenu and return control to the main menu
            case "2":
                print("Seleccionaste cerrar el submenú. ¡ADIOS!")
                activation_code = False
                break
