dias = int(input('Quantos dias alugados? '))
kms = float(input('Quantos km rodados? '))
dia = 60.00
km = 0.15
valor = (dia * dias) + (km * kms)
print('O total a pagar é de R${:.2f}'.format(valor))
