import time
import threading


def square(arr):
    print("calcolo il quadrato...")
    for obj in arr:
        time.sleep(0.2)
        print(obj**2)


def cube(arr):
    print("calcolo il cubo...")
    for obj in arr:
        time.sleep(0.2)
        print(obj**3)


arr = [201, 536, 164, 903, 572]
t = time.time()
t1 = threading.Thread(target=square, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("L'esecuzione ha impiegato " + str(time.time()-t))