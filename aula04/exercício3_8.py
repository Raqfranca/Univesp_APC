""" Exercício 3.8
Defina, diretamente no shell interativo, a função média(), que aceita dois números como entrada e 
retorna a média dos números. """

num1 = input("Digite o primeiro valor:");

num2 = input("Digite o segundo valor:");

valorNum1 = eval(num1);
valorNum2 = eval(num2);

media = (valorNum1 + valorNum2) / 2 ;

print("A média entre os valores é de: ", media );

