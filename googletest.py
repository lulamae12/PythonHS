import homeassistant.remote as remote

api = remote.API('', 'password')
print(remote.validate_api(api))
