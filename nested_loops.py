# nested loops are loops within another loop the nested loop will finish itself first

row = int(input("Enter amount of rows: "))
columns = int(input("Enter amount of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(row):  # outer loop for rows
    for j in range(columns):  # inner loop for columns
        print(symbol, end="")  # end="" stops from moving to next line
    print()
