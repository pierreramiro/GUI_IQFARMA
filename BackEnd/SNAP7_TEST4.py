import time
import snap7

#CARACTERÍSTICAS HARDWARE Y SOFTWARE DEL PLC
IP = '192.168.0.1'
RACK = 0
SLOT = 1

DB_NUMBER = 2
START_ADDRESS = 0
SIZE = 259

value = 1

#CONEXIÓN
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

#LECTURA DEL BLOQUE DE DATOS DEL PLC
db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

#LECTURA DEL PESO
peso = db[514:515].decode('UTF-8').strip('\x00')
print(f'{peso}')

#ESCRITURA DEL BLOQUE DE DATOS DEL PLC
#ESCRITURA DE UN BOOL
def writeBool(db_number, start_offset, bit_offset, value): 
    reading = plc.db_read(db_number, start_offset, 1)    
    snap7.util.set_bool(reading, 0, bit_offset, value)   
    plc.db_write(db_number, start_offset, reading)       
    return None

writeBool(DB_NUMBER, 258, 0, value)