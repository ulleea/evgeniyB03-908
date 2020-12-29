import multiprocessing
import time
def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [multiprocessing.Process(target=worker()) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)
# для работы функции необходимо вызвать ее и, если нет аргументов, оставить скобочки пустыми