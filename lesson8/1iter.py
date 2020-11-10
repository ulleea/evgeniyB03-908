def print_map(function, iterable):
    it=iter(iterable)
    while True:
        try:
            i=next(it)
        except StopIteration:
            break
        print(function(i))
def function(i):
    return i*2
print_map(function,[1,2,3,4,5])
