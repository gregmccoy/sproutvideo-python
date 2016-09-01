# sproutvideo-python
Python wrapper from sproutvideo API

```python
from sprout.client import SproutClient

sprout = SproutClient("TOKEN")
    
# Get videos
response = sprout.video.get()


#Upload video
response = sprout.upload_video("/path/to/video.mp4", title="Title!")

#Get tags
response = sprout.tag.get()

#Create tags
response = sprout.tag.get()
    

```
