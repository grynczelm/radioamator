import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import path
import sys


# KONFIGURACJA
email_host = '' # Adres serwera SMTP naszego dostawcy poczty
email_port = 587 # Port serwera SMTP dostawcy poczty
email_user = '' # Nazwa użytkownika, zazwyczaj będzie to adres email
email_password = '' # Hasło do poczty
"""
email_from - skąd wysłać email; standardowo 'user' jest również adresem email,
            stąd ta sama wartość
email_to - docelowo wysyła na lokalną skrzynkę, warto zmienić
"""
email_from = email_user 
email_to = email_user

znaki = [] # np. ['SP2AB', 'SP4QWX', 'SP5XYZ']

"""
KONIEC KONFIGURACJI
DALEJ NIC NIE TRZEBA ZMIENIAĆ 
"""

if len(znaki) < 1:
    sys.exit("Najpierw podaj chociaż jeden znak")

if path.exists('.amator_exists'):
    sys.exit("Znak został już znaleziony, zatrzymuję działanie")

adres = 'https://amator.uke.gov.pl/pl/individuals.json?columns[0][data]=id&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=number&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=valid_to&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=call_sign&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=category&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=transmitter_power&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=station_location&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&order[0][column]=1&order[0][dir]=asc&start=0&length=10&search[regex]=false&search[value]='

lista = []

for znak in znaki:
    response = requests.get(adres+znak).json()
    ilosc = response['recordsFiltered']
    dane = response['data']
    
    if ilosc != 0:
        lista.append(str(znak))

if len(lista) > 0:
    try:
        open('.amator_exists', 'w').close()
    except:
        sys.exit('Nie udało się utworzyć pliku kontrolnego, który hamuje działanie skryptu w przypadku znalezienia znaku. Nie wysyłam maila ze względu na możliwość klasyfikacji jako spam.')

    server = smtplib.SMTP(host=email_host, port=email_port)
    server.starttls()
    server.login(email_user, email_password)

    message = 'Wygląda na to, że jeden z Twoich znaków został zarejestrowany! :: ' + ", ".join(lista)

    msg = MIMEMultipart()

    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = 'Zarejestrowano znak amatorski!'

    msg.attach(MIMEText(message, 'plain'))

    server.send_message(msg)
    del msg

