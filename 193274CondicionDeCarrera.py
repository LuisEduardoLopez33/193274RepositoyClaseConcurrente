import threading 
import time
ganancia = 0
costo = 70
  
def cobro(): 
    global costo
    global ganancia
    ganancia += costo
  

def princpal(lock): 
    global ganancia
    lock.acquire() 
    cobro() 
    print( ganancia) 
    lock.release() 
  

def main(): 
   
    for y in range(5):
        lock = threading.Lock() 
        subproceso = threading.Thread(target=princpal, args=(lock,)) 
        subproceso.start() 
        subproceso.join() 
    time.sleep(2)
   
  
if __name__ == "__main__": 
    for i in range(2): 
        print('trabajador:')
        main() 
    