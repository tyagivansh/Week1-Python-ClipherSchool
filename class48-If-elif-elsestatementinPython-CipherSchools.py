# if elif else statement

# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = input("please input your age : ")
age = int(age)

if age==0 or age<0:
    print("you are underage to watch this movie")
elif 0<age<=3:
    print("Ticket price : Free")
elif 3<age<=10:
    print("Ticket price : 150")
elif 10<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")
