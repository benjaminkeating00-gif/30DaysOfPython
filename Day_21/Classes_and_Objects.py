class Statistics:
    def __init__(self, data):
        self.data = list(data)

    def count(self):
        return len(self.data)

    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)

    def data_range(self):
        return self.maximum() - self.minimum()

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        s = sorted(self.data)
        n = len(s)
        mid = n // 2
        k = n % 2
        return k * s[mid] + (1 - k) * (s[mid - 1] + s[mid]) / 2

    def mode(self):
        return max(set(self.data), key=self.data.count)

    def variance(self, population=False):
        n = len(self.data)
        m = self.mean()
        ss = sum((x - m) ** 2 for x in self.data)
        divisor = n - (not population)
        return ss / divisor

    def stdev(self, population=False):
        return self.variance(population) ** 0.5

    def percentile(self, p):
        s = sorted(self.data)
        n = len(s)
        pos = p / 100 * (n - 1)
        lo = int(pos)
        hi = lo + ((lo + 1) < n)
        frac = pos - lo
        return s[lo] + frac * (s[hi] - s[lo])

    def frequency_distribution(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1
        return freq

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats = Statistics(ages)
print("Count:", stats.count())
print("Minimum:", stats.minimum())
print("Maximum:", stats.maximum())
print("Range:", stats.data_range())
print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Variance (sample):", stats.variance())
print("Standard Deviation (sample):", stats.stdev())
print("25th Percentile:", stats.percentile(25))
print("50th Percentile:", stats.percentile(50))
print("Frequency Distribution:", stats.frequency_distribution())

class PersonAccount:
    def __init__(self, first_name, last_name, incomes, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses
        self.description = ''
    def account_info(self):
        return f'Account holder: {self.first_name} {self.last_name}\nIncomes: {self.incomes}\nExpenses: {self.expenses}'
    def add_income(self, description, add_income):
        self.incomes.update({description: add_income})

    def add_expense(self, description, add_expense):
        self.expenses.update({description: add_expense})

    def account_balance(self):
        return sum(self.incomes.values()) - sum(self.expenses.values())

print('\n'*2)

account1 = PersonAccount(
    first_name="Emma",
    last_name="Rodriguez",
    incomes={
        "Salary": 4800,
        "Freelance Web Design": 1200,
        "Dividends": 300,
        "Selling old furniture": 150
    },
    expenses={
        "Rent": 1800,
        "Groceries": 450,
        "Utilities": 200,
        "Internet": 80,
        "Transportation": 150,
        "Gym Membership": 60,
        "Entertainment": 120
    }
)
print(account1.account_info())
account1.add_income("Bonus", 500)
account1.add_expense("Dining Out", 90)

print("Updated Incomes:", account1.incomes)
print("Updated Expenses:", account1.expenses)
print("Account Balance:", account1.account_balance())
