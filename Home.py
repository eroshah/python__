# a = int(input("Born year: "))
# print("You will 100 from",2100-22-a, "years"  )


# a = int(input("Add temperature: "))
# b = input("C or F")
#
# if  b =="C" or b== "c":
#     print(a*1.8+32,"F")
#
# elif b == "F"  or b == "f":
#     print((a-32)*1.8,"C")



# keys = ["Ten", "Twenty","Thirty"]
# values = [10,20,30]
#
# dict = dict(zip(keys,values))
# print(dict)
#
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = {**dict1 , **dict2}
# print(dict3)

                   #TNAYIN

# def a(name,age):
#     print(name,age)
#
# a("astghik",15)


# def a(*args):
#     b = args
#     for i in b:
#         print(i)
# a(20,40,80,-25)


# def calculation(a,b):
#     plus = a+b
#     minus = a-b
#     print(plus,",",minus)
# calculation(40,10)


# def show_employee(a,b=9000):
#     print("Name: ",  a,  "Salary: ",  b)
# show_employee("Ben", 7500)
# show_employee("Jessica")


def function(a,b):

    def function1(a,b):
        return a * b
    res = function1(a,b)
    return res + 5
c = function(4,7)
print(c)
