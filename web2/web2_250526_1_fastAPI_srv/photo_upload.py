from uuid import uuid4
from fastapi import Form
from fastapi.responses import FileResponse


class Photo_upload:

    def __init__(self):
        self.dir = "./photo/"

    async def upload(self, title, photo):

        file = await photo.read()
        file_name = photo.filename
        type = photo.filename[-4:]
        file_name = photo.filename.replace(type, "")
        file_name += str(uuid4()) + type

        f = open(self.dir + file_name, "wb")
        f.write(file)
        f.close()

        return {"title": title, "photo": file_name}
    
    def download(self, photo):
        return FileResponse(self.dir + photo, filename=photo)