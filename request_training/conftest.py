import pytest
import requests
import json
from datetime import date
from datetime import timedelta
#API doc https://restful-booker.herokuapp.com/apidoc/index.html
target_url = "https://restful-booker.herokuapp.com/booking/"
currentday = date.today()
nextday = date.today() + timedelta(days=1)


booking_body = {'firstname': 'Feed', 
                'lastname': 'Cuong', 
                'totalprice': 2000, 
                'depositpaid': True, 
                'bookingdates': {'checkin': '2023-09-1', 'checkout': str(nextday)}, 
                'additionalneeds': 'super bowls'}


@pytest.fixture
def create_booking():
    x= requests.post(url = target_url, json = booking_body)
    assert x.status_code == 200
    create_booking_data = [(x.json()['bookingid'],x.json()['booking'])]
    with open('create_booking_data.txt', 'w') as filehandle:
        json.dump(create_booking_data, filehandle)    
        filehandle.close
    return x.json()

@pytest.fixture
def get_booking_id(create_booking):
    booking_id = create_booking['bookingid']
    return booking_id
