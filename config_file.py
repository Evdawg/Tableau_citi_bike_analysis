import configparser
from configparser import ConfigParser
import pathlib

# This does not include writing new config files, only reading existing.
# Don't forget to "import config_file" in python code.

#-----------------------------------------------------------------------------------------------------------------------
### source code is from: https://www.c-sharpcorner.com/article/configuration-files-in-python/#:~:text=Config%20files%20are%20used%20to,at%20some%20point%2C%20of%20time.
### this site also explains how to write a new config file including how to add new config entry formats!

def read_config():
    config = configparser.ConfigParser()
    conf_file_path = pathlib.Path(__file__).parent.absolute().joinpath('config.ini')
    print('Parsing: ' + str(conf_file_path))
    config.read(conf_file_path)
    return config
# read_config()