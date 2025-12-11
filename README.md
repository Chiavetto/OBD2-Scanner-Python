OBD2 Scanner en Python

Aplicación desarrollada en Python que se conecta a un escáner ELM327 OBD2 mediante un puerto COM para obtener datos en tiempo real del vehículo.  
Permite leer y borrar códigos de error (DTC) y visualizar valores de sensores a través de una interfaz gráfica creada con Tkinter.

Características principales

- Detección automática del dispositivo ELM327  
- Conexión mediante comunicación serie (PySerial)  
- Lectura de códigos de error (DTC)  
- Borrado de códigos almacenados en la ECU  
- Visualización en tiempo real de algunos sensores (RPM, velocidad, etc.)  
- Interfaz gráfica simple construida con Tkinter  
- Arquitectura modular con lógica separada por componentes

 Tecnologías utilizadas

- Python 3  
- Tkinter (interfaz gráfica)  
- PySerial (comunicación serial)  
- Hardware: ELM327 OBD2 conectado por puerto COM (USB o Bluetooth)



Estructura del proyecto

```text
src/
│  gui.py               → Interfaz gráfica principal
│  main.py              → Punto de entrada del programa
│  obd_connection.py    → Conexión y comandos al ELM327
│  dtc_screen.py        → Pantalla de lectura/borrado de códigos de falla
│  sensors_screen.py    → Pantalla de lectura de sensores en tiempo real
requirements.txt
README.md

Instalación
-----------

1. Clonar el repositorio: git clone https://github.com/Chiavetto/OBD2-Scanner-Python.git
cd OBD2-Scanner-Python


2. Instalar dependencias: pip install -r requirements.txt


3. Conectar el dispositivo ELM327 al puerto COM correspondiente (por ejemplo, COM3 o COM4).

---

Ejecución
---------

Para iniciar la aplicación:
python src/main.py



Esto abrirá la interfaz gráfica del escáner OBD2.  
Desde allí podrás:

- Buscar el dispositivo ELM327  
- Leer códigos de falla  
- Borrar códigos almacenados  
- Ver sensores en tiempo real

