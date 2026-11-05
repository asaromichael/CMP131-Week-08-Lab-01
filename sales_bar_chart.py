store = int(input("Enter the number of stores."))
ast = ""

for i in range(store):
    sale = int(input("Enter today's sales for store " + str(i+1)+":"))
    ast = ast + "Store " + str(i+1) + ": "
    sale = sale/100

    for j in range(int(sale)):
        ast = ast + "*"
    ast = ast + "\n"
print(ast)