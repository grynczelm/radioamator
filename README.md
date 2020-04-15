# radioamator
Skrypt pozwala wysłać wiadomość na podany adres email, jeśli nasz znak radioamatorski zostanie zarejestrowany.

## Użycie
Skrypt jest bardzo prosty w użyciu. Elementy, które należy skonfigurować, znajdują się w górnej części skryptu. Są to:

#### 1. Adres serwera SMTP naszego dostawcy poczty:
`email_host = ''`
#### 2. Port serwera SMTP dostawcy poczty:
`email_port = 587`
#### 3. Nazwa użytkownika, zazwyczaj będzie to adres email:
`email_user = ''`
#### 4. Hasło do poczty:
`email_password = ''`
#### 5. Skąd wysłać email; standardowo 'user' jest również adresem email, stąd ta sama wartość:
`email_from = email_user`
#### 6. Docelowo wysyła na lokalną skrzynkę, warto zmienić:
`email_to = email_user`
#### 7. Jakie znaki mają być wyszukiwane:
`znaki = []`

Warto dodać skrypt do cron, aby uruchamiał się co jakiś czas.
