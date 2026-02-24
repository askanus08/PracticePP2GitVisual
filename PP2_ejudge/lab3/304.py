class StringHandler:
    def __init__(self):
        self.s = ""
    def getstring(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
obj = StringHandler()
obj.getstring()
obj.printString()