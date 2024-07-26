import configparser
import os
import csv

class ReadConfig:
    config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Configuration/config.init'))

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
            logs_dir_abs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', logs_dir))
            print(f"Logs directory: {logs_dir_abs}")
            return logs_dir_abs
        except KeyError:
            raise KeyError("LogsDirectory key is missing in the configuration file.")

    @staticmethod
    def get_csv_file_path():
        config = ReadConfig.get_config()
        try:
            csv_file_path = config['DEFAULT']['CSVFilePath']
            csv_file_path_abs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', csv_file_path))
            print(f"CSV file path: {csv_file_path_abs}")
            return csv_file_path_abs
        except KeyError:
            raise KeyError("CSVFilePath key is missing in the configuration file.")

    @staticmethod
    def read_csv(file_path):
        print(f"Reading CSV file from: {file_path}")
        if os.path.exists(file_path):
            with open(file_path, mode='r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                data = [row for row in csv_reader]
            return data
        else:
            raise FileNotFoundError(f"CSV file not found: {file_path}")
