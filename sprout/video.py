class Video():

    def __init__(self, client):
        self.client = client

    def get(self, id=""):
        """Calls Gets videos or single video if an id is given

        Args:
            self (SproutClient): SproutClient instance
            id (str): id of video to grab

        Returns:
            Response in JSON format
        """

        if id != "":
            id = id + "/"
        return self.client.call_api("https://api.sproutvideo.com/v1/videos/" + id, "GET")

    def upload(self, source, title="", description="", privacy="", password="",  \
            prefers_embed_password="", tags="", tag_names="", notification_url="", \
            requires_signed_embeds="", embedded_url="", token=""):
        """ Uploads videos with the specified settings

        Args:
            self (SproutClient): SproutClient instance
            title (str): Title of video
            description (str): description of video
            privacy (str): level of video privacy 0-4
            password (str): Password for video
            prefers_embed_password (str): require password for video
            tags (str): tag id's
            tag_names (str): create new tags with the given names
            notification_url (str): url for postback
            requires_signed_embeds (str): indicates if signed embed codes are required
            embedded_url (str): embed url
            token (str): token from upload token request
       """

        data = {
            "title": title,
            "description": description,
            "privacy": privacy,
            "password": password,
            "prefers_embed_password": prefers_embed_password,
            "tags": tags,
            "tag_names": tag_names,
            "notification_url": notification_url,
            "requires_signed_embeds": requires_signed_embeds,
            "embedded_url": embedded_url,
            "token": token,
        }

        for key in list(data.keys()):
            if data[key] == "":
                del data[key]

        try:
            files = { "source_video": open(source, 'rb') }
        except:
            return "Couldn't read Video file"

        return self.client.call_api("https://api.sproutvideo.com/v1/videos", "POST", data=data, files=files)


    def poster_frame(self, id, image):
        """ Uploads a images and sets a video to use it as a poster image

        Args:
            self (SproutClient): SproutClient instance
            id (str): id of video
            image (str): location of the image file

        Returns:
            Response in JSON format
        """
        try:
            files = { "custom_poster_frame": open(image, 'rb') }
        except:
            return "Couldn't read Image file"
        return self.client.call_api("https://api.sproutvideo.com/v1/videos/" + id, "PUT", files=files)

    def delete(self, id):
        """Deletes single video

        Args:
            self (SproutClient): SproutClient instance
            id (str): id of video to delete

        Returns:
            Response in JSON format
        """
        return self.client.call_api("https://api.sproutvideo.com/v1/videos/" + id + "/", "DELETE")
