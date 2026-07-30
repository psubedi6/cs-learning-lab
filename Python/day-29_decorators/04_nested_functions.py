def outer():
    print("Outer function starts")

    def inner():
        print("Inner function starts")

    inner()
    
    print("Outer function ends")

outer()