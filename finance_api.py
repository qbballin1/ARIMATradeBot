import json

from urllib.request import urlopen



def get_jsonparsed_data (url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")

    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?apikey=demo")
print(get_jsonparsed_data(url))
