import time
import snap7
from datetime import datetime

IP_address = '192.168.0.1'
RACK = 0
SLOT = 2
#SERVER_PORT = 102

DB_NUMBER = 3
START_ADDRESS = 0
BYTES_SIZE = 259

PLC_client = 0;


def setUp(client):
    client = snap7.client.Client()
    client.connect(IP_address, RACK, SLOT)

# Checking the connection
def checkConnection(client):
    client.get_connected() 

# Checking the state
def checkState(client):
    state = client.get_cpu_state()
    print(f'Current state is:{state}')
    
# Reading the DB 
def readDb(client,db_num,start_addr,byte_to_rd):
    rd_var = client.db_read(db_num, start_addr, byte_to_rd)
    return rd_var

def byte_to_str(rd_var,init_range,final_range):
    str_var = rd_var[init_range:final_range].decode('UTF-8').strip('\x00')
    return str_var

def byte_to_int(rd_var,init_range,final_range):
    int_var = int.from_bytes(rd_var[init_range:final_range], byteorder='big')
    return int_var

def byte_to_bool(rd_var):
    bool_var = bool(buffer[258])
    return bool_var

if __name__ == "__main__":
    setUp(PLC_client)
    checkConnection(PLC_client)
    checkState(PLC_client)   

    while(1):
        try: 
            buffer = readDb(PLC_client,DB_NUMBER,START_ADDRESS,BYTES_SIZE)
            product_name = byte_to_str(buffer,2,256)
            product_value = byte_to_int(buffer,256,258)
            product_status = byte_to_bool(buffer[258])
            dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            #Printing data logging (Example)
            print(f'DATE:\tPRODUCT NAME:\tPRODUCT VALUE:\tPRODUCT_STATUS\n')
            print(f'{dt_string}\t{product_name}\t{product_value}\t{product_status}\n')
        except ConnectionError as e:
            print(str(e))
        time.sleep(15)
    
