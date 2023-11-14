def getUsdRate():
    import requests
    import xml.etree.ElementTree as ET

    data = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?numcode=051').content
    tree = ET.ElementTree(ET.fromstring(data))
    rate = float(tree.getroot().findall('.//Valute[CharCode="USD"]/VunitRate')[0].text.replace(',','.'))
    return rate

print(getUsdRate())