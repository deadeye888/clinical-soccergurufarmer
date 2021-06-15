import requests, time, yaml

class App():
	def __init__(self):
		self.frame = 0
		config_file = open("config.yml")
		config_file = yaml.load(config_file, Loader = yaml.FullLoader)
		config_file = config_file["vars"]
		authorise = config_file["authorization"]
		self.headers = {
			"authorization": authorise
		}
		self.prefix = config_file["prefix"]
		self.channel = "https://discord.com/api/v9/channels/{}/messages".format(config_file["channel"])
		self.arena = config_file["arena"]

	def run(self):
		while True:
			time.sleep(1)
			self.frame += 1
			if (self.frame % 3600 == 0):
				self.action(self.prefix + "claim")
				time.sleep(3)
				if (self.arena):
					self.action(self.prefix + "arena")
					time.sleep(1)
					self.action("1")

	def action(self, msg):
		payload = {
			"content" : msg
		}
		try:
			self.re = requests.post(self.channel, data = payload, headers = self.headers)
		except requests.exceptions.RequestException as e:
			raise SystemExit(e)

if __name__ == "__main__":
	app = App()
	app.run()