import sys, os, shutil, requests
from kivy.base import runTouchApp
from kivy.lang import Builder
from geo import geo

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from kivy.garden.mapview import MapView

location = geo()
lat = str(location[0])
lon = str(location[1])
mac = "https://www.apple.com/hk/en/macos/images/og.jpg?201705142356"
windows = "https://yt3.ggpht.com/-osp9sQ-_FPI/AAAAAAAAAAI/AAAAAAAAAAA/cT6zVAR80XQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"
linux = "http://cyberops.in/wp-content/uploads/2017/04/linux-operating-system-cyberops-infosec.png"
generic = "https://cdn1.iconfinder.com/data/icons/rounded-flat-country-flag-collection-1/2000/_Unknown.png"
if sys.platform == "darwin":
	os_image = mac
	#desc = platform.platform()
	desc = "APPLE OS X"
elif sys.platform == "win32" or sys.platform == "cygwin":
	os_image = windows
	#desc = platform.platform()
	desc = "WINDOWS"
elif sys.platform == "linux2":
	os_image = linux
	#desc = platform.platform()
	desc = "LINUX"
else:
	os_image = generic
	desc = "Unknown OS"

root = Builder.load_string("""
#:import sys sys
#:import MapSource mapview.MapSource
MapView:
    lat: 40
    lon: -100
    zoom: 4
    map_source: MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"
    MapMarkerPopup:
        lat: %s
        lon: %s
        popup_size: dp(230), dp(130)
        Bubble:
            BoxLayout:
                orientation: "horizontal"
                padding: "5dp"
                AsyncImage:
					#Image for scroll over
                    source: "%s"
                    mipmap: True
                Label:
					#Text next to image scroll over
                    text: "%s"
                    markup: True
                    halign: "center"
""" % (lat, lon, os_image, desc))
runTouchApp(root)
shutil.rmtree("cache")
if os.path.exists("geo.pyc"):
	os.remove("geo.pyc")
