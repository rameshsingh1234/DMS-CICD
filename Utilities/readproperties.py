import configparser
import os
import csv


class ReadConfig:
    config_file = os.path.join(os.path.dirname(__file__), '../Configuration/config.init')

    @staticmethod
    def get_config():
        config = configparser.ConfigParser()
        if os.path.exists(ReadConfig.config_file):
            config.read(ReadConfig.config_file)
        else:
            raise FileNotFoundError(f"Configuration file not found: {ReadConfig.config_file}")
        return config

    @staticmethod
    def get_logs_directory():
        config = ReadConfig.get_config()
        try:
            return config['DEFAULT']['LogsDirectory']
        except KeyError:
            raise KeyError("LogsDirectory key is missing in the configuration file.")

    @staticmethod
    def get_auth_url():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_url']
        except KeyError:
            raise KeyError("auth_url key is missing in the authorization section of the configuration file.")

    @staticmethod
    def get_auth_method():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_method']
        except KeyError:
            raise KeyError("auth_method key is missing in the authorization section of the configuration file.")

    @staticmethod
    def get_auth_headers():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_headers']
        except KeyError:
            raise KeyError("auth_headers key is missing in the authorization section of the configuration file.")

    @staticmethod
    def get_auth_payload():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_payload']
        except KeyError:
            raise KeyError("auth_payload key is missing in the authorization section of the configuration file.")

    @staticmethod
    def get_csv_file_path():
        config = ReadConfig.get_config()
        try:
            return config['DEFAULT']['CSVFilePath']
        except KeyError:
            raise KeyError("CSVFilePath key is missing in the configuration file.")

    @staticmethod
    def get_base_url():
        config = ReadConfig.get_config()
        try:
            return config['DEFAULT']['Base_url']
        except KeyError:
            raise KeyError("Base_url key is missing in the configuration file.")

    @staticmethod
    def read_csv(file_path):
        if os.path.exists(file_path):
            with open(file_path, mode='r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                data = [row for row in csv_reader]
            return data
        else:
            raise FileNotFoundError(f"CSV file not found: {file_path}")
