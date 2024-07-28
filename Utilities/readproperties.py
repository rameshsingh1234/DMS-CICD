import configparser
import os
import logging

class ReadConfig:
    @staticmethod
    def get_config_path():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '../Configuration/config.init'))

    @staticmethod
    def get_config():
        config_path = ReadConfig.get_config_path()
        logging.info(f"Reading config file from: {config_path}")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        config = configparser.ConfigParser()
        config.read(config_path)
        return config

    @staticmethod
    def get_username():
        config = ReadConfig.get_config()
        return config.get('EMAIL', 'username')

    @staticmethod
    def get_password():
        config = ReadConfig.get_config()
        return config.get('EMAIL', 'password')

    @staticmethod
    def get_recipient_email():
        config = ReadConfig.get_config()
        return config.get('EMAIL', 'recipient_email')

    @staticmethod
    def get_logs_directory():
        config = ReadConfig.get_config()
        try:
            logs_directory = config['DEFAULT']['LogsDirectory']
            return os.path.abspath(os.path.join(os.path.dirname(ReadConfig.get_config_path()), logs_directory))
        except KeyError:
            raise KeyError("LogsDirectory key is missing in the configuration file")

    @staticmethod
    def get_csv_file_path():
        config = ReadConfig.get_config()
        try:
            csv_file_path = config['DEFAULT']['CSVFilePath']
            return os.path.abspath(os.path.join(os.path.dirname(ReadConfig.get_config_path()), csv_file_path))
        except KeyError:
            raise KeyError("CSVFilePath key is missing in the configuration file")

    @staticmethod
    def read_csv(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = [row for row in csv_reader]
        return data

    @staticmethod
    def get_base_url():
        config = ReadConfig.get_config()
        try:
            base_url = config['DEFAULT']['Base_url']
            return base_url
        except KeyError:
            raise KeyError("Base_url key is missing in the configuration file")

    @staticmethod
    def get_auth_url():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_url']
        except KeyError:
            raise KeyError("auth_url key is missing in the authorization section of the configuration file")

    @staticmethod
    def get_auth_method():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_method']
        except KeyError:
            raise KeyError("auth_method key is missing in the authorization section of the configuration file")

    @staticmethod
    def get_auth_headers():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_headers']
        except KeyError:
            raise KeyError("auth_headers key is missing in the authorization section of the configuration file")

    @staticmethod
    def get_auth_payload():
        config = ReadConfig.get_config()
        try:
            return config['authorization']['auth_payload']
        except KeyError:
            raise KeyError("auth_payload key is missing in the authorization section of the configuration file")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        logs_directory = ReadConfig.get_logs_directory()
        csv_file_path = ReadConfig.get_csv_file_path()
        csv_data = ReadConfig.read_csv(csv_file_path)
        logging.info(f"Logs Directory: {logs_directory}")
        logging.info(f"CSV Data: {csv_data}")
    except FileNotFoundError as e:
        logging.error(e)
    except KeyError as e:
        logging.error(e)
