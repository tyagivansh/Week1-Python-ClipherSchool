name = input("please enter your name : ")
# pranjal singh

# pranjal, len = 7-1 = 6
# name.count("p") , name.count(name[0]) = 1
# name.count("r") , name.count(name[1]) = 1
# name.count("a") , name.count(name[2]) = 2
# name.count("n") , name.count(name[3]) = 1
# name.count("j") , name.count(name[4]) = 1
# name.count("a") , name.count(name[5]) = 2
# name.count("l") , name.count(name[6]) = 1

# output
# p : 1 
# r : 1
# a : 2
# n : 1
# j : 1
# a : 2
# l : 1
temp_var = ""
i = 0
while i<len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1