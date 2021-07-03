totalCompras = 0
valorRecebido = 0
troco = 0
trocoFinal = 0
modedas = [200, 100, 50, 20, 10, 5, 2]

totalCompras = int(input('Digite o valor total da compra: '))
valorRecebido = int(input('Digite o valor recebido do cliente: '))
troco = valorRecebido - totalCompras
print(troco)



for i in modedas:
    trocoFinal = int(troco / i)
    print(f'Notas de R${i}: ',trocoFinal)
    if (trocoFinal >= 1):
        trocoCliente = i
        print('Seu troco é ', trocoCliente * trocoFinal)
        troco = troco - (trocoFinal * i)
        print("=================== troco", troco)
    else:
        print('Não tem troco')    

