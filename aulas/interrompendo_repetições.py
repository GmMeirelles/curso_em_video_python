#break
# usado para parar um laço de repetição while
tal_coisa = 0
while tal_coisa != 10:
    if tal_coisa < 7:
        tal_coisa += 1
        print(f"Tal Coisa: {tal_coisa}")
    if tal_coisa >= 8:
        print(f'{tal_coisa} quase no fim')
        tal_coisa += 1
    if tal_coisa == 7:
        tal_coisa += 1
print(f'{tal_coisa} finalmente Tal coisa chegou a 10')