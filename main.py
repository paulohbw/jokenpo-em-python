import funcao

print('----------------------')
print('bem vindo ao JO-KEN-PÔ')
print('----------------------')
print('')
print('temos dois modos de jogo')
print('')
print('jogador SOLO - você versus a maquina')
print('1v1 - você contra alguem')
print('')
print('modo 1 - jogo SOLO')
print('modo 2 - 1v1')
print('')
escolha = input('qual modo vai jogar? ')

if escolha == '1':
    funcao.contraPc()
elif escolha == '2':
    funcao.contraPessoa()
else:
    print('você é burro')
