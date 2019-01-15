#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests 
url = 'https://galaxy-manager.fr/_ajax/snips.php'
payload = {"intentMessage": intentMessage, 'conf' : conf}
headers = {'Content-type': 'application/json'}
res = requests.post(url, data=payload, headers=headers)

