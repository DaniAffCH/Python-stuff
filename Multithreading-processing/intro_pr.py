import multiprocessing
result = []

def square(arr):
    global result
    for n in arr:
        result.append(n**2)
    print("Dentro il processo: "+str(result))


arr = [201, 536, 164, 903, 572]
process = multiprocessing.Process(target=square, args=(arr,))
process.start()
process.join()
print("Fuori il processo: "+str(result))