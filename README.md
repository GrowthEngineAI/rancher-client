# rancher-client
 Python Rancher Client with Async Support

This library is a fork from Rancher's official [client-python](https://github.com/rancher/client-python) to enable support of:
- Environment Variables for Service Usage
- Async [WIP] / Sync Client Support
- Replace `requests` in favor of `httpx`


## Installing

**Note: This package requires Python 3+**

```bash
pip install rancher-client
# or 
pip install git+https://github.com/growthengineai/rancher-client.git@main
```

## Environment Variables

Below are the currently supported Environment Variables

- `RANCHER` Prefix
    - `RANCHER_URL`: str = ""
    - `RANCHER_ACCESS_KEY`: str = ""
    - `RANCHER_SECRET_KEY`: str = ""
    - `RANCHER_TOKEN`: str = None

- `CATTLE` Prefix
    - `CATTLE_URL`: str = ""
    - `CATTLE_ACCESS_KEY`: str = ""
    - `CATTLE_SECRET_KEY`: str = ""
    - `CATTLE_TOKEN`: str = None

- `HTTPX` Variables
    - `HTTPX_TIMEOUT`: float = 15.0
    - `HTTPX_KEEPALIVE`: int = 50
    - `HTTPX_MAXCONNECT`: int = 200

- Misc Variables
    - `SSL_VERIFY`: bool = True
    - `RANCHER_LOG_LEVEL`: str = "info"
    - `RANCHER_CACHE_DIR`: str = `~/rancher-client/rancher/.cache`


## Using API

```python
from rancher import RancherClient

client = RancherClient(url='https://localhost:8443/v3',
                        access_key='<some valid access key>',
                        secret_key='<some valid secret key>')

# Alternatively if Env Variables are set, can be called implicitly
# client = RancherClient()

# curl -s https://localhost:8443/v3/users?me=true
client.list_user(me='true')

# curl -s -X POST https://localhost:8443/v3/users -H 'Content-Type: application/json' -d '{ "username" : "user1", "password": "Password1" }'
client.create_user(username='user1', password='Password1')

# curl -s -X PUT https://localhost:8443/v3/users/user-xyz123 -H 'Content-Type: application/json' -d '{ "description" : "A user" }'
user = client.by_id_user('user-xyz123')
client.update(user, description='A user')

# curl -s -X DELETE https://localhost:8443/v3/users/user-xyz123
user = client.by_id_user('user-xyz123')
client.delete(user)

# Links
# curl -s https://localhost:8443/v3/clusterRoleTemplateBindings?userId=user-xyz123
user = client.by_id_user('user-xyz123')
user.clusterRoleTemplateBindings()
```

## Examples

### Actions [Rancher API spec](https://github.com/rancher/api-spec/blob/master/specification.md#actions)
From the spec 
> "Actions perform an operation on a resource and (optionally) return a result."

To perform the `setpodsecuritypolicytemplate` action on a project object these are the steps.

This first method has built-in retry logic inside of `client.action()` when the error returned is 409
```python
#creates a project and handles cleanup
project =  admin_pc.project 
# create an api_client from a management context
api_client = admin_mc.client
# perform the action via the client api
api_client.action(obj=project, action_name="setpodsecuritypolicytemplate",
                    podSecurityTemplateId=pspt.id)
```
Or alternatively, performing the action from the project context (which does not have built-in retry logic)
```python

project = api_client.create_project(name="test-project", clusterId="local")
project.setpodsecuritypolicytemplate(podSecurityPolicyTemplateId="my-pspt")

```