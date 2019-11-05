spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue #é True, então ele pula direto para o while loop e não executa o print abaixo.
    print('Spam is ' + str(spam))