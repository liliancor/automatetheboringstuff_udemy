def div42by(divideBy):
    try: 
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: you tried to divide by Zero')

print(div42by(42))
print(div42by(2))
print(div42by(0))
print(div42by(1))

#pode-se não colocar nenhum tipo de Erro. O programa irá pular TODOS os tipos de Erro. 