<p align="center">
<img src="./smtp-view-1.png" width="600" height="310">
</p>

# smtp-checker
smtp checker tool 
this tool can work as will (Cli/Gui)

For (Windows/Linux)

`no` more info it's clean code :]
# API
```python
import requests

def check(mail):
    url = "https://validateemailaddress.org/"
    payload="email="+mail.replace("@","%40")
    headers = {
        'User-Agent': 'Mozilla/5.0 ',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '26',
        'Origin': 'https://validateemailaddress.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://validateemailaddress.org/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-GPC': '1'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.text
```

# screens
<img src="./Smtp-view.png">
<img src="./smtp-view-2.png">
<img src="./smtp-view-3.png">
