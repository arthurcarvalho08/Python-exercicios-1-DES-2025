
salario = float(input("digite o quanto você ganha: "))

if salario <= 2000.00:
    print(f"seu salario é {salario + salario * 15 / 100}")
elif 2000.01 <= salario <= 5000.00:
    print(f"seu salario é {salario + salario * 10 / 100}")
else:
    print(f"seu salario é {salario + salario * 5 / 100}")
    # finalizado