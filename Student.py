class Student:

    school = "DPS"

    def __init__(self, name, cls):
        print("Constructor called : {}()".format(__name__))
        self.name=name
        self.cls=cls

    def getName(self):
        return self.name

    def getCls(self):
        return self.cls

    def setName(self,name):
        self.name=name

    def setCls(self,cls):
        self.cls=cls

    @classmethod
    def setSchoolName(cls,name):
        cls.school=name

    def sum(self,a=0,b=0,c=0):
        return a+b+c

