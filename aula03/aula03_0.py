# Videoaula 8 - Lista   

pessoa1 = [25, "Raquel", "Oliveira", 1.60, ["Rua 24 de abril", 25, "Santo André"], 11954768423];


print(pessoa1[4]);

#Operados

"""in - Ele vai verificar se o dado informado está na lista ou não"""

print("Raquel" in(pessoa1)); 

print("Raquel" not in(pessoa1)); 

print("Caio" not in(pessoa1)); 

"""+ = auto incremente, é utilizado em laços junto com for"""

""" * = Repete os items da lista, nesse exemplo ele repete todos os valores 4 vezes, não multiplica os números"""
print(4* (pessoa1));

""" len() - Conta quantos item tem na lista"""

print( len(pessoa1));

""" min(), max() e sum() - Só funciona em lista de dados tipo númericos, """

numeros = [25, 34, 100, 1001, 2587, 698, 4, 0.3, 90006, 708];

""" min() - Retorna o menor valor da lista"""

print( min(numeros));

""" max() - Retorna o maior valor da lista"""

print( max(numeros));

""" sum() - Retorna a soma de valores da lista"""

print( sum(numeros));

"""Alterando dados da lista"""

pessoa1[2] = "França";

print(pessoa1);

# Criando Tuplas - Iguais as listas mas imutáveis 

pessoa2 = (17, "Jorge", "Alvaro", 1.70, ("Avenida Brasil", 1500, "Rio de Janeiro"));

# pessoa2[2] = "ALves"; Não consigo alterar as tuplas. 

print(pessoa2[0]);

#Métodos 
# append() - Acredente um novo item na lista.

pessoa1.append("Brasileira");

print(pessoa1);

# count()- Conta quantos vezes o item passado no parametro aparece na lista. 

quantRaquel = pessoa1.count("Raquel");

print(quantRaquel); #Resultado: 1

print(pessoa1.count("25")); #Resultado: 0, porque o 25 da lista é númerico e não string. 

# index() - Ele retorna qual a posição esse item está na lista. Se ele aparcer em mais de uma posição, vai informar o valor do primeiro, lendo o cógico da esquerda para a direita. 

ondeRaquel = pessoa1.index("Raquel");

print(ondeRaquel);

print(pessoa1.index(1.60));


# insert() - Utilizamos para inserir um novo elemento, mas conseguimos informar em qual posição ele deve entrar

pessoa1.insert(2, "França");

print(pessoa1);

# pop() - Remove o elemento de uma posição específica

pessoa1.pop(2);

print(pessoa1);

# remove() - Remove o primeiro item que passamos como parametro.

pessoa1.remove("Raquel");

print(pessoa1);

# reverse() -  Inverte a ordem de classificação dos elementos.

pessoa1.reverse();

print(pessoa1[0]); #Como alterei a ordem o indice um troca para ultimo e o ultimo vira o 0 "primeiro". 


# sort() - Classifica a lista em ordem crescente, funciona apenas com números. 

numeros.sort();

print(numeros);

