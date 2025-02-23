# Hoc ve list
numbers = [1, 2, 3.5, 4]
print(type(numbers)) # type list
print(numbers) 
print(numbers[1]) # 2
print (numbers[-1]) #4

numbers.append(100) #thêm giá trị 100 vào cuối danh sách
print(numbers)

numbers.remove(1) #xóa gía trị 1 đầu tiên tìm thấy trong list
print(numbers)

numbers.extend([2.5, 1000, 100, 125, 100, 100]) #them chuoi vao sau chuoi ban dau
print(numbers)

amount = numbers.count(10000) #dem so gia tri trong chuoi
print(amount)

# numbers.clear() #xoa het phan tu trong list
# print(numbers)

amount = len(numbers)
print(amount)

#insert : chem gia tri vao vi tri bat ki trong list
numbers.insert(1,2000)

numbers.remove(100)
print(numbers)

#index: tra ve vi tri cua gia tri nam trong list
index_of_3p5 = numbers.index(3.5)
print(index_of_3p5)

#reserve #lat nguoc list 
numbers.reverse()
print(numbers)

#ham sắp xếp những con số theo giá trị tăng hoặc giamr dần
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
