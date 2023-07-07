"""  Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe 
a temperatura em graus Celsius usando a fórmula

Seu programa deverá ser executado da seguinte forma:
>>>
Digite a temperatura em graus Fahrenheit: 50
A temperatura em graus Celsius é 10.0
  """


f = input("Digite o valor da temperatura em Fahrenheit:");

f_temp = eval(f);

c = (f_temp - 32) / 1.8 ;

print( "A temperatura em graus Celsius é: " ,c);