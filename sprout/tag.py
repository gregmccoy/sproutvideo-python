class Tag():

    def __init__(self, client):
        self.client = client


    def get(self, id=""):
        """Calls Gets tags or single tag if an id is given

        Args:
            self (SproutClient): SproutClient instance
            id (str): id of tag to grab

        Returns:
            Response in JSON format
        """

        if id != "":
            id = id + "/"
        return self.client.call_api("https://api.sproutvideo.com/v1/tags/" + id, "GET")

    def create(self, name):
        """creates single tag

        Args:
            self (SproutClient): SproutClient instance
            name (str): name of tag to create

        Returns:
            Response in JSON format
        """
        data = { "name": name }
        return self.client.call_api("https://api.sproutvideo.com/v1/tags/", "POST", data=json.dumps(data))


    def delete(self, id):
        """Deletes single

        Args:
            self (SproutClient): SproutClient instance
            id (str): id of tag to delete

        Returns:
            Response in JSON format
        """
        return self.client.call_api("https://api.sproutvideo.com/v1/tags/" + id + "/", "DELETE")
