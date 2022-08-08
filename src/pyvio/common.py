import logging
import os.path
import time
import json
from typing import Union

import yaml


def get_logger(logfile, name=None, level=logging.INFO):
    # Set up logging.
    log_format = '%(asctime)s.%(msecs)03d - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename=logfile, filemode='w', format=log_format, datefmt=date_format, level=level)
    logger = logging.getLogger(name=name)

    if logfile:
        console = logging.StreamHandler()
        console.setLevel(level)
        logger.addHandler(console)

    logger.info("Logging started, timestamp={}".format(str(time.time())))
    return logger


class Configuration:
    def __init__(self, data: Union['Configuration', dict, str, None] = None, def_path=None):
        if isinstance(data, str):
            path = data
            if def_path is not None and not os.path.exists(path):
                path = os.path.join(def_path, path)
            loader = json if path[-5:] == '.json' else yaml
            with open(path, "r") as fh:
                data = loader.safe_load(fh)
        if isinstance(data, Configuration):
            data = data.dictview()
        assert isinstance(data, (dict, type(None))), \
            'wrong type data given, must be a path to a config file or a config dict'
        self._data = data or {}

    def __getattr__(self, item):
        if item == '_data':
            return super(Configuration, self).__getattr__(item)

        val = self._data[item]
        if isinstance(val, dict):
            return Configuration(val)
        return val

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __setattr__(self, item, val):
        if item == '_data':
            super(Configuration, self).__setattr__(item, val)
        else:
            if isinstance(val, Configuration):
                val = val.dictview()
            self._data[item] = val
        return val

    def __setitem__(self, item, val):
        return self.__setattr__(item, val)

    def __contains__(self, item):
        return item in self._data

    def dictview(self):
        return self._data

    def to_json(self):
        return json.dumps(self.data)

    def to_yaml(self):
        return yaml.dump(self.data)
