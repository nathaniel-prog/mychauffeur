import pygeoip
import requests


my_ip_adress= requests.get('https://api.ipify.org').txt



gip= pygeoip.GeoIP('GeoLiteCity.dat')
res= gip.record_by_addr('77.138.204.33')
for key, val in res.items():
	print('%s : %s' % (key,val))