import logging
import os


def get_logger():
    # create logger 创建对象
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug 创建处理器
    ch = logging.FileHandler(filename='mylog.log', encoding="utf-8")
    chi=logging.StreamHandler()
    chi.setLevel(logging.DEBUG)
    # create formatter 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch 格式器添加到处理器 ch.setFormatter(formatter)
    # add ch to logger 处理器添加到对象
    logger.addHandler(chi)
    return logger

