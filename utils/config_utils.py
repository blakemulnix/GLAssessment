import configparser
import os


config = configparser.RawConfigParser()
config.read('./environment.properties')


print(config.sections())

def get_base_url():
    return config.get('Network', 'baseurl')