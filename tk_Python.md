////////////////////////////////////////////// Thư viện ///////////////////
          
          - import math : thư viện liên quan đến toán và sử dụng như lấy giá trị pi....

////////////////////////////////////////////// Các câu gợi  ý ///////////////////
           # : Conment 1 dòng
           '''{Conment}''' : Conment nhiều dòng
           \  : tiếp tục nhiều dòng khi hàm quá dài có thể dùng \ để xuống dòng rồi viết tiếp
           \n : xuống dòng
           \t tab trắng
           


////////////////////////////////////////////// Các  Hàm quan trọng ///////////////////

////////////////////////////////////////////// Toán học  ///////////////////
     + phép cộng
     - phép trừ
     * phép nhân
     ** phép chia lũy thừa
     /  phéo chia lấy so thap phan
     //  phéo chia nguyên
     % phép chia lấy phần dư

-----------------------------------------------------------------------------------------
     int() : kiểu số nguyên
     float(): kiểu số thực

------------------------------------------Hàm liên quan đến Toán -------------------------

     - pow({Số1},{Số2}) : Cho phép bạn tính số mũ
     - round({số_thập_phân}, {lấy_sau_số_phẩy}) :  cho  phép bạn lấy số thập phân
     - :.2f : Làm tròn sau hai chữ số thập phân(* Lưu ý:  2f chỉ được dùng trực tiếp khi in ra)

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
    
     - for x  in  range({Số_vòng_lặp}) : Vòng lặp
     - for x in  y : lặp  trong arr 
     - for x  in enumerate(y) :  lấy chỉ số index và lặp lại trong array


```python
          for x in range(3):
               print(f'Vòng lặp:{x}')
          # ==> KQ: lặp  lại 3 lần
          arr=[2,3,4]
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


////////////////////////////////////////////// Câu điều kiện  ///////////////////
     if( a==b): 
     <!-- Cho phép bạn kiểm tra -->



////////////////////////////////////////////// Array (mảng arr)   ///////////////////


////////////////////////////////////////////// Objeay (json object)   ///////////////////