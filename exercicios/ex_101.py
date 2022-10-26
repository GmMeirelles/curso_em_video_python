def idade(num):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - num 
    if idade < 18:
        return 'Não vota'
    
    elif idade > 18 and idade < 65:
        return 'Voto obrigatorio'

    else:
        return 'Voto opcional'


print(idade(1900))