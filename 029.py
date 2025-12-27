from time import sleep

print('Você está viajando de férias com sua família...')
sleep(1)
print('Ao chegar em uma rodovia, você avista uma placa.')
sleep(1)
print('⚠️ É uma placa que sinaliza um radar!')
sleep(2)
print()

V_MAX = 120 

velocidade = int(input('Qual a velocidade atual do carro? -> '))

if velocidade == V_MAX:
    print(f'🚗 Você está no limite de velocidade ({velocidade} km/h). Tenha cuidado!')
    print('💡 O recomendado para a via é 100 km/h.')

elif velocidade < V_MAX:
    print(f'✅ Tudo certo! Você está a {velocidade} km/h, abaixo do limite de 120 km/h.')

else:
    print('🚓 Você foi multado!')
    print(f'❌ Velocidade registrada: {velocidade} km/h')
