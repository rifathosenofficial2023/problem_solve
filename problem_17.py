#সমস্যা:একটি সংখ্যা Armstrong সংখ্যা কিনা তা পরীক্ষা করুন।(উদাহরণ: 153→13 +5³ + 32 = 153)
#সমাধান:
num = int(input("একটি সংখ্যা লিখুন: "))
sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))
if num == sum_of_digits:
 print(num, "একটি Armstrong সংখ্যা")
else:
 print(num, "Armstrong সংখ্যা নয়")