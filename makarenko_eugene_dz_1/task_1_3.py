# 3-ая задача

def functionale(x):
    if x % 10 == 1:
        print("1 процент")
    elif 1 < x % 10 < 5:
        print(f"{x} процента")
    else:
        print(f"{x} процентов")
functionale(1)
functionale(2)
functionale(5)