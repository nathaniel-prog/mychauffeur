import requests
from urllib.parse import urlencode



api_key= 'AIzaSyBZm0yJKUnuSD9prSp2MvKctcw45GXZ__g'

url_base_endpoint=f'https://www.googleapis.com/geolocation/v1/geolocate/json'

req= requests.get(url_base_endpoint)

r= req.status_code

print(r)


def extract_lat_lng():
	endpoint=f'https://maps.googleapis.com/geolocation/v1/geolocate'
	params={ 'key': api_key}
	url_param= urlencode(params)
	urll=f'{endpoint}?{url_param}'
	r= requests.get(urll)
	w= r.json()["wifiAccessPoints"]
	if w.status_code not in range(200,299):
		return {}
	else:
		return w.json()


print(extract_lat_lng())






