////////////////////////////////////////////// Thư viện ///////////////////

          - import math : thư viện liên quan đến toán và sử dụng như lấy giá trị pi....
          - encodeing='utf-8' : Sử dụng việt mã hóa để utf-8 để đọc được file tiếng việt.
          - with {Hàm}() as {file,seesion,conn...} : Nó cho phép bạn  sử dụng để tự động hóa quản lý tài nguyên.

////////////////////////////////////////////// Các câu gợi ý /////////////////// # : Conment 1 dòng
'''{Conment}''' : Conment nhiều dòng
\ : tiếp tục nhiều dòng khi hàm quá dài có thể dùng \ để xuống dòng rồi viết tiếp
\n : xuống dòng
\t tab trắng

           - Trong python cho phép bạn dùng chỉ số âm ( arr[-1])


////////////////////////////////////////////// Các Hàm quan trọng /////////////////// - isinstance(<item>,<kiểu>) : cho phép bạn kiểm tra có phải số cần kiểu không.

```python
               # Kiểm tra xem một số có phải là số nguyên không
               x = 10
               print(isinstance(x, int))  # Output: True
```

          - enumerate(): Lấy chỉ số và và gía trị trọng For

          - strip() :  Loại bỏ khoảng trắng và xuống dòng
          - rstrip() : xóa một phần tử nào đó trong dòng file
          - index() : Trả về index của một array,ob,list...
          -sum()
```python
                    row_count = sum(1 for _ in reader) # doc file trong dem so dong ,  cung co the tinh tong
```
          -sreach() :  Tìm kiếm chuỗi 



https://gemini.google.com/app/055b30eb7b1b185e?hl=vi













          - split() : Tách các chuỗi thành một chuỗi nhỏ
          - re.findallP(<CanTim> , <Sring>) : Tìm số lần xuất hiện trong một chuỗi

          - re.finditer(<Cần_tìm> , <String> ) : Tìm kiếm lọc ra các số.....


```python
               #  finditer()
                    import re 
                    a='2004-09-20'
                    c=  re.finditer('-',a)
                    for num in  c :
                         print(num.start())

```


          -  float('inf')  : Số vô cùng  lớn ===> Dùng trong không cần đặt một giá trị nhất định
          -  float('-inf') : Số vô cùng bé   ===> Dùng trong không cần đặt một giá trị nhất định



////////////////////////////////////////////// Toán học /////////////////// + phép cộng - phép trừ \* phép nhân
\*\* phép chia lũy thừa
/ phéo chia lấy so thap phan
// phéo chia nguyên
% phép chia lấy phần dư

------------------------------------------Toán tử --------------------------------------
and : sử dụng kết hợp điều kiện cả hai cùng đúng thì đúng.
or : Sử dụng kết hợp điều kiện một trong hai đúng là đc
not : là điều kiện phủ định (true --> False | False --> True)

---

     int() : kiểu số nguyên
     float(): kiểu số thực

------------------------------------------Hàm liên quan đến Toán -------------------------

     - pow({Số1},{Số2}) : Cho phép bạn tính số mũ
     - round({số_thập_phân}, {lấy_sau_số_phẩy}) :  cho  phép bạn lấy số thập phân
     - :.2f : Làm tròn sau hai chữ số thập phân(* Lưu ý:  2f chỉ được dùng trực tiếp khi in ra)
     - format() :Định dạng ở 2 số thập phân
               <!-- Vd  format
                         txt = "For only {price:.2f} dollars!"
                         print(txt.format(price = 49))
               -->

```python
          # //////////  pow
               print(pow(2,3))
               # KQ: 8
          # //////////  round
               print(round(23.4756775465,2))
               # KQ: 23.47
          # //////////  :.2f
               num=34345.576576
               print(f'{num:.2f}')
               # KQ: 34345.58
```

////////////////////////////////////////////// Vòng lặp ///////////////////

     - for x  in  range({Start},{Stop},{step}) : Vòng lặp
     - for x in  y : lặp  trong arr
     - for x  in enumerate(y) :  lấy chỉ số index và lặp lại trong array

```python
     # Lặp vòng lặp khi  biết trước số vòng lặp
          # step
          for x in range(3):
               print(f'Vòng lặp:{x}')
               # ==> KQ: lặp  lại 3 lần
          arr=[2,3,4]
          # ///// start, stop
               for x in range(1,3):
                    print(f'Vòng lặp:{x}')
                    # ==> KQ: lặp  lại 3 lần
               arr=[2,3,4]
          # ///// start, stop,step
               for x in range(1,3,1):
                    print(f'Vòng lặp:{x}')
                    # ==> KQ: lặp  lại 3 lần
               arr=[2,3,4]
     # Lặp vòng lặp không biết vòng lặp nhất định
          for x in arr:
               print(f'Vòng lặp Arr:{x}')
               # ==> KQ: lặp  lại 3 lần in ra lần lượt các số trong mảng

     # lặp  và lấy chỉ số index
          fruits = ['apple', 'banana', 'cherry']
          for index, fruit in enumerate(fruits):
               print(f"Index: {index}, Fruit: {fruit}")


     # ===> Sự khác nhau của for  in và for in range() và for in  enumerate() là:
                         # +For in:  là lặp trong mảng
                         # +For in range() : lặp  đi lặp lại các số chuyền trong range(y)
                         # +For in enumarate : lặp để lấy dữ liệu trong mảng và lấy cả index chỉ số của nó
```

     - while  : Vòng lặp

```python
          # chạy vòng lặp while
          n= 0
          while n < 8:
               n+=1;
          # chạy vòng lặp true:
          while(True):
               # Vòng lặp chạy cho đến khi =
```

////////////////////////////////////////////// Câu điều kiện ///////////////////
if( a==b):
<!-- Cho phép bạn kiểm tra điều kiện -->
elif ( a==c):
<!-- Cho phép bạn kiểm tra trường hợp trong khi điều kiện sai -->
else:
<!-- Trường hợp else là trường hợp sai -->
pass
<!--  Hiểu đơn giản nó cho  phép ta để trống vị trí đó nếu chưa điền gì vào trong đó -->

////////////////////////////////////////////// List (array list) /////////////////// - list() : Cho phép bạn tạo danh sách trong python
: [<start>:<end>] ==> cho phép bạn lát cắt trong python
: [<item>] ==> Lấy ví trị trong list
: [<vitri>::<step>] ==> Cho phép bạn bắt đầu vị trí và lấy trong danh sách - del(<item>) : Xóa phần tử trong list - append(<item>) : Thêm vào trong list - insert(<index>,<item>) : THêm một phần tư vào một vị trí được chỉ định và các chỉ số khác sẽ đc +1 <item> - sort() : Sắp xếp theo thứ tự tăng dần - remove(<giaTriChoTruoc>) : Xóa phần tử được giá trị cho trước - pop(<item>) : Xóa phần tư tại vi tri truyèn vao - reverse() : đảo ngược danh sách list - clear() : Xóa tất cả các phần tử

![Vd:Su_dung_list](./tk_list.py)

////////////////////////////////////////////// Tuple ///////////////////

////////////////////////////////////////////// Array (mảng arr) ///////////////////

     Arr : là kiểu mảng được khai báo.
     len() : kiểm tra độ dài của mảng,  của kí tự....
     append() : Thêm phần tử vào mảng
     insert() : Thêm phần tử vào trong mảng vào một vị trí bất kì
     extend() : Thêm một mảng khác vào cuối danh sách phần tử trong mảng trước đó
     pop() : Xóa phần tử
     remove() : Cũng là xóa phần tử (có thử sử dụng một trong hai  để xóa phần tử)
     clear()  :  Xóa bỏ tất cả trong mảng
     count()  : Đếm số lần xuất hiện trong mảng
     index()  : Đếm chỉ số trong mảng
     reverse(): Đảo ngược mảng trong phần tử
     sort()   : Sắp xếp các phần tử trong mảng

![Vd: Sử dụng các thuộc tính trong python](./tk_hàm_thuộc_tính.py) link : https://www.w3schools.com/python/python_arrays.asp

===> Sự khác nhau của list và array: + List: cho phép bạn thêm được nhiều kiểu dữ liệu khác nhau trong cùng một list. Chạy chậm hơn + Array: Lưu trữ đc 1 kiểu dữ liệu trong 1 arays. Chạy nhanh hơn list

////////////////////////////////////////////// Json object ///////////////////

////////////////////////////////////////////// Hàm def(function) + object- class ///////////////////
def <dặt_tên_hàm> (<tham_chieu>):

     lambda : Hàm này là cho  phép bạn định nghia def (function) một cách đơn giản hơn, ngan gon(logic cao)

     ----->  Hàm sinh ra để giup ta xay dựng phát triển và tái sử dụng một cách đơn giản hơn!

![VD:tham_khao_sudung_def_lambda](./tk_function_Def.py)

////////////////////////////////////////////// Hàm /////////////////// - global : Biến toàn cục sẽ sử dụng cho phép bạn sử dụng. Khi sử dụng biến toàn cầu để thay gán đc giá trị bên trong ra bên ngoài.

```python

          #  Global
               count = 0
               def increment():
                    global count
                    count += 1
               increment()
               increment()
               print(count)  # Output: 2

```

////////////////////////////////////////////// Class (OPP huong doi tuong) /////////////////// - class <dat_ten> :
--> Cho phép bạn lập trình opp

          - super() : Cho phép bạn sử dụng lại các Claas cha trong thằng con

![VD: Sử dụng Supertrong python](./tk_Class_OPP_Super.py)

////////////////////////////////////////////// Module Random /////////////////// - random.randrange(start, stop, step): Tạo số nguyên ngẫu nhiên trong một khoảng với bước nhảy nhất định. - random.random(): Ngẫu nhiên trong khoảng từ 0.0 đến 1.0 (không bao gồm 1.0) - random.uniform(a, b): Tạo số thực ngẫu nhiên trong khoảng (a, b). - random.choice(seq): Chọn ngẫu nhiên một phần tử từ một chuỗi, danh sách, hoặc tuple. - random.randint(a, b): Tạo ra một số nguyên ngẫu nhiên trong khoảng từ a đến b - random.shuffle(x): Trộn ngẫu nhiên các phần tử trong một danh sách. - random.sample(population, k): Chọn ngẫu nhiên k phần tử không trùng lặp từ một tập hợp (population). - random.seed(a): Thiết lập giá trị số ngẫu nhiên. Giúp bạn có thể tái tạo lại cùng một dãy số ngẫu nhiên. - random.gauss(mu, sigma): Tạo số ngẫu nhiên theo phân phối chuẩn.

     ==> Tham khảo: Moldum RanDom() : https://www.w3schools.com/python/module_random.asp


```python
          # random.choice
               import random
               fruits = ["apple", "banana", "cherry"]
               qua_ngau_nhien = random.choice(fruits)
               print(qua_ngau_nhien)  # Output: Ví dụ: "banana"
          # random.shuffle
               import random
               cards = [1, 2, 3, 4, 5]
               random.shuffle(cards)
               print(cards)  # Output: Ví dụ: [3, 5, 1, 4, 2]
```

////////////////////////////////////////////// Module Math /////////////////// - math.sqrt(x): Tính căn bậc hai của số x.
<!-- ==> Ví_dụ: math.sqrt(16) sẽ trả về kết quả là 4.0. --> - math.pow(x, y): Tính x mũ y.
<!-- ==> Ví_dụ: math.pow(2, 3) sẽ trả về kết quả là 8.0. --> - math.ceil(x): Làm tròn số x lên thành số nguyên nhỏ nhất lớn hơn hoặc bằng x.
<!-- ==> Ví_dụ: math.ceil(2.3) sẽ trả về kết quả là 3. --> - math.floor(x): Làm tròn số x xuống thành số nguyên lớn nhất nhỏ hơn hoặc bằng x.
<!-- ==> Ví_dụ: math.floor(2.7) sẽ trả về kết quả là 2. --> - math.fabs(x): Tính giá trị tuyệt đối của số x.
<!-- ==> Ví_dụ: math.fabs(-5) sẽ trả về kết quả là 5.0. --> - math.sin(x), math.cos(x), math.tan(x): Tính giá trị sin, cos, tan của góc x (x tính bằng radian).
<!-- ==> Ví_dụ: math.sin(math.pi/2) sẽ trả về kết quả gần bằng 1.0. --> - math.pi: Hằng số pi (π).
<!-- ==> Ví_dụ: chu_vi = 2 * math.pi * ban_kinh để tính chu vi hình tròn. --> - math.e: Hằng số Euler (e).
<!-- ==> Ví_dụ: luy_thua_e = math.e ** 2 để tính e mũ 2. --> - math.log(x): Tính logarit tự nhiên (cơ số e) của x.
<!-- ==> Ví_dụ: math.log(math.e) sẽ trả về kết quả là 1.0. --> - math.log10(x): Tính logarit cơ số 10 của x.
<!-- ==> Ví_dụ: math.log10(100) sẽ trả về kết quả là 2.0. -->

     ==> Link_ThamKhao: https://www.w3schools.com/python/module_math.asp

////////////////////////////////////////////// module request ///////////////////
////////////////////////////////////////////// module date ///////////////////
////////////////////////////////////////////// File ///////////////////

          - Mode trong file :
                    r : Mở để đọc. Mode mặc định
                    r+: Mở để đọc và ghi
                    w : Mở để ghi-Xóa hết text cũ-Không tồn tại tự tạo 1 file cùng tên
                    w+: Mở để Ghi Đọc -Xóa hết text cũ-Không tồn tại tự tạo 1 file cùng tên
                    a : Mở để ghi-Không tồn tại tư tạo file
                    a+: Mở để ghi và đọc -Không tồn tại tư tạo file
                    x : tạo file mới- Nhưng thất bại khi tồn tại file
                    b : Mở file chế độ nhị phân

          - Kiểm tra file:
                    exists(path): Kiểm tra xem một file hoặc thư mục có tồn tại hay không (trong module os).
                    isdir(path): Kiểm tra xem một đường dẫn có phải là một thư mục hay không (trong module os).
                    isfile(path): Kiểm tra xem một đường dẫn có phải là một file hay không (trong module os).
                    remove(path): Xóa một file (trong module os).
                    rename(src, dst): Đổi tên hoặc di chuyển một file (trong module os).
          - File:
                    read()    : Đọc file
                    write()   : Viết vào file
                    close()   : đóng file

![VD:Tham khảo_file](./tk_File.py)

----------------------------------------------- File.csv--------------------------
File sử dụng bằng.csv: - khai báo thư viện: import csv (pip install csv) - THuộc tính: + next() : cho phép bạn bỏ qua dòng tiêu đề: + csv.QUOTE_ALL: Tất cả dấu ngoặc kép, dấu đặc biệt. + csv.QUOTE_MINIMAL: Chỉ bao quanh các trường có chứa dấu phẩy, dấu ngoặc kép hoặc ký tự đặc biệt khác. + csv.QUOTE_NONNUMERIC: Chỉ bao quanh các trường không phải là số. + csv.QUOTE_NONE: Không bao quanh bất kỳ trường nào.

               - Đọc file csv:
                    + csv.reader(<ten_file>) :  đọc file trả về array
                    + csv.DictReader(<ten_file>)

               - Viết file csv:
                    + csv.DictWriter(<tên_file> , <định_dạng>, <thuộc_tính> )

                    + writeheader() : Cho phép bạn ghi hàng tiêu đề với cột

                    + writerow({<định_dạng>: <chuyền_vào>}) : Cho phép bạn ghi dữ liệu vào hàng song song với tiêu đề

```python
                    # ĐỂ ĐỌC ĐƯỢC TIẾNG VIỆT PHẢI CHUYỂN MÃ HÓA SANG UTF-8
                    # VD: with open('tung.csv', 'w+' , encoding='utf-8')
```

![Vd:Sử_dụng_csv](./tk_File_csv.py)

////////////////////////////////////////////// try + except ///////////////////

     - try excpet ValueError :
               ===>  Sử lý ngoại lệ
     - try suite : 
               ===> đưa ra khả năng ngoại lệ có thể sử lý được nhiều ngoại lệ khác nhau
     -  try  finally

```python


```
////////////////////////////////////////////// numpy ///////////////////
////////////////////////////////////////////// tkinner ///////////////////
////////////////////////////////////////////// web python ///////////////////
