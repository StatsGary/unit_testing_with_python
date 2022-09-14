import requests

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    def monthly_schedule(self, month):
        # Fake website - will fail
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response!'