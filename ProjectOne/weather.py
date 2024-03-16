from webex_bot.models.command import Command
import logging

log = logging.getLogger(__name__)

class WeatherByZIP(Command):
    def __init__(self):
        super().__init__(
            command_keyword="weather",
            help_message="Get current weather conditions by ZIP code.",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        return f"Got the message: {message}"
