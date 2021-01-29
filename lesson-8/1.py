class Data:

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def param(cls, day_month_year):
        my_data = []
        for i in day_month_year.split():
            if i != '-':
                my_data.append(int(i))
        return f'current day: {my_data[0]}, current month: {my_data[1]}, current year: {my_data[2]}'

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year == 2021:
                    return f'the date is correct'
                else:
                    return 'the year is not correct'
            else:
                return 'the month is not correct'
        else:
            return 'the day is not correct'

    def __str__(self):
        return f'current date: {Data.param(self.day_month_year)}'


d = Data('28 - 1 - 2021')
print(d)
print(d.validation(5, 11, 2222))
print(d.validation(30, 15, 2021))
print(d.param('20 - 10 - 2020'))
