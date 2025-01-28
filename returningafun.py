def fun():
    print("hello")
    def y():
        print("bye")
    return y
i=fun()
i()
