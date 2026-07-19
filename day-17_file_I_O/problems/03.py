with open ("practice.txt", "r")as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("not found")