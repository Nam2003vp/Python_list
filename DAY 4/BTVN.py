#1.
Movies = ["Attack on titan", "Songoku", "Naruto", "Hope", "Conan", "Doraemon", "gió"]

#2.
Add_Movies = (input("Nhap vao mot bo phim: "))
print(Add_Movies)

#3.
Movies.append(Add_Movies)
print(Movies)

#4.
amount = len(Movies)
print(Movies[0])
print(Movies[amount//22])
print(Movies[3])

#5.
print(amount)

#6.
del Movies[0]
del Movies[-1]
print(Movies)
#7.
last = Movies.pop()
print(last)
print(Movies)

#8.
Add_begin = input("Moi ban nhap vao 1 bo phim de chen: ")
Movies.insert(0,Add_begin)
print(Movies)

#9.
count = Movies.count("One Piece")
print(count)

#10.
index_of_gio = Movies.index("gió")
print(index_of_gio)

#11.
Movies.extend(["One piece", "Supermen", "Wukong"])
print(Movies)

#12.
Movies.clear()
print(Movies)