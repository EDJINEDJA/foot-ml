import requests


class FOOTAPI:
    def __init__(self, API_TOKEN, config) -> None:
        self.base_url = config["BASE_URL"]
        self.COMPETITIONS_URL = config["COMPETITIONS_URL"]

        self.API_TOKEN = API_TOKEN
        self.headers = {"X-Auth-Token": self.API_TOKEN}
        self.status = requests.get(
            config["COMPETITIONS_URL"], headers=self.headers
        ).status_code
        self._auth = self.status == 200

    def authentification(funct):
        def wrapped(self, *args, **kwargs):
            if not self._auth:
                raise Exception("You must be authenticated to use this method")
            else:
                return funct(self, *args, **kwargs)

        return wrapped

    @authentification
    def competitions(self):
        try:
            response = requests.get(self.COMPETITIONS_URL, self.headers)
            print(response)
        except Exception as e:
            print(f"An error occur: {e}")
