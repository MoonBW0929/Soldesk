from datetime import datetime
from uuid import uuid4


class MoonFileNameGenerator:
    def generate(file_name, mode):

        type = file_name[-4:]
        file_name = file_name.replace(type, "")

        if mode == "uuid":
            uuid = str(uuid4)
            return file_name + uuid + type
        
        elif mode == "date":
            date = datetime.strftime(datetime.today(), "%Y%m%d%H%M%S")
            return file_name + date + type
