import random
import math

print("-"*35)
print("Vamos tentar adivinhar o número? ")
print("-"*35)
menor = int(input("Digite o Menor número:- "))

maior = int(input("Digite o Maior Número:- "))

x = random.randint(menor, maior)
print("\n\tVocê tem somente  ", round(math.log(maior - menor + 1, 2)), " chances para acertar!\n")

count = 0

while count < math.log(maior - menor + 1, 2):
    count += 1

    adivinha = int(input("Adivinhe o número:- "))

    if x == adivinha:
        print("Parabéns, você acertou em ", count, " tentativas")

        break
    elif x > adivinha:
        print("Tente novamente, seu número foi muito baixo")
    elif x < adivinha:
        print("Tente novamente, seu número foi muito alto")

if count >= math.log(maior - menor + 1, 2):
    print("\nO número é %d" % x)
    print("\tBoa sorte da próxima vez!")