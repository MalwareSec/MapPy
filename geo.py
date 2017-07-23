import requests
import json

# Automatically geolocate the connecting IP
def geo():
	f = requests.get('http://freegeoip.net/json/')
	location = f.json()
	#print(location)
	lat = location['latitude']
	lon = location['longitude']
	return lat, lon

if __name__ == "__main__":
	geo()
