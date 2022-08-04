from datetime import date, timedelta

def get_date_range(start_date, end_date):
    while start_date < end_date:
        yield start_date
        start_date += timedelta(days=1)

dates = get_date_range(date(2022, 1, 1),date(2022, 1, 10))

for item in dates:
    print(item)


print('//////////////////////////////////')
numbers = range(1,10)

def gen_squares(number_iter):
    for num in number_iter: 
        yield num **2
q = gen_squares(numbers)
for square in q:
    print(square)

print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

numbers_sq = (item**2 for item in numbers if item % 2 == 0)
for number in numbers_sq:
    print(number)
print('********************************')
numbers_sq = [item**2 for item in numbers if item % 2 == 0]
print(numbers_sq)
