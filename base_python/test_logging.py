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


if __name__ == '__main__':
    test_basic_logging()


