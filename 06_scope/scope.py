username = "golu"

def test():
    username ="Singh"
    print(username)

print(username)    
test()



x = 78

# def fun(y):
#     z = x + y
#     return z 

# print(fun(6))



# def fun2():
#     global x
#     x = 14

# fun2()
# print(x)   
 



# def fun3():
#     a = 3
#     print(a) 
#     print(b)
#     def demo():
#         b = 4
#         print(a)
#         print(b)
#     demo()        
      
# fun3()


# closer / bagpack / factory function
# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# myResult = f1()
# myResult()    


def chaicode(num):
    def actual(x):
        return x ** num
    return actual

f = chaicode(2)
g = chaicode(3)

print(f(5))
print(g(5))