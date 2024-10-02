def main():
     dict={}
     nhap=int(input("Nhap so i: "))
     for i in range(1,nhap+1):
          so=f"so{i}"
          dict.update({so:i*i})
     print(dict)

if __name__=='__main__':
     main()