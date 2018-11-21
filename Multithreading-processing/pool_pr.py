import multiprocessing


def f(n):
    return n*n


if __name__ == "__main__":
    array = [1,2,3,4,5]
    # process = n
    p = multiprocessing.Pool()
    # divide il lavoro tra i core
    result = p.map(f, array)
    print(result)