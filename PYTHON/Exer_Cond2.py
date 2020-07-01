#Developer: Joan C. Ayala
#Basic calc: This calc operates two numbers.

print("First number: ")
n1 = int(input())

n2 = int(input("Second number: "))

print("OPTIONS MENU")
print(" [+] Add \n [-] Subs \n [*] Mult \n [/] Div \n")
op = input("Please, press an option [+,-,*,/]: ")

if op == "+" :
    print("The add is: ", n1 + n2)
elif op == "-" :
    print("The sub is: ", n1 - n2)
elif op == "*" :
    print("The mult is: ", n1 * n2)
elif op == "/" :
    print("The div is: ", n1 / n2)
else :
    print("INVALID OPTION")
