import requests

basic_auth ={
    "username" : "admin",
    "password" : "password123"
}


def create_token():

    x = requests.post(url="https://restful-booker.herokuapp.com/auth",data=basic_auth)
    assert x.status_code == 200, f"Request has return status code = {x.status_code} as not expected"
    print (x.json())    