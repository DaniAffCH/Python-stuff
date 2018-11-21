import multiprocessing


def square(arr, queue):
    for n in arr:
        queue.put(n**2)


arr = [201, 536, 164, 903, 572]
queue = multiprocessing.Queue()
process = multiprocessing.Process(target=square, args=(arr, queue))
process.start()
process.join()
while queue.empty() is False:
    print(queue.get())
#queue module for threading 