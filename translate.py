import requests
import yaml

CREDENTIALS = yaml.load(open("./credentials.yaml", "rb"),
                        Loader=yaml.FullLoader)
HEADERS = {
    'Ocp-Apim-Subscription-Key': CREDENTIALS['azure']['api_key'],
    'Content-type': 'application/json'
}


def translate_text(text):
    body = [{"Text": text}]
    url = (CREDENTIALS['azure']['api_endpoint']
            + "translator/text/v3.0/translate?api-version=3.0"
            + "&to=en")
    response = requests.post(url, headers=HEADERS, json=body)

    return response.json()[0]['translations'][0]['text']
