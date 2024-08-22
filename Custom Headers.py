#Custom Headers :-

import requests

url = "https://stox.com" #url of site

h = {'User-Agent':'https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent&ved=2ahUKEwjD0rH8zsuGAxXWS2cHHbc3IlwQFnoECB0QAQ&usg=AOvVaw2dRS9NPbH5DaKo_dFAL1ks'}       #header (User-Agent-: get my valid useragent)

#allow_redirects will allows if website will redirect to any different site
data = requests.get(url, headers=h,allow_redirects=True, timeout=10)

print(data.status_code)
