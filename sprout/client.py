import requests
import json

from sprout.video import Video
from sprout.tag import Tag

class SproutClient(object):

    def __init__(self, token):
        self.token = token
        self.video = Video(self)
        self.tag = Tag(self)
        self.headers = { "SproutVideo-Api-Key": str(token) }


    def call_api(self, endpoint, method, data=None, files=None):
        """Calls the Sprout video API

        Takes in an endpoint and calls the api using requests

        Args:
            self (SproutClient): SproutClient instance
            endpoint (str): Str containg URL to call

        Returns:
            Response in JSON format
        """

        if method == "POST":
            response = requests.post(endpoint, headers=self.headers, data=data, files=files)
        elif method == "PUT":
            response = requests.put(endpoint, headers=self.headers, data=data, files=files)
        elif method == "GET":
            response = requests.get(endpoint, headers=self.headers, data=data)
        elif method == "DELETE":
            response = requests.delete(endpoint, headers=self.headers, data=data)
        else:
            raise Exception("Method not supported")

        if response.status_code != 200 and response.status_code != 201:
            raise requests.ConnectionError("Expected status code 200, but got {}".format(response.status_code))
        return_data = ""

        return response.json()
