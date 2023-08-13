larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('Sua parede tem a dimensão {} x {} e sua área é de {}m².'.format(larg, alt, larg*alt))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(larg*alt/2))
