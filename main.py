import requests
from colorama import Fore


def main():
    print(Fore.BLUE + '''
- - - - - - - - - - - - - - - - - - - - - - - -
Hypesquad badge obtainer Tool
Github: https://github.com/Void-Expanding/
- - - - - - - - - - - - - - - - - - - - - - - -
_______________________________________________
OPTIONS:
[1]: House of Bravery
[2]: House of Brilliance
[3]: House of Balance
[4]: Remove Badge
_______________________________________________
''')
    option = int(input(Fore.YELLOW + 'Enter option: '))
    user_token = input(Fore.YELLOW + 'Enter discord account token: ')
    if option == 1:
        get_hypesquad(option, user_token)
    elif option == 2:
        get_hypesquad(option, user_token)
    elif option == 3:
        get_hypesquad(option, user_token)
    elif option == 4:
        remove_hypesquad(user_token)
    else:
        print('Invalid choice')


def get_hypesquad(badge, token):
    response = requests.post('https://discord.com/api/v9/hypesquad/online', headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.8103.48 Mobile Safari/537.36', 'Authorization': token}, json={'house_id': badge})
    if response.status_code == 204:
        print(Fore.GREEN + 'You have successfully obtained hypesquad badge')
    elif response.status_code in (401, 403):
        print(Fore.RED + 'Unauthorized or Forbidden')
    elif response.status_code == 429:
        print(Fore.RED + 'Rate limited')

def remove_hypesquad(token):
    response = requests.delete('https://discord.com/api/v9/hypesquad/online', headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.8103.48 Mobile Safari/537.36', 'Authorization': token})
    if response.status_code == 204:
        print(Fore.GREEN + 'You have successfully removed hypesquad badge')
    elif response.status_code in (401, 403):
        print(Fore.RED + 'Unauthorized or Forbidden')
    elif response.status_code == 429:
        print(Fore.RED + 'Rate limited')

main()