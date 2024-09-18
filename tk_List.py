a=list('abcde')# danh sach (cho phep  them vao  danh sach +  cat lat trong danh sach )
print( a)                #['a', 'b', 'c', 'd', 'e']
a[-1]=[0,5,9]
print( a)                #['a', 'b', 'c', 'd', [0, 5, 9]]
a[1:3]=[1,2,3]
print( a)                #['a', 1, 2, 3, 'd', [0, 5, 9]]  
print(a[2::+1])          #[2, 1, 'a']
a[2:-1]=[0]
print(a)                 #['a', 1, 0, [0, 5, 9]]
del a[2::-1] # delete phan tu 
print( a)                #[[0, 5, 9]]

   
# ////////// cac ham trong python
# Tạo một list
my_list = [1, 3, 5, 2, 4]

# append: Thêm phần tử vào cuối list
my_list.append(6)
print(my_list)  # Output: [1, 3, 5, 2, 4, 6]

# insert: Thêm phần tử vào vị trí chỉ định
my_list.insert(2, 'hello')
print(my_list)  # Output: [1, 3, 'hello', 5, 2, 4, 6]

# remove: Xóa phần tử đầu tiên có giá trị bằng giá trị cho trước
my_list.remove(3)
print(my_list)  # Output: [1, 'hello', 5, 2, 4, 6]

# pop: Xóa phần tử tại vị trí chỉ định và trả về giá trị đó
removed_item = my_list.pop(1)
print(removed_item)  # Output: 'hello'
print(my_list)  # Output: [1, 5, 2, 4, 6]

# sort: Sắp xếp list theo thứ tự tăng dần
my_list.sort()
print(my_list)  # Output: [1, 2, 4, 5, 6]

# reverse: Đảo ngược thứ tự các phần tử trong list
my_list.reverse()
print(my_list)  # Output: [6, 5, 4, 2, 1]

# clear: Xóa tất cả các phần tử trong list
my_list.clear()
print(my_list)  # Output: []

