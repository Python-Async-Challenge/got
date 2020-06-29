import src.settings as settings

import requests_async as request


class BaseClient:
    def __init__(self, ms_name, version='v1'):
        self.BASE_URL = f'http://{ms_name}:8000/{ms_name}/{version}/{ms_name}/'

    async def get_list(self):
        response = await request.get(self.BASE_URL)
        return response.json()