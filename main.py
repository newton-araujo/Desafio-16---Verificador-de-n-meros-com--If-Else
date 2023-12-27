"""
Desafio 16 - Vericando número com IF ELSE.

Neste desafio vamos verificar uma entrada informada pelo o usuário.
- Caso o número informado for maior que 10.
        *Vamos informar que o número é maior que 10.
- Caso o número informado for menor que 10.
        *Vamos informar que o número é menor que 10.
"""


#informação informada pelo o usuário.
numero = int(input('informe um número: '))

#Condição para verificar o número.
if numero > 10:
    print('O número informado e maior que 10.')
else:
    print('O número informado é menor que 10.')

