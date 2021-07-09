totalCompras = 0
valorRecebido = 0
troco = 0
trocoFinal = 0
modedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05]

totalCompras = float(input('Digite o valor total da compra: '))
valorRecebido = float(input('Digite o valor recebido do cliente: '))
troco = valorRecebido - totalCompras
print('O troco é: R$ ', round(troco, 2))
for i in modedas:
    trocoFinal = int(troco / i)
    if trocoFinal != 0:
       
        if (trocoFinal >= 1):
            trocoCliente = i
            if(trocoCliente >= 2):
                print(trocoFinal, 'Nota(s) de R$ %.2f' %i)
            else:
                print(trocoFinal, 'Moeda(s) de R$ %.2f' %i)
        troco = troco - (trocoFinal * i)
