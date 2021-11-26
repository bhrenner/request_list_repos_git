import requests

usuario = str(input('Nome de usuário do git: '))
repos = requests.get(f'https://api.github.com/users/{usuario}/repos')

#verifica o usuario atraves do status do response
if repos.status_code==200:  
    print('Repositórios disponivéis:')
    for x in repos.json():
        print(x['name'])
else:
    print('Usuário não encontrado')

