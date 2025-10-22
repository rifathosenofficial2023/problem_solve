#তিনটি বাহু দেওয়া হলে, ত্রিভুজটি সমবাহু (Equilateral), সমদ্বিবাহু
#(Isosceles), নাকি বিভিন্ন বাহু বিশিষ্ট (Scalene) তা নির্ণয় করুন।
#সমাধান:
a = float(input("প্রথম বাহু: "))
b = float(input("দ্বিতীয় বাহু:"))
c = float(input("তৃতীয় বাহু: "))
if a == b == C:
 print("ত্রিভুজটি সমবাহু (Equilateral)")
elif a == b or b == c or a == c:
 print("ত্রিভুজটি সমদ্বিবাহু (Isosceles)")
else:
 print("ত্রিভুজটি বিভিন্ন বাহু বিশিষ্ট (Scalene)")