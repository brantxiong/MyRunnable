# -*- coding: utf-8 -*-
import requests

response = requests.post(upload_file_url,
                         files={'filename': open(uploadfile,'rb'),
                                'description': 'upload test'})
print response.content