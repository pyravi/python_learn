print("""Static Variable Access in Python:
        1. Constructor in access By using ClassName or Self reference variable.
        2. Instance method in access By using ClassName or Self reference variable.
        3. Static Method in access By using ClassName.
        4. Class method in By using ClassName or cls variable.
        5. Outside class variable access By using ClassName or Self reference variable
        \n\n """)
class Test:
    x=100
    def __init__(self):
        print(self.x)
        print(Test.x)
        Test.y=200
    def m1(self):
        Test.z=300
        print(self.y)
        print(Test.y)
    @staticmethod
    def m2():
        print(Test.z)
    @classmethod
    def m3(cls):
        cls.l=5000
        print(cls.x)
        print(Test.x)
         
s=Test()
s.m1()
Test.m2()
Test.m3()
print(s.l)
