velocidade_carro = float(input("digite sua velocidade: "))
limite = 80
multa = (velocidade_carro - limite) * 20  

if velocidade_carro > limite:
    print(f"a multa a pagar sera igual a: {multa}")
else:
    print(f"velocidade permitida")

