import threading
import time

class Contador():
    def __init__(self, conta = 0):
        self.locket = threading.Lock()
        self.conta_send = conta
        

    def incrementar(self):
       
        self.locket.acquire()
        try:
            self.conta_send += 1
            print(self.conta_send)
           
        finally:
            self.locket.release()
    
def func_conta(x):
    for y in range(4):
        time.sleep(2)
        x.incrementar()
        

if __name__ == "__main__":
    contador = Contador()
    for y in range(4):
        tsart = threading.Thread(target=func_conta, args=(contador,))
        tsart.start()
