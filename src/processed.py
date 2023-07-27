import os

from dotenv import load_dotenv

from src.utils.footapi import FOOTAPI

load_dotenv("./env/.env")
api_token = os.getenv("API_TOKEN")


class PROCESSED:
    def __init__(self, config) -> None:
        self.footapi = FOOTAPI(api_token, config)

    def competitions(self):
        return self.footapi.competitions()
