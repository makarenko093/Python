seconds = int(input('Введите кол. сек., которое вы хотите сконвертировать '))
YEARS = seconds // 3.154e+7
MONTHS = seconds % 3.154e+7 // 2.628e+6
WEEKS = seconds % 3.154e+7 % 2.628e+6 // 604800
DAYS = seconds % 3.154e+7 % 2.628e+6 % 604800 // 86400
HOURS = seconds % 3.154e+7 % 2.628e+6 % 604800 % 86400 // 3600
MINUTES = seconds % 3.154e+7 % 2.628e+6 % 604800 % 86400 % 3600 // 60
SECONDS = seconds % 3.154e+7 % 2.628e+6 % 604800 % 86400 % 3600 % 60
print(f"{seconds} секунд равняются", f"{YEARS} years/ {MONTHS} months/ {WEEKS} weeks/ {DAYS} days/ {HOURS} hours/ {MINUTES} minutes/ {SECONDS} seconds", sep="\n")
