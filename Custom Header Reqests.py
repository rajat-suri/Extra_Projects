#............Custom Headers send Request on Webhook Site .........#

import requests

url = "https://webhook.site/a7d47df1-0153-4449-b8c3-570f300e665e" #url of site

h = {'User-Agent':'Mysterice'}       #header (User-Agent-: Search on google get my valid useragent and get it.)

#allow_redirects will allows if website will redirect to any different site
data = requests.get(url, headers=h, timeout=10)

print(data.status_code)
