# -*- coding: utf-8 -*-

import pyshorteners
import requests

def short(lien):
    try :
        res = pyshorteners.Shortener().tinyurl.short(lien)
        return res
    except Exception:
        try:
            base_url = 'http://tinyurl.com/api-create.php?url='
            url = base_url + lien
            r = requests.get(url)
            return r.text
        except Exception:
            try:
                api_key = "421e2f330de08755cf6e6a866e0ea1e3d10b1"
                url = lien
                api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
                data = requests.get(api_url).json()["url"]
                if data["status"] == 7:
                    shortened_url = data["shortLink"]
                    return shortened_url
            except Exception:
                try:
                    username = "o_1q16v1a5hu"
                    password = "G@briel@dkn2002"
                    auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
                    if auth_res.status_code == 200:
                        access_token = auth_res.content.decode()
                    headers = {"Authorization": f"Bearer {access_token}"}
                    groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
                    if groups_res.status_code == 200:
                        groups_data = groups_res.json()['groups'][0]
                        guid = groups_data['guid']
                    url = lien
                    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
                    if shorten_res.status_code == 200:
                        link = shorten_res.json().get("link")
                    return link
                except Exception:
                    return lien



# lien = "https://agridigitale.net/art-un_nouveau_concours_d_entre_dans_l_agriculture_au_togo_.html"
# print(short(lien))

