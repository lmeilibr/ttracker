import requests
import os
import json

API_URL = "https://api.scryfall.com"


class MtgClient:

    def __init__(self, root_folder=None):
        self.root_folder = root_folder

    def get_by_arena_id(self, arena_id):
        url = API_URL + f"/cards/arena/{arena_id}"
        result = requests.get(url)

        if self.root_folder:
            if os.path.exists(self.root_folder):
                self.download(result)
        return result.json()

    def download(self, result):
        obj = result.json()
        arena_id = str(obj['arena_id'])
        try:
            png_url = obj['image_uris']['png']
        except:
            raise

        download_path = os.path.join(self.root_folder, arena_id)

        # Skip if already exists
        if os.path.exists(download_path):
            return

        os.makedirs(os.path.join(self.root_folder, arena_id))
        json_filename = f'{arena_id}.json'
        png_filename = f'{arena_id}.png'

        with open(os.path.join(download_path, json_filename),
                  'w') as js_handle:
            json.dump(result.json(), js_handle)

        with open(os.path.join(download_path, png_filename), 'wb') as handle:
            response = requests.get(png_url, stream=True)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

            print('saved file')
