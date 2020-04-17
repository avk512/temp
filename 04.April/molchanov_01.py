import requests
from bs4 import BeautifulSoup


def get_html(url):
    resp = requests.get(url)
    return resp.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    # return h1
    p = soup.find('header', id='masthead').find('p', 'site-description').text
    return p


def main():
    # url = 'https://wordpress.org/'
    url = 'https://ru.wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
