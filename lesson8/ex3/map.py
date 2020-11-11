def nemap(func,arr):
    _arr=arr
    _i=0
    while True:
        try:
            yield func(arr[_i])
            _i+=1
        except IndexError:
            break
def function(i):
    return(i**2)

arr=[1,2,3,4,5]
for i in nemap(function,arr):
    print(i)
