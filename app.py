#!/usr/local/bin/python
import requests
import openai
import configparser

class Whisperer:
    def __init__(self, engine="text-davinci-003", config_file="config.ini"):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.engine = engine
        self.persona = config["API"]["PERSONA"]
        self.api_key=config["API"]["KEY"]

    def generate_response(self, message):
        full_prompt = f"{self.prompt}\n{message}" if self.prompt 
        return self._generate_response(full_prompt)

    def _generate_response(self, prompt): 
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt
        )
