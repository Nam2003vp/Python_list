#operators
# + - * / // ** % 
# print(1+2)
# print(1-2)
# print(3*2)
# print(3/2)#ctrl + Alt + N
# print(3//2)#ctrl + Alt + N
# print(5**2)
# print(5%3)

# Toan tu so sanh : >, < , >=, <= , ==, !=
# Ket qua tra ra la bool: True/False
# print(1 >2 )
# print(3.0 == 3)
# print('a' != 'a')

#Toan tu : and, or, not
# 1 > 2 and 2 > 3
# Ctrl + Shift + L : bôi đen những từ giống nhau

# print(True and True) # True
# print(True and False) # Flase
# print(False and False) # Flase

# print(False or True) #True
# print(bool(0)) #False
# print(bool(1))

# print(1 and 2)# Trả về giá trị phía sau nếu giá trị đầu tiên là đúng 
# print(0 and 2)
# print(0 or 2)# Trả về giá trị phía sau nếu giá trị thứ nhất False
# print(1 or 2)# Trả về giá trị đầu luôn do 1 là True

# print(not 1) # Trả về giá trị bool
# print(not 2)# Trả về giá trị bool

#bool(falsy) = False
# Khi truyền vào 1 hàm trống thì gía trị cũng là False
# Ví dụ: List[] ; set()
# print(bool(set()))
# Khi bool một chuỗi thì giá trị sẽ là False
# print(bool(''))
# x = 1
# y = 2
# print( x>y) # 1>2 ->> False

# Toán tử gán bằng: +=, -=, *=, /=, //=, %=, **=
# x = 5
# x = x+5 # x += 5
# x -=9 # x = x - 9
# x *= 12 # x = x*12
# print("x =",x)
 # /: float ; //: int

# age = 30
# # I am 30          
# print("I am " + str(age))
# # f-string
# print(f"I am {age}")

# print("I am {}".format(age))

s = "Hello World"
s = s.upper() # Hàm in hoa các chữ cái 
print (s)
s = s.capitalize() # Hàm in hoa chữ cái đầu tiên
s = s.title() # Hàm in hoa chữ cái đầu tiên của mỗi từ
print(s)

lst = s.split() # Ham chia các từ trong câu thành 1 danh sách

print (lst)

lower_case = s.lower() #in thường toàn bộ chuỗi
print(lower_case)

print ("Chào bạn nhénhé")

age=input ("Nhap gia tri tuoi cua ban: ")
print(age)

print(❤️😍😒)