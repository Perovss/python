import application.salary as cs
import application.db.people as ge
import datetime

if __name__ == '__main__':
    cs.calculate_salary()
    ge.get_employees()
    print(datetime.date.today())