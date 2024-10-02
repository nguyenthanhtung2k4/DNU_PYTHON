def bai1():
     string='nguyen thanh tung nguen thanh thanh'
     name=string.split()
     s=[]
     for i  in name:
          char=i[0].upper()
          s.append(char)
     print('.'.join(s),end='')
     
     
def bai2():
     num ='2541'.strip()
     tong=0
     for  i in num :
          tong+=int(i);
     print(tong)
     
     
     
bai2()