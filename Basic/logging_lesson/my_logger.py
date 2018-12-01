import logging
from logging.handlers import RotatingFileHandler

# 第一步 创建一个日志收集器logger
logger = logging.getLogger("autotest")

# 第二步
# 默认输出warning级别
# 修改日志的输出级别
logger.setLevel(logging.INFO)

# 第三步
# 输出的日志内容格式
fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

fm = logging.Formatter(fmt, datefmt)

# 第四步
# 设置输出渠道--输出到文件handler
hd_1 = RotatingFileHandler("autotest.log",maxBytes=1024*1024*2,backupCount=10)
# 在handle中指定日志内容格式
hd_1.setFormatter(fm)

# 设置输出到控制台
hd_2 = logging.StreamHandler()

# 将handle添加到日志logger上
logger.addHandler(hd_1)
logger.addHandler(hd_2)

# 第五步
#调用日志输出方法
logger.info("hehheheheh")
logger.warning("我是warning级别")
logger.error("我是error级别")
