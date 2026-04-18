A=int(input("Age :"))
G=input("Gender= M/F:")
if((A==1 or A==2) and G=="M"):
    print("Fees Is 300 .")
elif((A==3 or A==4) or G=="F"):
    print("Fees IS 400 .")
elif(A==5 and G=="M"):
    print("Fees IS 500 .")
else:
    print("No Fees")