import csv
# Đọc một tệp CSV trả về arr
def read_csv():
    with open('output.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            print(f'{row[0]}\t{row[1]}\t{row[2]}')
    
# Đọc tệp CSV và trả object
def read_csv2():
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], row['age'])

# Ghi dữ liệu vào một tệp CSV
def write_csv():
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'age', 'city']# Định dạng file chuyền vào.
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': 'Alice', 'age': 30, 'city': 'New York'})
        writer.writerow({'name': 'Bob', 'age': 25, 'city': 'Los Angeles'})
        
read_csv()