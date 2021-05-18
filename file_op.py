with open("C:\\Users\\PycharmProjects\\PyWorld\\test.txt.txt",mode='r') as f:
    print(f.read())

with open("C:\\Users\\PycharmProjects\\PyWorld\\test.txt.txt",mode='a') as f:
    f.write("\nTHIS IS THE APPENDED TEXT")

with open("C:\\Users\\PycharmProjects\\PyWorld\\test.txt.txt",mode='r') as f:
    print(f.read())

with open("C:\\Users\\PycharmProjects\\PyWorld\\test.txt.txt",mode='r+') as f:
    print(f.read())
    f.write("\nTHIS IS THE LINE ADDED FOR mode = r+")

with open("C:\\Users\\PycharmProjects\\PyWorld\\test.txt.txt",mode='w+') as f:
    f.write("\nTHIS IS THE LINE ADDED FOR mode = w+")
    print(f.read())
