import requests
URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSc9mhTWQ3CKj0dzViSA15Nqci555Z2pAXpjxKg0wT9jNU86CQ/formResponse'

form_data = {
        'entry.2112628087': '891137',
        'entry.1862114957': '36.4',
        'entry.1328967546': '無',
}

reponse = requests.post(URL, data=form_data)