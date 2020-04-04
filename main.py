from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
from utils import *
import config
import time

def main():
    previous_time = ''
    with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        while True:
            if not previous_time == get_current_time():
                current_time = get_current_time()
                previous_time = current_time
                generate_image(current_time)
                image = client.upload_file('time_image.jpg')
                client(UploadProfilePhotoRequest(image))
                p = client.get_profile_photos('me')[1]
                client(DeletePhotosRequest(id = [InputPhoto(id = p.id, access_hash = p.access_hash, file_reference = p.file_reference)]))
                time.sleep(1)

if __name__ == '__main__':
    main()
