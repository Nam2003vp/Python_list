friends = ["Jack", "John", "kenny", "Henry" ]

friends[0] = "Anna"
print(friends)

friends.insert(1, "Leona")
print(friends)

last = friends.pop() #Lay ra 1 phan tu va xoa khoi list
print(last)
print(friends)

friends.remove("Anna")
print(friends)

del friends[1]# xoa gia tri trong list o vi tri dc chon
print(friends)

friends.extend(["Jack"]) #them gia tri vao cuoi list
print(friends)

