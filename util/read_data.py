import os
import yaml
from settings import DATA_DIR


class ReadData:

    def get_yaml_data(self, file):
        if not os.path.isfile(DATA_DIR + file):
            raise FileNotFoundError("文件路径不存在， 请检查路劲是否正确： %s" % DATA_DIR + file)
        with open(DATA_DIR + file, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data


