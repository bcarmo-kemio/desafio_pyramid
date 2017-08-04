import requests
import static
import json


class DesafioAPI:
    @staticmethod
    def do_request(quote_number=""):
        url = static.BASE_API_URL
        if quote_number:
            url += quote_number

        r = requests.get(url)
        if r.ok:
            return json.loads(r.text)
        else:
            r.raise_for_status()
