import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER + configuration.TRACK_NUMBER,
                         json=body,
                         headers=data.headers)
response = post_new_order(data.create_order)