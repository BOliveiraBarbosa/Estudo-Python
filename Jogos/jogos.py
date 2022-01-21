import jogo_forca
import jogo_adivinhacao

print("*******************")
print("Escolha o seu jogo!")
print("*******************")
print("\n")

print("(1) Forca | (2) Adivinhação")
jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando Forca...\n")
    jogo_forca.jogar()
elif(jogo == 2):
    print("Jogando Advinhação...\n")
    jogo_adivinhacao.jogar()
