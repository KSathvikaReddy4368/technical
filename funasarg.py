def f1():
    print("hi")
def f2():
    print("bye")
def f3(a,b):
    a()
    b()
f1()
f2()
f3(f1,f2)
