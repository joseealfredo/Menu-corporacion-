import os
import time
from PIL import Image
from PIL.ExifTags import TAGS

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_console()
    print("""
    __  _    __   _
   / __ \/   |  /  _/ | / /
  / /_/ / /| |  / //  |/ / 
 / _/ __ |_/ // /|  /  
//   //  |/_// |_/   

1. Chatear entre terminales de Linux
2. Borrar metadatos de una imagen
3. Registrar número de teléfono con alias
4. Salir
    """)

def chat_between_terminals():
    print("Chatear entre terminales requiere el uso de netcat (nc).\n")
    print("Para iniciar el chat, abre dos terminales. En una escribe:\n")
    print("    nc -l -p [puerto]\n")
    print("En la otra terminal escribe:\n")
    print("    nc [IP_del_otra_terminal] [puerto]\n")
    input("Presiona Enter para volver al menú principal...")

def remove_image_metadata():
    image_path = input("Introduce la ruta de la imagen: ")
    try:
        with Image.open(image_path) as img:
            data = list(img.getdata())
            img_without_metadata = Image.new(img.mode, img.size)
            img_without_metadata.putdata(data)
            output_path = input("Introduce la ruta para guardar la imagen sin metadatos: ")
            img_without_metadata.save(output_path)
            print(f"Metadatos eliminados y nueva imagen guardada en {output_path}.")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
    input("Presiona Enter para volver al menú principal...")

def register_phone_number():
    phonebook = {}
    while True:
        alias = input("Introduce un alias (o escribe 'salir' para volver al menú): ")
        if alias.lower() == 'salir':
            break
        number = input(f"Introduce el número de teléfono para {alias}: ")
        phonebook[alias] = number
        print(f"Alias y número registrados: {alias} -> {number}")
    print("Agenda telefónica actualizada.")
    input("Presiona Enter para volver al menú principal...")

def main():
    while True:
        display_menu()
        choice = input("Selecciona una opción: ")

        if choice == "1":
            chat_between_terminals()
        elif choice == "2":
            remove_image_metadata()
        elif choice == "3":
            register_phone_number()
        elif choice == "4":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, selecciona otra opción.")
            time.sleep(2)

if __name__ == "__main__":
    main()
