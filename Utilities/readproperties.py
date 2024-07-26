import configparser
import os
import csv


class ReadConfig:
    config_file = os.path.join(os.path.dirname(__file__), '../Configuration/config.init')

    @staticmethod
    def get_config():
        print(f"Reading configuration file from: {ReadConfig.config_file}")
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
            logs_dir = config['DEFAULT']['LogsDirectory']
            print(f"Logs directory: {logs_dir}")
            return logs_dir
        except KeyError:
            raise KeyError("LogsDirectory key is missing in the configuration file.")

    @staticmethod
    def get_csv_file_path():
        config = ReadConfig.get_config()
        try:
            csv_file_path = config['DEFAULT']['CSVFilePath']
            print(f"CSV file path: {csv_file_path}")
            return csv_file_path
        except KeyError:
            raise KeyError("CSVFilePath key is missing in the configuration file.")

    @staticmethod
    def read_csv(file_path):
        abs_path = os.path.join(os.path.dirname(__file__), '..', file_path)
        print(f"Reading CSV file from: {abs_path}")
        if os.path.exists(abs_path):
            with open(abs_path, mode='r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                data = [row for row in csv_reader]
            return data
        else:
            raise FileNotFoundError(f"CSV file not found: {abs_path}")
