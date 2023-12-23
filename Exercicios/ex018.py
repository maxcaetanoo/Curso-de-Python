import math
angle = int(input('Digite um angulo inteiro: '))
print('O Seno de {} é {:.2f} \nO Cosseno de {} é {:.2f} \nE a Tangente de {} é {:.2f}'.format(angle, math.sin(math.radians(angle)), angle, math.cos(math.radians(angle)), angle, math.tan(math.radians(angle))))
