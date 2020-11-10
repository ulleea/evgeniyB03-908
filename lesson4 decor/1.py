import sys
import argparse
def fibonachi(n):
    if n==1 or n==2:
        return(1)
    else:
        n1=1
        n2=1
        n3=0
        for i in range(2,n):
            n3=n1+n2
            n2=n1
            n1=n3
        return n1
def create_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument('name',nargs='?',default='0')
    return parser
parser = create_parser()
namespace=parser.parse_args()
n=int(namespace.name)
n=fibonachi(n)
print(n)
