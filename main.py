import os
from art import tprint
import browsers

dict_of_browsers = browsers.browsers()
list_of_browsers = tuple(dict_of_browsers)

URLS = {
    'telegram': 'https://web.telegram.org',
    'git': 'https://github.com',
    'vk': 'https://vk.com',
}


def main():
    tprint('Welcome', font='sub-zero')

    for idx, browser in enumerate(list_of_browsers, start=1):
        print(f"{idx} - {browser['display_name']}")
    print('0 - Leave')

    browser = int(input('\nChoose your browser >> '))

    if not browser:
        tprint('Goodbye', font='sub-zero')

    else:
        tprint('Running', font='sub-zero')
        path = list_of_browsers[browser - 1]['path']
        os.system(f"""\"{path}" -incognito {URLS['git']} {URLS['telegram']} {URLS['vk']} """)


if __name__ == '__main__':
    main()
    input('Press any key to leave')
