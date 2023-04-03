def show(w):
    for i in w:
        yield i
f = open("File.txt", "w")

f.write("this is the code ")
f.close()
f = open("File.txt", "r")

for word in show(f):
    print(word) 