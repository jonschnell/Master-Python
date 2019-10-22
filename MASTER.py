#master python referance

#printing strings
print('hello')

#string variable
a = "string"
#print variable
print(a)
#removes variable a
del(a)

#user I/O
a = float(input("enter a number\n"))
print(a)

#define boolean
booleana = (6 == a)
print(booleana)
#if else statment
if booleana == True:
    print('truth is always the answer')
else:
    print('you liar')
    
i = 1
#while statment
while i <= 5:
    print(i)
    i += 1


g = 0
#list delectration
lista = ["item 1", "item 2"]
#append a list
lista.append("item 4")
lista.insert(2, "item 3")
#while length of a list
while g <= len(lista)-1:
    print(lista[g])
    g += 1

#searching the list and printing that index
in1 = input("what whould you like to search for?\n")
print (lista.index(in1))
print (lista[lista.index(in1)])
