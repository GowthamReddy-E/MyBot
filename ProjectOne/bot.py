from webex_bot.webex_bot import WebexBot
from weather import WeatherByZIP

api_token = "NzViYmY1M2EtOTIwOC00MTM2LWJmZGQtOGI3MTQwMzE3MWRjNTJkZWE1MTUtYzM2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

bot = WebexBot(api_token, approved_domains=["0x2142.com"])

bot.add_command(WeatherByZIP())

bot.run()
