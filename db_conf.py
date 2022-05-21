import os
import yaml
from conf import CONFIG_FILE_PATH, env


config_file = ''
if env == 'local':
    config_file = 'db_local.yaml'
elif env == "product":
    config_file = 'db_product.ymal'
else:
    raise Exception("Unknown env!!")
print(CONFIG_FILE_PATH)
with open(os.path.join(CONFIG_FILE_PATH, config_file)) as f:
    CONFIG = yaml.load(f, Loader=yaml.FullLoader)

# ========================== mysql
MYSQL_HOST = CONFIG['MYSQLHOST']
MYSQL_PORT = CONFIG['MYSQLPORT']
MYSQL_DATABASE = CONFIG['MYSQLDATABASE']
MYSQL_USER = CONFIG['MYSQLUSER']
MYSQL_PASSWORD = CONFIG['MYSQLPASSWORD']

# =========================== redis
REDIS_HOST = CONFIG['REDISHOST']
REDIS_PORT = CONFIG['REDISPORT']
REDIS_DB = CONFIG['REDISDB']
REDIS_PASSWORD = CONFIG['REDISPASSWORD']
