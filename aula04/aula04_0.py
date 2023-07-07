# PRINT

#O print() é utilizado para imprimir a mensagem no terminal e podemos utilizar a 
#virgula para separar os argumentos. ")

h = 13;

print("Vou parar de estudar para fazer almoço as ", h);

""" O sep='/', foi utilizado para informar que no lugar do espaço quero a barra.
O end='.\n'foi utilizado para informar que não é para dar um enter no final do programa e 
colocar no ponto. """ 

dia = 15;
mes = 10;
ano = 1997;

print(dia, mes, ano, sep='/', end='.\n');

# INPUT 

""" O comando input() é usado para solicitar dados do usuário no shell
Lembrando que mesmo que o usuário digite um valor numérico, o type do dado  sempre vai ser 
string """

idade = input('Digite sua idade:');

print(type(idade));

""" O comando eval() faz com que a expressão que está em string seja analisada como 
expressão Python.  """

idadeNumerico = eval(idade);

idade2023 = idadeNumerico + 1;

print(type(idadeNumerico));

print(idade2023);

c = input("Digite a temperatura em Celsius:");
c_temp = eval(c);

f = 1.8 * c_temp + 32;

print(f, 'graus Fahrenheit');

