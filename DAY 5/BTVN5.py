friends = ["Jen", "Jack", "Kenny", "Jully", "Bob", "Henry", "Anne"]
#a.
four_first_f = friends[0:4]
print(four_first_f)
#b.
four_last_f = friends[3:]
print(four_last_f)

#c.
reverse = friends[::-1]
print(reverse)

#d.
first_to_over = friends[1:]
print(first_to_over)

#e.
new_friends = friends.copy()
print(new_friends)

#f.
hai_den_cuoi = friends[1:-1]
print(hai_den_cuoi)

#2.
#a.
students = [["SV001","Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
first_id_s1 = students[0][0]
first_name_s1 = students[0][1]
first_age_s1 = students[0][2]
print(f"Thông tin của sinh viên thứ nhất: ID: {first_id_s1}, Name: {first_name_s1} - Age: {first_age_s1} " )

#b.
two_age_s2 = students[1][2]
print(f"Tuổi của sinh viên thứ hai là: {two_age_s2}")

#c.
new_students =students[1:]

print("Thong tin cua hai sinh vien cuôi cung: ", new_students)

#d.
third_id_s3 = students[2][0]
print(third_id_s3)

