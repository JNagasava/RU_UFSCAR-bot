import urllib.request
import bs4 as bs
from datetime import datetime, timedelta

# Formata a mensagem do cardapio
# Parametro:
#   cardapio -> html do cardapio
# Retorno:
#   (str) -> mensagem formatada do cardapio
def msg(cardapio):
    refeicao = cardapio.find_all('div')
    msg = ''.join([x.text for x in refeicao[1].find_all('b')]) + '\n'
    for item in refeicao[2::]:
        msg = msg + item.b.text + item.span.text + '\n'
    return msg

# Cardapio do proximo RU
# Retorno:
#   (str) -> cardapio do proximo RU em HTML
def proximo():
    now = datetime.now()
    start = now.replace(hour = 13, minute = 30)
    end = now.replace(hour = 19, minute = 0)
    if start <= now and now <= end:
        return jantar()
    elif now > end:
        return amanha()[0]
    else:
        return almoco()

# Cardapio de amanha(almoco e janta) no formato HTML
# Retorno:
#   (str) -> cardapio de amanha em HTML
def amanha():
    amanha = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
    site_ru = urllib.request.urlopen('https://www2.ufscar.br/restaurantes-universitario/cardapio')
    soup = bs.BeautifulSoup(site_ru, 'html.parser')
    cardapio_amanha = list()
    for cardapio in soup.find_all('div', {'class': 'col-lg-7 metade periodo'}):
        if amanha == cardapio.find('div', {'class':'cardapio_titulo'}).b.text:
            cardapio_amanha.append(cardapio)
    return cardapio_amanha

# Cardapio de hoje(almoco e janta) no formato HTML
# Retorno:
#   (str) -> cardapio de hoje em HTML
def hoje():
    hoje = datetime.now().strftime("%d/%m/%Y")
    site_ru = urllib.request.urlopen('https://www2.ufscar.br/restaurantes-universitario/cardapio')
    soup = bs.BeautifulSoup(site_ru, 'html.parser')
    cardapio_hoje = list()
    for cardapio in soup.find_all('div', {'class': 'col-lg-7 metade periodo'}):
        if hoje == cardapio.find('div', {'class':'cardapio_titulo'}).b.text:
            cardapio_hoje.append(cardapio)
    return cardapio_hoje

# Cardapio do almoco de hoje no formato HTML
# Retorno:
#   (str) -> cardapio do almoco de hoje em HTML
def almoco():
    hoje = datetime.now().strftime("%d/%m/%Y")
    site_ru = urllib.request.urlopen('https://www2.ufscar.br/restaurantes-universitario/cardapio')
    soup = bs.BeautifulSoup(site_ru, 'html.parser')
    for cardapio in soup.find_all('div', {'class': 'col-lg-7 metade periodo'}):
        horario = cardapio.find('div', {'class':'cardapio_titulo'}).find_all('b')[-1].text
        data = cardapio.find('div', {'class':'cardapio_titulo'}).find_all('b')[0].text
        if hoje == data and 'ALMOÇO' == horario:
            cardapio_almoco = cardapio
            break
    return cardapio_almoco

# Cardapio da janta de hoje no formato HTML
# Retorno:
#   (str) -> cardapio da janta de hoje em HTML
def jantar():
    hoje = datetime.now().strftime("%d/%m/%Y")
    site_ru = urllib.request.urlopen('https://www2.ufscar.br/restaurantes-universitario/cardapio')
    soup = bs.BeautifulSoup(site_ru, 'html.parser')
    for cardapio in soup.find_all('div', {'class': 'col-lg-7 metade periodo'}):
        horario = cardapio.find('div', {'class':'cardapio_titulo'}).find_all('b')[-1].text
        data = cardapio.find('div', {'class':'cardapio_titulo'}).find_all('b')[0].text
        if hoje == data and 'JANTAR' == horario:
            cardapio_jantar = cardapio
            break
    return cardapio_jantar