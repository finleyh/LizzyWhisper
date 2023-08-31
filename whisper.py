#!/usr/local/bin/python
import requests
import openai
import configparser

class Whisperer:
    def __init__(self, engine="text-davinci-003", config_file="config.ini"):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.engine = engine
        self.persona = config["API"]["PERSONA"].strip()
        openai.api_key=config["API"]["KEY"].strip()

    def generate_response(self, message):
        full_prompt = f"{self.persona}\n{message}" 
        return self._generate_response(full_prompt)

    def _generate_response(self, prompt, max_tokens=2048):
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text
