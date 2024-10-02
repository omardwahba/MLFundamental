total = 0
numOfCups = int(input("pls, enter number of cups: "))
size = input("pls enter L for Large size or M for medium size: ")
if size == 'L':
    total = numOfCups * 10
elif size == 'M':
    total = numOfCups * 5

print("====================== Check out ============================")
print("your Final cost is : ", total, " LE.")
print("====================== Thank you ============================")