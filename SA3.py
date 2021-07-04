totalCompras = 0
valorRecebido = 0
troco = 0
trocoFinal = 0
modedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]

totalCompras = float(input('Digite o valor total da compra: '))
valorRecebido = float(input('Digite o valor recebido do cliente: '))
troco = valorRecebido - totalCompras
print('O troco é: R$ ', round(troco, 2), 'Reais')
for i in modedas:
    trocoFinal = int(troco / i)
    if trocoFinal != 0:
       
        if (trocoFinal >= 1):
            trocoCliente = i
            if(trocoCliente >= 2):
                print('Seu troco é ', trocoCliente * trocoFinal)
                print(f'Notas de R${i}: ',trocoFinal)
            else:
                print('Seu troco é ', trocoCliente * trocoFinal)
                print(f'Moedas de R${i}: ',trocoFinal)
        troco = troco - (trocoFinal * i)
        
            # if(trocoFinal > 0 and trocoFinal < 1):
            #     trocoMoedas = trocoFinal
            #     trocoMoedas = float(troco / i)
            #     trocoCliente = i
            #     print('Seu troco é ', trocoCliente * trocoMoedas)
            #     print(f'Moeda de R${i}: ',trocoFinal)
            #     troco = troco - (trocoCliente * trocoMoedas)