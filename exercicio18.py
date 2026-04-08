import math

ang = float(input('Digite o valor do angulo: '))
cos = math.cos(math.radians(ang))
se = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Do angulo {}º , o seu cosseno é {}, seu seno é {} e a sua tangente é {}'.format(ang, cos, se, tan))