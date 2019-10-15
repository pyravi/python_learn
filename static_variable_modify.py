print("""Static Variable Modify in Python:
        1. Constructor in modify By using ClassName.
        2. Instance method in modify By using ClassName.
        3. Static Method in modify By using ClassName.
        4. Class method in modify By using ClassName or cls variable.
        5. Outside class variable modify By using ClassName.
        \n\n """)
class Test:
    x=100
    def __init__(self):
        Test.x=500
        print(self.x)
    def m1(self):
        print(self.x)
        Test.x=600
    @staticmethod
    def m2():
        print(Test.x)
        Test.x=700
    @classmethod
    def m3(cls):
        print(cls.x)
        cls.x=800
        print(Test.x)

s=Test()
s.m1()
Test.x=900
Test.m2()
Test.m3()
print(s.x)
print(Test.x)
                                                                                                            
