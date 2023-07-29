import os

from dotenv import load_dotenv

from src.utils.footapi import FOOTAPI

# Load environment variables from the .env file
load_dotenv("./env/.env")

# Get the API token from the environment variables
api_token = os.getenv("API_TOKEN")


class PROCESSED:
    """A class for processing competitions using the FOOTAPI."""

    def __init__(self, config) -> None:
        """
        Initializes a new PROCESSED object.

        Parameters:
            config (dict): Configuration settings for the FOOTAPI.

        Example usage:
            config = {"param1": value1, "param2": value2}
            processed_obj = PROCESSED(config)
        """
        self.footapi = FOOTAPI(api_token, config)

    def competitions(self):
        """
        Fetches and returns the list of competitions using the FOOTAPI.

        Returns:
            list: A list of competition data.

        Example usage:
            processed_obj = PROCESSED(config)
            competition_list = processed_obj.competitions()
        """
        return self.footapi.competitions()
