import requests


class FOOTAPI:
    """
    A class to interact with the FOOTAPI.

    Parameters:
        API_TOKEN (str): The API token required for authentication.
        config (dict): Configuration settings for the API.

    Example usage:
        config = {
            "BASE_URL": "https://api.example.com",
            "COMPETITIONS_URL": "/competitions",
        }
        api_token = "your_api_token_here"
        footapi = FOOTAPI(api_token, config)
    """

    def __init__(self, API_TOKEN, config) -> None:
        self.base_url = config["BASE_URL"]
        self.COMPETITIONS_URL = config["COMPETITIONS_URL"]

        self.API_TOKEN = API_TOKEN
        self.headers = {"X-Auth-Token": self.API_TOKEN}
        self.status = requests.get(
            self.base_url + config["COMPETITIONS_URL"], headers=self.headers
        ).status_code
        self._auth = self.status == 200

    def authentification(funct):
        def wrapped(self, *args, **kwargs):
            """
            A decorator to ensure that the method is called only if authenticated.

            Raises:
                Exception: If the user is not authenticated.

            Returns:
                The result of the wrapped function if authenticated.

            Example usage:
                @authentification
                def some_method(self, *args, **kwargs):
                    # Method logic here
            """
            if not self._auth:
                raise Exception("You must be authenticated to use this method")
            else:
                return funct(self, *args, **kwargs)

        return wrapped

    @authentification
    def competitions(self):
        """
        Fetches and returns the competitions data from the FOOTAPI.

        Returns:
            dict: A dictionary containing the competitions data.

        Example usage:
            competitions_data = footapi.competitions()
        """
        try:
            response = requests.get(
                self.base_url + self.COMPETITIONS_URL, headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return {}
