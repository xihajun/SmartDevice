# This is just a test

import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()

# Shut down discovery
pychromecast.discovery.stop_discovery(browser)







print("done")
