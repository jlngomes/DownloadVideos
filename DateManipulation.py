from datetime import datetime

class DataManagement:
    _months = {1:"Jan", 2:"Fev", 3:"Mar", 4:"Abr", 5:"Mai", 6:"Jun",
               7:"Jul", 8:"Ago", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}

    def __init__(self):
        self._date_actual = datetime.today().date()

    @property
    def date_day(self):
        return str(self._date_actual.day)

    @property
    def date_month(self):
        return self._months.get(self._date_actual.month, "Mês inválido")

    @property
    def date_year(self):
        return self._date_actual.year

    @property
    def its_saturday(self):
        if self._date_actual.weekday() == 5:
            return True
        else:
            return False

class DateFormat(DataManagement):
    def format_date(self):
        return f"{self.date_day} {self.date_month} {self.date_year}"