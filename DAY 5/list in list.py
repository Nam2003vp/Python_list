friend = [["Bob", 23],["Jen", 34], ["How", 27]]
print(friend[0][0])

#copy list
lst1 = [1, 3, 2]
lst2 = lst1


#is: kiem tra vi tri bo nho cua list
# //: so sanh gia tri bo nho
print(lst1 == lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))
#id: hien thi vi tri bo nho

#listing slicing: lay ra mot phan cua list

a = [1, 3, 10, 100, 45]

new_list = a[0:2:1] # a[start:stop:step]
print(new_list is a)
new_list = a[1:] #in ra list tu vi tri 1 den het
new_list = a[1:-1] # in ra tu vi tri 1 den het
new_list = a[:] #in ra toan bo list
print(new_list)

