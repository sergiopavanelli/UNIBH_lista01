nome = "Medvedev"
sal_fix = input("Informe o valor do salário fixo atual: ")
mont_vendas = input("Informe o montante de vendas no mês em R$: ")
total = float(sal_fix) + float(mont_vendas)*0.15
print("TOTAL =", "R$", "{:.2f}".format(total))
