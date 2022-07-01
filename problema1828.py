# Problema 1828

# pegando input
n = int(input())

# definindo as condições de vitória
for i in range(1, n + 1):
    sheldon, raj = input().split()
    

    if sheldon == raj:
        print("Caso #{}: De novo!")
    elif sheldon == "tesoura" and raj == "papel":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "papel" and raj == "pedra":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "pedra" and raj == "lagarto":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "lagarto" and raj == "Spock":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "Spock" and raj == "tesoura":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "tesoura" and raj == "lagarto":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "lagarto" and raj == "papel":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "papel" and raj == "Spock":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "Spock" and raj == "pedra":
        print("Caso #{}: Bazinga!".format(i))
    elif sheldon == "pedra" and raj == "tesoura":
        print("Caso #{}: Bazinga!")
    elif raj == "tesoura" and sheldon == "papel":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "papel" and sheldon == "pedra":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "pedra" and sheldon == "lagarto":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "lagarto" and sheldon == "Spock":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "Spock" and sheldon == "tesoura":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "tesoura" and sheldon == "lagarto":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "lagarto" and sheldon == "papel":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "papel" and sheldon == "Spock":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "Spock" and sheldon == "pedra":
        print("Caso #{}: Raj trapaceou!".format(i))
    elif raj == "pedra" and sheldon == "tesoura":
        print("Caso #{}: Raj trapaceou!".format(i))