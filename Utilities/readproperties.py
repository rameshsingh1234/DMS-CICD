import os
import csv
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
    def get_csv_file_path():
        config = ReadConfig.get_config()
        try:
            csv_file_path = config['DEFAULT']['CSVFilePath']
            full_csv_path = os.path.abspath(os.path.join(os.path.dirname(ReadConfig.get_config_path()), csv_file_path))
            logging.info(f"CSV file path resolved to: {full_csv_path}")
            return full_csv_path
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

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        csv_file_path = ReadConfig.get_csv_file_path()
        csv_data = ReadConfig.read_csv(csv_file_path)
        logging.info(f"CSV Data: {csv_data}")
    except FileNotFoundError as e:
        logging.error(e)
    except KeyError as e:
        logging.error(e)
