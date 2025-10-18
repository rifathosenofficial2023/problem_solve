#সমস্যা:একটি সংখ্যা ইনপুট নিয়ে সেটি মৌলিক সংখ্যা কিনা তা পরীক্ষা করুন।
num= int(input("একটি সংখ্যা লিখুন: "))
if num >1:
 for i in range(2, int(num**0.5) + 1):
  if num% i == 0:
     print(num, "মৌলিক সংখ্যা নয়")
     break
 else:
  print(num, "একটি মৌলিক সংখ্যা")
else:
  print(num, "মৌলিক সংখ্যা নয়")