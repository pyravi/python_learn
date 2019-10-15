#!/usr/bin/python3.6
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)
# for i in range(26):
#     print(chr(65+i),end=' ')
# def myfun():
#     #ndnlnfllfkf
#     '''dddddddd'''
#     pass
#print(myfun.__doc__)
# squares = [x**2 for x in range(10)]
# print(squares)
#
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

s='python'
s1='python3 is simple'
# for x in s[::-1]:  #------>nothyp
#     print(x,end='')
# for i in s1[::-1]: #--------->elpmis si 3nohtyp
#     print(i, end='')
# l=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(l)
#
# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12],
#           ]
# r=[[row[j] for row in matrix] for j in range(4)]
# # transpose rows and columns:
# print(r)
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# d={'gallahad': 'the pure', 'robin': 'the brave'}
# #printing with index
# for i, v in enumerate(d):
#     print(i,v)
# #printing with key & value using items()
# for i, v in d.items():
#     print('{} ---> {}'.format(i,v))

#Important function()
# for i in reversed(range(1,20,2)):
#     print(i,end=' ')
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)
