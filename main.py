import yaml
from portkey_ai import Portkey

with open('assets/credentials.yml') as cred_file:
    creds = yaml.safe_load(cred_file)

PORTKEY_API_KEY = creds['portkey_api_key']
PORTKEY_VIRTUAL_KEY = creds['portkey_virtual_key']

pk_gateway = Portkey(
    api_key = PORTKEY_API_KEY,
    virtual_key = PORTKEY_VIRTUAL_KEY
)

response = pk_gateway.chat.completions.create(
    messages = [
        {
            'role': 'user',
            'content': 'Strictly refer to https://portkey.ai/ to tell me concisely what portkey does'
        }
    ],
    model = 'gemini-pro'
)

print(response.choices[0].message.content)