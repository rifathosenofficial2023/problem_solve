#How to check leap year 

year = int(input("Enter your old "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(year,'It is leap year')
else:
    print('It is not leap year')