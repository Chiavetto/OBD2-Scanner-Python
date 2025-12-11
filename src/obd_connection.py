import serial
import time

puerto = None

def conectar_elm327():
    posibles_puertos = ["COM3", "COM4"]  # Podés agregar más si lo necesitás
    for p in posibles_puertos:
        try:
            ser = serial.Serial(p, 9600, timeout=1)
            time.sleep(2)
            ser.write(b'ATZ\r')
            time.sleep(1)
            respuesta = ser.read(100).decode('utf-8', errors='ignore')
            if "ELM" in respuesta:
                return ser
            ser.close()
        except:
            pass
    return None


def enviar_comando(comando):
    global puerto
    try:
        if puerto:
            puerto.write((comando + "\r").encode())
            time.sleep(1)
            return puerto.read(1024).decode('utf-8', errors='ignore')
        return "Puerto no conectado"
    except Exception as e:
        return f"Error: {str(e)}"
