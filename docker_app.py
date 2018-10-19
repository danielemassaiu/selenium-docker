import os, sys, time, json, requests
from pydoc import locate
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

print('Jasmine Started')

print('Starting Browser')
# profile.set_preference("general.useragent.override", "whatever you want")
profile = webdriver.FirefoxProfile()
path = os.getcwd()
mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"

profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", path)
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.manager.focusWhenStarting", False) 
profile.set_preference("browser.download.useDownloadDir", True)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.closeWhenDone", True)
profile.set_preference("browser.download.manager.showAlertOnComplete", False)
profile.set_preference("browser.download.manager.useWindow", False)
profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
profile.set_preference("pdfjs.disabled", True)
profile.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)

driver = webdriver.Firefox(firefox_profile=profile)


driver.get('https://onetouch.traveltrust.co.uk/Login.aspx')
time.sleep(1)


# print('--------------------geckodriver.log--------------------------')
# with open('geckodriver.log', 'r') as f:
# 	print(f.read().split('\n'))
# f.close()
# print('---------------- END geckodriver.log--------------------------')

print('Stop Browser')
driver.close()
