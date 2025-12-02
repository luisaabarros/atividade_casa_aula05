# DESAFIO 1

# nota_1 = float(input('Informe a primeira nota: '))
# nota_2 = float(input('Informe a segunda nota: '))
# nota_3 = float(input('Informe a terceira nota: '))
# nota_4 = float(input('Informe a quarta nota: '))

# media = (nota_1 + nota_2 + nota_3 + nota_4) // 4

# print(f'Sua média é: {media}')

# if media > 7:
#     print('Aluno aprovado.')
# elif media <= 7 and media > 5:
#     print('Aluno em recuperação.')
# else:
#     print('Aluno em reprovado.')

# DESAFIO 2

# codigo = int(input('Insira o código: '))

# match codigo:
#     case 1:
#         print ('Sul')
#     case 2:
#         print('Norte')
#     case 3:
#         print('Leste')
#     case 4:
#         print('Oeste')
#     case 5 | 6:
#         print('Nordeste')
#     case 7 | 8 | 9:
#         print('Sudeste')
#     case 10:
#         print('Centro-oeste')
#     case 11:
#         print('Noroeste')
#     case _:
#         print('Importado.')



# DESAFIO 3

valor = float(input('Digite o valor da compra: '))
av = (valor * 0.10)
a_vista = valor - av 
db = (valor * 0.05)
debito = valor + db
cd = (valor * 0.08)
credito = valor + cd
cq = (valor * 0.12)
cheque = valor + cq


print('Escolha a forma de pagamento: \n[1] À VISTA \n[2] PIX \n[3] DEBITO \n[4] CREDITO \n[5] CHEQUE')
opcao = int(input('Digite a opção desejada: '))

match opcao:
    case 1:
        print(f'Voce escolheu à vista, o valor de {valor} com o desconto ficou {a_vista}')
    case 2:
        print(f'Voce escolheu PIX, sua compra ficou {valor}')
    case 3:
        print(f'Voce escolheu débito, o valor de {valor} ficou {debito}')
    case 4:
        print(f'Voce escolheu crédito, o valor de {valor} ficou {credito}')
    case 5:
        print(f'Voce escolheu cheque, o valor de {valor} ficou {cheque}')
    case _:
        print('Opção inválida.')
