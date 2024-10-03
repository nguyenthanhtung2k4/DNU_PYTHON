import os,  sys
def check(file):
     if os.path.exists(file):
          return file
def main():
     while True:
          try:
               file= input('Nhap  file: ')
               if check(file):
                    break;
          except FileNotFoundError:
               print("Vui  long nhap lai!")
     with open(file, 'r') as file:
          text=file.read()
          print(set(text.strip().split()))
if __name__ == '__main__':
     file='set.txt'
     main()