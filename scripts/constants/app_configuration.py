import configparser

__config__ = configparser.ConfigParser()
__config__.read("conf/application.conf")

session = 'LOG'

log_level = __config__.get('LOG', 'log_level')
basepath = __config__.get('LOG', 'basepath')
file_name = __config__.get('LOG', 'file_name')
file_name_json = __config__.get('LOG', 'file_name_json')
