def displayNumbers(x):
    for i in range(0,x):
        print("Your are at iteration number {i}/{x}".format(i=i,x=x))


def main():
    print("hello from local")
    print('hello from remote')
    displayNumbers(8)
  
main()
