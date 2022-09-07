import random
import os

opcoes = ["Pedra", "Papel", "Tesoura"]
while True:
    menu = input("""
        [1]- Tesoura
        [2]- Papel
        [3]- Pedra
        Digite a opção desejada:""")
    opcoes_robo = random.choice(opcoes)
    if menu == "1":

        if opcoes_robo == "Papel":
            print(f"Robo escolheu {opcoes_robo}. Voce Ganhou!")
        elif opcoes_robo == "Tesoura":
            print(f"Robo escolheu {opcoes_robo}. Empate!")
        else: 
            print(f"Robo escolheu {opcoes_robo}. Voce perdeu!")

    elif menu == "2":

        if opcoes_robo == "Pedra":
            print(f"Robo escolheu {opcoes_robo}. Voce Ganhou!")
        elif opcoes_robo == "Papel":
            print(f"Robo escolheu {opcoes_robo}. Empate!")
        else: 
            print(f"Robo escolheu {opcoes_robo}. Voce perdeu!")

    elif menu == "3":

        if opcoes_robo == "Tesoura":
            print(f"Robo escolheu {opcoes_robo}. Voce Ganhou!")
        elif opcoes_robo == "Pedra":
            print(f"Robo escolheu {opcoes_robo}. Empate!")
        else: 
            print(f"Robo escolheu {opcoes_robo}. Voce perdeu!")

    sair = input ("Deseja jogar novamente? [Y]Yes [N]No:")

    if sair.upper() == "N":
        print("Fechando o jogo...")
        break
    os.system("cls")

    