from datetime import date, timedelta


class MyRange:

    def __init__(self,start,end):
        self.start = start
        self.end = end
    

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor +=1

        if self.cursor == self.end:
            raise StopIteration
        return self.cursor


    
for item in MyRange(1,10):
    print(item)


# ----------------------------------
def get_date_range(start_date, end_date):
    date_list = []
    while start_date < end_date:
        date_list.append(start_date)
        start_date += timedelta(days=1)
    return date_list

print(get_date_range(date(2022, 1, 1),date(2022, 1, 10)))