import requests
import dotenv
import os
from NapariliDV import settings
from loguru import logger


dotenv.load_dotenv()


class AmoCRM: 
    def __init__(self, subdomain: str, client_id: str, client_secret: str, redirect_uri: str): 
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri
        self.SUBDOMAIN = subdomain
        self.CLIENT_DOMAIN = f'https://{self.SUBDOMAIN}.amocrm.ru/'

        self.access_token_path = os.path.join(settings.BASE_DIR, 'amocrm_tokens', 'access_token.txt')
        self.refresh_token_path = os.path.join(settings.BASE_DIR, 'amocrm_tokens', 'refresh_token.txt')

    def get_initial_tokens(self, authorization_code: str) -> None: 
        url = f'{self.CLIENT_DOMAIN}oauth2/access_token'
        data = {
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': self.REDIRECT_URI
        }
        response = requests.post(url, data=data)

        if response.status_code == 200: 
            access_token = response.json()['access_token']
            refresh_token = response.json()['refresh_token']

            logger.info(f'Acess token получен')
            logger.info(f'Refresh token получен')

            with open(self.access_token_path, 'w', encoding='utf-8') as file: 
                file.write(access_token)
            with open(self.refresh_token_path, 'w', encoding='utf-8') as file: 
                file.write(refresh_token)
        else: 
            print(response.json())
            logger.error(f'Ошибка получения токенов. Код {response.status_code}') 

    def refresh_tokens(self, ) -> None: 
        url = f'{self.CLIENT_DOMAIN}oauth2/access_token'
        data = {
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'refresh_token': self.get_current_refresh_token(),
            'redirect_uri': self.REDIRECT_URI
        }
        response = requests.post(url, data=data)

        if response.status_code == 200: 
            access_token = response.json()['access_token']
            refresh_token = response.json()['refresh_token']

            logger.info(f'Access token обновлён')
            logger.info(f'Refresh token обновлён')

            with open(self.access_token_path, 'w', encoding='utf-8') as file: 
                file.write(access_token)
            with open(self.refresh_token_path, 'w', encoding='utf-8') as file: 
                file.write(refresh_token)
        else: 
            logger.error(f'Ошибка обновления токенов. Код {response.status_code}\n{response.text}') 

    def create_lead(
            self, 
            name: str
        ) -> int: 
        url = f'{self.CLIENT_DOMAIN}api/v4/leads'
        data = [{
            'name': name,
            'created_by': 0,
        }]

        headers = {
            'Authorization': f'Bearer {self.get_current_access_token()}'
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200: 
            logger.info(f'Сделка "{name}" создана!')
            return response.json()['_embedded']['leads'][0]['id']
        else: 
            logger.error(f'Ошибка создания сделки. Код {response.status_code}\n{response.text}') 

    def get_current_access_token(self) -> str | None: 
        with open(self.access_token_path, 'r', encoding='utf-8') as file: 
            access_token = file.read() 
        return access_token
    
    def get_current_refresh_token(self) -> str | None: 
        with open(self.refresh_token_path, 'r', encoding='utf-8') as file: 
            refresh_token = file.read() 
        return refresh_token


crm = AmoCRM(
    subdomain=os.getenv('AMOCRM_SUBDOMAIN'), 
    client_id=os.getenv('AMOCRM_CLIENT_ID'), 
    client_secret=os.getenv('AMOCRM_CLIENT_SECRET'), 
    redirect_uri=os.getenv('AMOCRM_REDIRECT_URL')
)