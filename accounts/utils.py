from django.conf import settings
import base64
import requests

key=settings.IMHOST
def UploadImage(file,name):
    data={
            "key":key,
            "image":base64.b64encode(file),
            "name":name
        }
    resp= requests.post("https://api.imgbb.com/1/upload",data=data)
    # Perform Error Handling here
    return resp.json()['data']['url']
