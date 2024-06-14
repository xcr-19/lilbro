import requests
import random

class Quotes():
    def __init__(self) -> None:
        self.url = 'https://api.quotable.io/quotes?tags='

    def get_quote(self, type: str):
        response = requests.get(f'{self.url}{type}')
        if response.status_code != 200:
            return "Unfortunatly, I couldn't get the quote you where looking for. Take the hint 😉"
        else:
            jresp = response.json()
            quote_count = jresp.get('count')
            if quote_count == 0:
                return "I couldn't find any quotes for the type you requested. Try another type 😅"
            else:
                quote = random.choice(jresp.get('results'))
                return f"{quote.get('content')} - {quote.get('author')}"
            