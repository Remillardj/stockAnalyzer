import configparser
import requests
import http.client
import logging

'''
	Set up fixed settings
'''
logging.basicConfig(filename="stockCurrencyTracker.log", format='%(asctime)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class cryptoCurrencyTracker(object):

	'''
		Initialize the program with basic variables, as well as obtain the configurations in the config file.
		The program requires a parameter of URL to scrap the values of 
	'''
	def __init__(self, url):
		# initialize configurations
		checkConfigurations()
		self.data = None
		self.url = url

		self.min = None
		self.max = None
		self.alert = False

		if (validateURL(self.url)):
			response = requests.post(self.url, self.data)
		else:
			error = "Failed to validate URL! Exiting program! URL: " + self.url
			writeLog("ERROR", error)
			exit()

	def writeLog(self, level, message):
		if (level == "INFO"):
			logging.info(message)
		elif (level == "DEBUG"):
			logging.debug(message)
		elif (level == "WARNING"):
			logging.warning(message)
		elif (level == "ERROR"):
			logging.error(message)
		else:
			logging.critical(message)

	def validateURL(self, url):
		try:
			http.client.HTTPConnection(url)
			return True
		except:
			return False

	def checkConfigurations(self):
		config = configparser.ConfigParser()
		config.read('config.ini')

		self.min = config['DEFAULT']['MIN']
		self.max = config['DEFAULT']['MAX']
		self.alert = config['DEFAULT']['ALERT']