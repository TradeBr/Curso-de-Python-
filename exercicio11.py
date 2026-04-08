larg = int(input('Digite o valor da largura da parede: '))
alt = int(input('Digite o valor da altura da parede: '))
area = larg*alt
tinta = area/2
print('Então a largura da parede é igual a {} e a altura igual a {}, nesse caso a área da parede é de {}m² e vamos precisar de {}L de  tinta'.format(larg,alt,area,tinta))
