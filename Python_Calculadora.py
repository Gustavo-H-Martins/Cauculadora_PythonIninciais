# Calculadora em Python
import time

contador = 0
operador = 0
n1 = 0
n2 = 0
resultado = 0
ciclo = 0
total = 0
print(f'{3 * "^~^"} esta é uma calculadora de Python, me ajude a melhorá-la e tornar algo melhor ? {3 * "^~^"}')

while ciclo != 'N':
    contador += 1
    n1 += int(input(f'Insira aqui o {contador}º número:  '))
    if total == 0:
        total = n1
    else:
        if "+" in operador:
            total += n1
        elif "-" in operador:
            total -= n1
        elif "/" in operador:
            total /= n1
        elif "*" in operador:
            total *= n1
        elif "P" in operador:
            var = total ** n1
        elif "%" in operador:
            var = total % n1
    operador = input("Qual o tipo de operação ?"
                     "\n[+] - Adição"
                     "\n[-] - Subtração"
                     "\n[/] - Divisão"
                     "\n[*] - Multiplicação"
                     "\n[P] - Potência"
                     "\n[%] - Resto de uma divisão"
                     "\n   :   ").strip().upper()[0]
    if "+" in operador:
        operador = operador
    elif "-" in operador:
        operador = operador
    elif "/" in operador:
        operador = operador
    elif "*" in operador:
        operador = operador
    elif "P" in operador:
        operador = operador
    elif "%" in operador:
        operador = operador
    else:
        print("Entrada inválida esta operação vai dar erro.")
        break

    contador += 1
    n2 += int(input(f' Insira agora o {contador}º número:  '))
    if "+" in operador:
        resultado = n1 + n2
        total += n2
    elif "-" in operador:
        resultado = n1 - n2
        total -= n2
    elif "/" in operador:
        resultado = n1 / n2
        total /= n2
    elif "*" in operador:
        resultado = n1 * n2
        total *= n2
    elif "P" in operador:
        resultado = n1 ** n2
        var = total ** n2
    elif "%" in operador:
        resultado = n1 % n2
        var = total % n2
    else:
        break
    ciclo = input(f'O resultado desta operação até agora é {resultado}, deseja continuar ?'
                  f'\n[S] - Sim'
                  f'\n[N] - Não'
                  f'\n     :      ').upper().strip()[0]
print(f'Obrigado por testar este algorítimo!'
      f'\n Enquanto estávamos realizando esta operação, realizando operações de acordo'
      f'\n com seus inputs, e com isso geramos um resultado total veja abaixo o total manipulado'
      f'\n{total}    ')
time.sleep(3)
print("Até mais!")
