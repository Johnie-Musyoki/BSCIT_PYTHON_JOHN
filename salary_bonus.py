#find bonus based on years of service
salary =int(input("enter the salary:"))
years= int(input("enter years of service:"))
if (years>=10):
    bonus= 0.1 *salary
elif years>=6 and years < 10:
     bonus= 0.08*salary
else:
    bonus= 0.05* salary
print("the bonus is",bonus)
net_salary = salary +bonus
print("the net salary is", net_salary)