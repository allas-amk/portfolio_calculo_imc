

def main():
    print("Seja bem vindo(a)! Vamos calcular seu IMC (Indice de Massa Corporal)?")
    peso = float(input("Qual seu peso? "))
    print("{} (Kg)".format(peso))
    altura = float(input("Qual sua altura? (m) "))
    print("{} (m)".format(altura))
    imc = peso / (altura * altura)
    print("Seu IMC é {:.1f}".format(imc))

main()