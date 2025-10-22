import logging
import requests



class APIClient:
    def __init__(self, base_url, timeout = 10, api_key = None):
        self.base_url =base_url.lstrip('/')
        self.timeout = timeout
        self.session = requests.session()
        self.session.headers.update({
            "content-type": "application/json"
        })

        if api_key:
            self.session.headers.update({
                "x-api-key": api_key
            })

        #Basic Logging Configuration
        logging.basicConfig(
            level = logging.INFO,
            format = "%(asctime)s - %(levelname)s - %(message)s"
        )

        self.logger = logging.getLogger(__name__)

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"{method.upper()} -> {url} ")
        print(f"{self.base_url}/{endpoint.lstrip('/')}")
        try:
            response = self.session.request(
                method = method,
                url = url, 
                timeout = self.timeout,
                **kwargs
            )
            self.logger.info(f"Response Status: {response.status_code}")
            return response
        
        except requests.RequestException as e:
            self.logger.error(f"Request failed with: {e}")
            raise
    
    def get(self, endpoint,  **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)
    
    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

    