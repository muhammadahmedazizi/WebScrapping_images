# This script download images from the given links

import requests
import time 



Image_links_list = ['https://upload.wikimedia.org/wikipedia/commons/e/ee/Wilcox.jpg']


def save_images (url_list):
    ind = 1
    for pic_url in url_list:
        picName = "pic" + str(ind)+".jpg"
        with open(picName, 'wb') as handle:
                

                response = requests.get(pic_url, stream=True)

                if not response.ok:
                    print (response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
                    ind = ind + 1



save_images(Image_links_list)
