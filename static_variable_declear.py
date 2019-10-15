print("""Static Variable Declear in Python:
        1. Directly inside of class.
        2. Constructor in By using ClassName.
        3. Instance method in By using self reference variable.
        4. Static Method in By using ClassName.
        5. Class method in By using ClassName or cls variable. \n\n """)
class Test:
    x=100
    def __init__(self):
        Test.y=200
    def m1(self):
        Test.z=300
    @staticmethod
    def m2():
        Test.a=400
    @classmethod
    def m3(cls):
         cls.c=500
         Test.l=600
Test.d=700
print(Test.__dict__)
ref_v=Test()
print(Test.__dict__)
ref_v.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)

