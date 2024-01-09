import os
import sys

import browsers
from cfonts import render

dict_of_browsers = browsers.browsers()
list_of_browsers = tuple(dict_of_browsers)

URLS = {
    'telegram': 'https://web.telegram.org',
    'git': 'https://github.com',
    'vk': 'https://vk.com',
}


def main():
    print(render('Welcome', colors=['green', 'gray'], align='left'))

    for idx, browser in enumerate(list_of_browsers, start=1):
        print(f"{idx} - {browser['display_name']}")
    print('0 - Leave')

    browser = int(input('\nChoose your browser >> '))

    if not browser:
        print(render('Goodbye', colors=['green', 'gray'], align='left'))

    else:
        print(render('Running', colors=['green', 'gray'], align='left'))
        path = list_of_browsers[browser - 1]['path']
        os.system(f"""\"{path}" -incognito {URLS['git']} {URLS['telegram']} {URLS['vk']} """)


if __name__ == '__main__':
    main()
