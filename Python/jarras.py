import time


class Jarras:
    a = 0
    b = 0
    c = 8
    jarra1 = 'a'
    jarra2 = 'b'
    jarra3 = 'c'


def troca(x, y, origem, dest):
    if dest == 'a':
        max = 3
    elif dest == 'b':
        max = 5
    else:
        max = 8
    if y == max:
        print("Jarra cheia")
    else:
        while y < max:
            if x == 0:
                break
            else:
                x -= 1
                y += 1

    if dest == 'a':
        jarra.a = y
    elif dest == 'b':
        jarra.b = y
    else:
        jarra.c = y

    if origem == 'a':
        jarra.a = x
    elif origem == 'b':
        jarra.b = x
    else:
        jarra.c = x

    print("Situação: Jarra 1: "+str(jarra.a)+"L, Jarra 2: "+str(jarra.b)+"L, Jarra 3: "+str(jarra.c)+"L.")
    time.sleep(5)
    if jarra.b == 4 and jarra.c == 4:
        print("Correto!")


if __name__ == "__main__":

    jarra = Jarras()
    print("Situação: Jarra 1: " + str(jarra.a) + "L, Jarra 2: " + str(jarra.b) + "L, Jarra 3: " + str(jarra.c) + "L.")
    time.sleep(5)
    troca(jarra.c, jarra.a, jarra.jarra3, jarra.jarra1)
    troca(jarra.a, jarra.b, jarra.jarra1, jarra.jarra2)
    troca(jarra.c, jarra.a, jarra.jarra3, jarra.jarra1)
    troca(jarra.a, jarra.b, jarra.jarra1, jarra.jarra2)
    troca(jarra.b, jarra.c, jarra.jarra2, jarra.jarra3)
    troca(jarra.a, jarra.b, jarra.jarra1, jarra.jarra2)
    troca(jarra.c, jarra.a, jarra.jarra3, jarra.jarra1)
    troca(jarra.a, jarra.b, jarra.jarra1, jarra.jarra2)

# Você tem três jarras numa mesa a sua frente.
# A primeira comporta três litros, a segunda cinco litros e a última, comporta oito, e é a única que está cheia.
# Seu objetivo é separar quatro litros nas jarras b e c, e o único movimento que você pode fazer
# é o de trocar o líquido de uma jarra para a outra, até que ela atinja o limite da jarra que recebe,
# ou até o líquido da jarra que despeja acabar.
