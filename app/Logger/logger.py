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

    # 格式输出
    'formatters': {
        'colored_console': {
                        'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        'datefmt': '%H:%M:%S'
        },
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"  #时间格式
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler', 
            'level': 'DEBUG',
            'formatter': 'colored_console'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',  
            'maxBytes': 1024 * 1024 * 1024,  
            'backupCount': 1, 
            'filename': log_path, 
            'level': 'INFO',  
            'formatter': 'detail',  # 
            'encoding': 'utf-8',  # utf8 编码  防止出现编码错误
        },
    },

    'loggers': {
        'logger': {
            'handlers': ['console'],  
            'level': 'DEBUG', 
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