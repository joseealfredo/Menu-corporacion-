# Proyecto Terminal Utilities

Este proyecto proporciona un conjunto de utilidades accesibles desde la terminal. Las opciones disponibles permiten realizar tareas como chatear entre terminales de Linux, eliminar metadatos de imágenes, y registrar números de teléfono con alias. La interfaz es simple y se maneja completamente desde la terminal.

## Funcionalidades

### 1. **Chatear entre terminales de Linux**
   - Utiliza `netcat` (nc) para crear una conexión entre dos terminales de Linux y permitir el intercambio de mensajes.
   - Requiere abrir dos terminales y configurar una conexión de red con los comandos:
     - En la primera terminal: `nc -l -p [puerto]`
     - En la segunda terminal: `nc [IP_del_otra_terminal] [puerto]`
   - Se pueden enviar mensajes entre los terminales conectados.

### 2. **Borrar metadatos de una imagen**
   - Elimina los metadatos EXIF de una imagen, garantizando que no se conserve información privada o innecesaria.
   - Se pide al usuario la ruta de la imagen original y una ruta de salida para la imagen sin metadatos.
   - Utiliza la librería `Pillow` para manejar la imagen y eliminar los metadatos.

### 3. **Registrar número de teléfono con alias**
   - Permite registrar números de teléfono bajo un alias (nombre o apodo) en una agenda telefónica simple.
   - El usuario puede agregar múltiples alias y sus números correspondientes.
   - Al finalizar, la agenda se actualiza y se guarda en el programa.

### 4. **Salir**
   - Sale del programa y termina la ejecución del script.

## Requisitos

- **Python 3**: El código está escrito en Python 3 y requiere de una instalación de este lenguaje.
- **Pillow**: Para trabajar con imágenes y eliminar metadatos EXIF. Se puede instalar usando:
  
  ```bash
  pip install Pillow
  ```

- **Netcat (nc)**: Para la funcionalidad de chat entre terminales, es necesario tener instalado `netcat`. En sistemas basados en Linux, generalmente ya está instalado. Si no lo está, puede instalarse con el siguiente comando:
  
  ```bash
  sudo apt install netcat
  ```

## Uso

1. **Ejecutar el programa**: Para iniciar el programa, simplemente ejecuta el archivo Python:
   ```bash
   python3 nombre_del_archivo.py
   ```
2. **Seleccionar una opción**: Una vez iniciado el programa, el menú te mostrará las opciones disponibles. Ingresa el número correspondiente para seleccionar una acción.

3. **Interactuar con las opciones**:
   - Si seleccionas la opción de **chatear entre terminales**, seguirás las instrucciones para configurar la conexión de red con `netcat`.
   - Si eliges **borrar metadatos de una imagen**, proporciona la ruta de la imagen y la ruta de salida donde deseas guardar la nueva imagen sin metadatos.
   - Si optas por **registrar un número de teléfono**, puedes ingresar alias y números hasta que decidas salir.

## Estructura del Código

- **clear_console()**: Limpia la terminal para mantener la interfaz limpia.
- **display_menu()**: Muestra el menú con las opciones disponibles.
- **chat_between_terminals()**: Inicia el proceso de chat entre dos terminales usando `netcat`.
- **remove_image_metadata()**: Elimina los metadatos EXIF de la imagen seleccionada por el usuario.
- **register_phone_number()**: Permite registrar números de teléfono con alias en una agenda simple.
- **main()**: Bucle principal del programa que maneja la navegación y ejecución de las funcionalidades.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o deseas agregar nuevas funcionalidades, por favor crea un **pull request**. Asegúrate de seguir las mejores prácticas de codificación y agregar pruebas unitarias si es necesario.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo `LICENSE`.
