workHours = int(input("Input the number of wokred hours: "))
hourlyPay = float(input("Input your hourly rate: "))

salary = workHours * hourlyPay

print(salary)



def total_euro(work_hours, hourly_pay):
    return work_hours * hourly_pay

print(total_euro(workHours, hourlyPay))