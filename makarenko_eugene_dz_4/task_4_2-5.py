from utils import currency_rates
from sys import argv
for i in range(1, len(argv)):
    print(currency_rates(argv[i]))