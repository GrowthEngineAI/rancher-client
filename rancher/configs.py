import os
from pathlib import Path


## Finds Env Variables in case of service usage ##
## Should only set one of two, not mix and match ##

RANCHER_URL = os.getenv('RANCHER_URL', "")
RANCHER_ACCESS_KEY = os.getenv('RANCHER_ACCESS_KEY', "")
RANCHER_SECRET_KEY = os.getenv('RANCHER_SECRET_KEY', "")
RANCHER_TOKEN = os.getenv('RANCHER_TOKEN', None)

# Support Cattle Env
CATTLE_URL = os.getenv('CATTLE_URL', "")
CATTLE_ACCESS_KEY = os.getenv('CATTLE_ACCESS_KEY', "")
CATTLE_SECRET_KEY = os.getenv('CATTLE_SECRET_KEY', "")
CATTLE_TOKEN = os.getenv('CATTLE_TOKEN', None)

HTTPX_TIMEOUT = float(os.getenv("HTTPX_TIMEOUT", "15.0"))
HTTPX_KEEPALIVE = int(os.getenv("HTTPX_KEEPALIVE", "50"))
HTTPX_MAXCONNECT = int(os.getenv("HTTPX_MAXCONNECT", "200"))

SSL_VERIFY = bool(os.getenv('SSL_VERIFY', 'true') in {'true', 'True', '1', 'yes', 'Yes'})
ENABLE_CLIENT_ASYNC = bool(os.getenv('ENABLE_CLIENT_ASYNC', 'true') in {'true', 'True', '1', 'yes', 'Yes'})
CACHE_DIR = os.getenv('RANCHER_CACHE_DIR', None)
LOG_LEVEL = os.getenv('RANCHER_LOG_LEVEL', 'info')

CLIENT_URL = RANCHER_URL or CATTLE_URL
CLIENT_ACCESS_KEY = RANCHER_ACCESS_KEY or CATTLE_ACCESS_KEY
CLIENT_SECRET_KEY = RANCHER_SECRET_KEY or CATTLE_SECRET_KEY
CLIENT_TOKEN = RANCHER_TOKEN or CATTLE_TOKEN

if not CACHE_DIR: CACHE_DIR = Path(__file__).parent.joinpath('.cache')
CACHE_DIR.mkdir(parents=True, exist_ok=True)
