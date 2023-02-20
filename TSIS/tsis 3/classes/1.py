class stroka():
    def __init__(self, stroka):
        self.a = stroka

    def getstring(self):
        print(self.a)

    def printString(self):
        b = self.a
        print(b.upper())
a = input()
slovo = stroka(a)
slovo.getstring()
slovo.printString()


        