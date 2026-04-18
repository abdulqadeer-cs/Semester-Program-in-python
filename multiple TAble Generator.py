start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
for num in range(start, end + 1):
    print("\nTable of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
