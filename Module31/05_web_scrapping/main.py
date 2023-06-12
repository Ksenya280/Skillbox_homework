import requests
import re
def get_h3_tags(url):
    response = requests.get(url)
    html = response.text
    h3_tags = re.findall(r'<h3.*?>(.*?)</h3>', html, re.IGNORECASE)
    h3_text = [re.sub(r'<.*?>', '', tag).strip() for tag in h3_tags]

    return h3_text


url = 'http://www.columbia.edu/~fdc/sample.html'
h3_tags = get_h3_tags(url)
print(h3_tags)