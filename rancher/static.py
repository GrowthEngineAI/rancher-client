import os


LIST_METHODS = {'__iter__': True, '__len__': True, '__getitem__': True}

TIME = os.environ.get('TIME_API') is not None
DEFAULT_TIMEOUT = 45

LIST = 'list-'
CREATE = 'create-'
UPDATE = 'update-'
DELETE = 'delete-'
ACTION = 'action-'
TRIM = True
JSON = False

GET_METHOD = 'GET'
POST_METHOD = 'POST'
PUT_METHOD = 'PUT'
DELETE_METHOD = 'DELETE'

HEADERS = {'Accept': 'application/json'}