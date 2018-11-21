import multiprocessing

def square(arr, result, v):
    for idx, n in enumerate(arr):
        result[idx] = n**2
    v.value = 3.14

arr = [201, 536, 164, 903, 572]
result = multiprocessing.Array("i", 5)
v = multiprocessing.Value("d", 0.0)
process = multiprocessing.Process(target=square, args=(arr, result, v))
process.start()
process.join()
print(result[:])
print(v.value)