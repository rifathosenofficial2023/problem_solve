#সমস্যা:একটিসংখ্যা উল্টো করলে যদি সেটি একই থাকে,তাহলে সেটি palindromel

num = input("Enter the number : ")
if num == num[::-1]:
 print(num,"It is palindrome number")
else:
 print(num, "It is not palindrome number")