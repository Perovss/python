from application.salary import *
from application.db.people import *
from datetime import date

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())