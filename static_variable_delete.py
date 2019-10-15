print("""Static Variable delete in Python:
        1. Constructor in delete By using ClassName.
        2. Instance method in delete By using ClassName.
        3. Static Method in delete By using ClassName.
        4. Class method in delete By using ClassName or cls variable.
        5. Outside class variable delete By using ClassName.
        \n """)

class Test:
    x=100
    def __init__(self):
        Test.y=500
        del Test.x
    def m1(self):
        Test.z=600
        del Test.y
    @staticmethod
    def m2():
        Test.b=700
        Test.c=800
	del Test.z
    @classmethod
    def m3(cls):
        cls.a=400
	del Test.c
        del cls.a
       

s=Test()
print(Test.__dict__)
s.m1()
print(Test.__dict__) 
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
