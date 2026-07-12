rows = int(input("Enter the number of rows: "))

number = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()
  
'''
O/P:
Enter the number of rows: 4
1 
2 3 
4 5 6 
7 8 9 10 
'''
