import requests

try:
    response = requests.get('http://pudim.com.br')
    status_code = response.status_code

    if status_code >= 200 and status_code <= 299:
        print('O site funfa')

    else:
        print(f'Algo deu errado: {status_code}')
        print(response.text)

except:
    print('Erro Site não encontrado')