class BaseClass:
    def __init__(self, arg1):
        self.arg1 = arg1

class ClassA(BaseClass):
    def __init__(self, arg1, arg2):
        super().__init__(arg1)
        self.arg2 = arg2

class ClassB(BaseClass):
    def __init__(self, arg1, arg3):
        super().__init__(arg1)
        self.arg3 = arg3

class ClassC(ClassA, ClassB):
    def __init__(self, arg1, arg2, arg3):
        ClassA.__init__(self, arg1, arg2)
        ClassB.__init__(self, arg1, arg3)
