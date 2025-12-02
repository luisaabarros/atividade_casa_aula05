# IF_ELIF_ELSE

# ATIVIDADE 1

# compra = float(input('Qual o valor da sua compra? '))
# desconto = (compra * 0.16)
# valor_final = float(compra - desconto)

# if compra > 250:
#     print(f'Parabéns! Você recebeu um desconto e o valor final da sua compra é de {valor_final}')
# else:
#     print(f'O valor final da sua compra é de {compra}')



# ATIVIDADE 2

# pedido = int(input('Qual a quantidade solicitada? '))
# estoque = 100
# peso = pedido * 2

# if pedido <= estoque and peso <= 50:
#     print(f'Pedido aprovado!')
# else:
#     print(f'Pedido não pode ser enviado.')



# ATIVIDADE 3

# tempo = int(input('Forneça o tempo que está na empresa: '))
# valor = float(input('Informe o valor movimentado nos últimos 6 meses: '))

# if tempo > 3 or valor > 5.000:
#     print(f'Você tem direito ao benefício especial!')
# else:
#     print('Você ainda nao cumpre os requisistos para o benefício.')



# ATIVIDADE 4

# valor = int(input('Forneça o valor: '))

# if valor < 0:
#     print('Valor inválido.')
# elif valor >= 0 and valor <= 50:
#     print('Valor considerado BAIXO.')
# elif valor >= 51 and valor <= 200:
#     print('Valor ACEITÁVEL.')
# else:
#     print('Valor ALTO e pode indicar um erro no dado.')



# ATIVIDADE 5

# valor = float(input('Informe o valor da compra: '))

# match valor:
#     case v if v > 500:
#         print(f'Frete grátis.')
#     case v if 300 <= v <= 500:
#         print(f'Frete 10$')
#     case v if 150 <= v <= 299:
#         print(f'Frete 20$')
#     case v if 80 <= v <= 149:
#         print(f'Frete 30$')
#     case v if v < 80:
#         print(f'Frete 45$')



# MATCH_CASE

#ATIVIDADE 1

# n = float(input('Forneça o número: '))

# match n:
#     case n if n > 0:
#         print('POSITIVO.')
#     case n if n < 0:
#         print('NEGATIVO.')
#     case n if n == 0:
#         print('ZERO.')



# ATIVIDADE 2 (nao entendi direito)

# valor = float(input('Forneça o valor da venda: '))

# match valor:
#     case v if v < 100:
#         print('Venda pequena.')
#     case v if 100 <= v < 500:
#         print('Venda média.')
#     case v if v >= 500:
#         print('Venda grande.')



# ATIVIDADE 3

print('[1] Criar usuário \n[2] Editar usuário \n[3] Visualizar usuário \n[4] Deletar usuário')
num = int(input('Digite a opção desejada: '))

match num:
    case 1:
        print('Criar usuário.')
    case 2:
        print('Editar usuário')
    case 3:
        print('Visualizar usuário')
    case 4:
        print('Deletar usuário')