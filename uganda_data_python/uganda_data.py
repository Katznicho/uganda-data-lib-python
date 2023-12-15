# uganda_data_python/uganda_data.py
import requests

class UgandaData:
    def __init__(self, api_key):
        """
        Initializes the API client with the provided API key.

        Parameters:
            api_key (str): The API key for authenticating requests.

        Returns:
            None
        """
        self.baseurl = "https://uganda.rapharm.shop/api/uganda/data/v1"
        self.api_key = api_key
        self.headers = {
            'X-API-KEY': self.api_key,
            'Authorization': f'Bearer {self.api_key}',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def set_api_key(self, api_key):
        """
        Set the API key for authentication.

        Args:
            api_key (str): The API key to be set.

        Returns:
            None
        """
        self.api_key = api_key
        self.headers = {
            'X-API-KEY': self.api_key,
            'Authorization': f'Bearer {self.api_key}',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def fetch_data(self, url):
        """
        Fetches data from the given URL using a GET request and returns the response as a JSON object.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            dict: The response from the API as a JSON object.

        Raises:
            ValueError: If there is an error fetching data from the URL.
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error fetching data from {url}: {e}")

    def fetch_districts(self, limit=100, page=1, sort_order="asc"):
        """
        Fetches districts from the API based on the provided parameters.

        Args:
            limit (int, optional): The maximum number of districts to retrieve. Defaults to 100.
            page (int, optional): The page number of the districts to retrieve. Defaults to 1.
            sort_order (str, optional): The sort order of the retrieved districts. Defaults to "asc".

        Returns:
            dict: The fetched districts data.
        """
        url = f"{self.baseurl}/districts?limit={limit}&page={page}&sort_order={sort_order}"
        return self.fetch_data(url)

    def fetch_district(self, uuid):
        """
        Fetches the district data based on the provided UUID.

        Parameters:
            uuid (str): The UUID of the district.

        Returns:
            dict: The district data.
        """
        url = f"{self.baseurl}/district/{uuid}"
        return self.fetch_data(url)

    def fetch_district_county(self, uuid):
        """
        Fetches the district county using the given uuid.

        Parameters:
            uuid (str): The uuid of the district county.

        Returns:
            The fetched data.
        """
        url = f"{self.baseurl}/county/{uuid}"
        return self.fetch_data(url)

    def fetch_district_subcounty(self, uuid):
        """
        Fetches the district subcounty data using the provided UUID.

        :param uuid: The UUID of the subcounty.
        :type uuid: str
        :return: The fetched data.
        :rtype: dict
        """
        url = f"{self.baseurl}/subcounty/{uuid}"
        return self.fetch_data(url)

    def fetch_district_parish(self, uuid):
        """
        Fetches the district parish data based on the provided UUID.

        Parameters:
            uuid (str): The UUID of the district parish to fetch.

        Returns:
            dict: The fetched district parish data.
        """
        url = f"{self.baseurl}/parish/{uuid}"
        return self.fetch_data(url)

    def fetch_district_village(self, uuid):
        url = f"{self.baseurl}/village/{uuid}"
        return self.fetch_data(url)

    def fetch_counties(self, limit=100, page=1, sort_order="asc"):
        url = f"{self.baseurl}/counties?limit={limit}&page={page}&sort_order={sort_order}"
        return self.fetch_data(url)

    def fetch_county_subcounties(self, uuid):
        url = f"{self.baseurl}/county/{uuid}/subcounties"
        return self.fetch_data(url)

    def fetch_county_parishes(self, uuid):
        url = f"{self.baseurl}/county/{uuid}/parishes"
        return self.fetch_data(url)

    def fetch_county_villages(self, uuid):
        url = f"{self.baseurl}/county/{uuid}/villages"
        return self.fetch_data(url)

    def fetch_subcounties(self, limit=100, page=1, sort_order="asc"):
        url = f"{self.baseurl}/subcounties?limit={limit}&page={page}&sort_order={sort_order}"
        return self.fetch_data(url)

    def fetch_subcounty_parishes(self, uuid):
        url = f"{self.baseurl}/subcounty/{uuid}/parishes"
        return self.fetch_data(url)

    def fetch_subcounty_villages(self, uuid):
        url = f"{self.baseurl}/subcounty/{uuid}/villages"
        return self.fetch_data(url)

    def fetch_parishes(self, limit=100, page=1, sort_order="asc"):
        url = f"{self.baseurl}/parishes?limit={limit}&page={page}&sort_order={sort_order}"
        return self.fetch_data(url)

    def fetch_parish(self, uuid):
        url = f"{self.baseurl}/parish/{uuid}"
        return self.fetch_data(url)

    def fetch_parish_villages(self, uuid):
        url = f"{self.baseurl}/parish/{uuid}/villages"
        return self.fetch_data(url)

    def fetch_villages(self, limit=100, page=1, sort_order="asc"):
        url = f"{self.baseurl}/villages?limit={limit}&page={page}&sort_order={sort_order}"
        return self.fetch_data(url)

    def fetch_village(self, uuid):
        url = f"{self.baseurl}/village/{uuid}"
        return self.fetch_data(url)


# uganda_data_python/__init__.py
from .uganda_data import UgandaData
