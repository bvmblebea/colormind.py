import requests

class ColorMind:
	def __init__(self) -> None:
		self.api = "http://colormind.io"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"
		}
	
	def get_random_color_palette(self, model: str = "default") -> dict:
		data = {
			"model": model
		}
		return requests.post(
			f"{self.api}/api/",
			data=data,
			headers=self.headers).json()
	
	def get_color_suggestions(
			self, 
			input: list,
			model: str = "default") -> dict:
		data = {
			"input": input,
			"model": model
		}
		return requests.post(
			f"{self.api}/api/",
			data=data,
			headers=self.headers).json()
	
	def get_models_list(self) -> dict:
		return requests.get(
			f"{self.api}/list/",
			headers=self.headers).json()
