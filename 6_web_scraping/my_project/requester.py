user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"
)


class Requester:
    def __init__(self):
        self.__requests_tries = 3
        self.timeout = 15
        self.__init_session()

    def __init_session(self):
        """
        Initializes a session object for making requests.

        Returns:
            requests.Session: The session object.

        """
        self.session = requests.Session()

    def get_requests(self, url, headers, proxy=None):
        """
        Sends a GET request to the specified URL using the provided session, headers, and proxy.

        Args:
            session (requests.Session): The session object to use for making the request.
            url (str): The URL to send the request to.
            headers (dict): The headers to include in the request.
            proxy (dict, optional): The proxy to use for the request. Defaults to None.

        Returns:
            requests.Response or None: The response object if the request is successful (status code 200),
            otherwise None.

        Raises:
            requests.exceptions.RequestException: If an error occurs while making the request.
            requests.exceptions.Timeout: If the request times out.

        """
        for _ in range(self.__requests_tries):
            try:
                response = self.session.get(
                    url, headers=headers, proxies=proxy, timeout=self.timeout
                )
                if response.status_code == 200:
                    return response
            except requests.exceptions.RequestException as e:
                print(e)
            except requests.exceptions.Timeout as e:
                print(e)
        return None

    def post_requests(url, headers, data=None, proxy=None):
        """
        Sends a POST request to the specified URL with the given headers, data, and proxy.

        Parameters:
        url (str): The URL to send the POST request to.
        headers (dict): The headers to include in the request.
        data (dict, optional): The data to include in the request body. Defaults to None.
        proxy (dict, optional): The proxy to use for the request. Defaults to None.

        Returns:
        response (requests.Response): The response object if the request is successful and the status code is 200.
        None: If the request fails or the status code is not 200.
        """
        for _ in range(self.__requests_tries):
            try:
                response = self.session.post(
                    url, headers=headers, data=data, proxies=proxy
                )
                if response.status_code == 200:
                    return response
            except requests.exceptions.RequestException as e:
                print(e)
            except requests.exceptions.Timeout as e:
                print(e)
        return None


url_home = "https://century21mexico.com/v/resultados?json=true"
headers_home = {
    "Host": "century21mexico.com",
    "User-Agent": user_agent,
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://century21mexico.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
}
headers_casa = {
    "Host": "century21mexico.com",
    "User-Agent": user_agent,
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://century21mexico.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
}

req = Requester()
req.session.cookies
response = req.get_requests(url_home, headers_home)
