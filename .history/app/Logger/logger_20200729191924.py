# coding=utf-8
import os
import logging
import logging.config as log_conf
import datetime
import coloredlogs

coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}, 'hostname': {'color': 'magenta'}, 'levelname': {'color': 'magenta', 'bold': False}, 'name': {'color': 'green'}
         }


log_dir = os.path.dirname(os.path.dirname(__file__)) + '/logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
today = datetime.datetime.now().strftime("%Y-%m-%d")

log_path = os.path.join(log_dir, today + ".log")

log_config = {
    'version': 1.0,

    # 日志格式
    'formatters': {
        'colored_console': {
                        'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        'datefmt': '%H:%M:%S'
        },
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"  # 如果不加这个会显示到毫秒。
        },
    },

    # 终端或者文件
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',  # 日志打印到屏幕显示的类。
            'level': 'DEBUG',
            'formatter': 'colored_console'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',  # 日志打印到文件的类。
            'maxBytes': 1024 * 1024 * 1024,  # 单个文件最大内存
            'backupCount': 1,  # 备份的文件个数
            'filename': log_path,  # 日志文件名
            'level': 'INFO',  # 日志等级
            'formatter': 'detail',  # 调用上面的哪个格式
            'encoding': 'utf-8',  # 编码
        },
    },

    'loggers': {
        'logger': {
            'handlers': ['console'],  # 只打印屏幕
            'level': 'DEBUG',  # 只显示错误的log
        },

    }
}

log_conf.dictConfig(log_config)
log_v = logging.getLogger('log')

coloredlogs.install(level='DEBUG', logger=log_v)
# log_v.debug("哈哈哈哈")




# # Some examples.
# logger.debug("this is a debugging message")
# logger.info("this is an informational message")
# logger.warning("this is a warning message")
# logger.error("this is an error message")
# logger.critical("this is a critical message")