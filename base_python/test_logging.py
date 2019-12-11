"""
logging 与 print
"""

def test_print():
    # 2.0 与 3.0 print
    word = "hello world"
    # print word
    print(word)
    x = "a"
    y = 123
    z = ["abc"]
    print(x, y, z)
    print(x, y, z, sep=".....")
    print(x, y, z, end=" *\n")
    print(x, y, z, sep='...', file=open('data.txt','w'))
    print(open('data.txt').read())


def test_simple_logging():
    import logging
    logger = logging.getLogger(__name__)
    logger.info("logging info")
    logger.debug("logging debug")
    logger.warning("logging warning")
    logger.error("logging error")
    logger.critical("logging critical")


def test_basic_logging():
    import logging
    import datetime
    log_filename = 'log/sys_%s.log' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
    log_level = logging.INFO
    log_format = '%(asctime)s[%(levelname)s]: %(message)s'
    # stream 和 filename共存，取filename 忽视stream
    # logging.basicConfig(filename=log_filename, level=log_level, format=log_format)
    logging.basicConfig(level=log_level, format=log_format)
    logger = logging.getLogger()
    logger.info("logging info")
    logger.debug("logging debug")
    logger.warning("logging warning")
    logger.error("logging error")
    logger.critical("logging critical")

def test_handler_logging():
    import logging
    import datetime
    import sys
    logger = logging.getLogger()
    # 设置日志输出级别
    logger.setLevel(logging.INFO)
    # FileHandler 日志输出到文件handler_log.log下
    log_file = "log/handler_log.log"
    file_handler = logging.FileHandler(log_file)
    # 给文件设置日志级别
    file_handler.setLevel(logging.WARNING)
    # 设置日志输出格式
    file_format = logging.Formatter("%(asctime)s[%(levelname)s]: %(messages)s")
    file_handler.setFormatter(file_format)
    # StreamHandler 日志输出到Stream，默认输出是sys.stderr,可以设置为sys.stdout
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    # 将不同的Handler添加到logger中，日志就会同时输出到不同的Handler控制的输出中
    # 注意如果此logger在之前使用basicConfig进行基础配置，因为basicConfig会自动创建一个Handler，所以此logger将会有3个Handler
    # 会将日志同时输出到3个Handler控制的输出中
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.info("logging info")
    logger.debug("logging debug")
    logger.warning("logging warning")
    logger.error("logging error")
    logger.critical("logging critical")


if __name__ == '__main__':
    # test_basic_logging()
    test_handler_logging()

