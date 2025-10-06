#সমস্যা:একটি সংখ্যা জোড় (even) নাকি বিজোড় (odd) তা চেক করুন।
#সমাধান:
num = int(input("Enter the number: "))
if num%2 == 0:
 print(num, "This is even number")
else:
 print(num, "This is odd number")