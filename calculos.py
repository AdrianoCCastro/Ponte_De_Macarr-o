
qtd_Barras = int(input('Quantidade de barras: '))

for barra in range(0, qtd_Barras):
    esforco_interno = float(input('Digite o esforço da Barra: '))
    tipo = input('Digite o tipo da barra: ')
    comprimento = float(input('Digite o comprimento da Barra: '))

    if tipo == 'C' or tipo == 'c':
        resultado = ((esforco_interno*(comprimento*10)**2) /27906*1**4)**0.5
        

    elif tipo == 'T' or tipo == 't':
        resultado = esforco_interno/42.67
        
    print(resultado)
    print(teste)