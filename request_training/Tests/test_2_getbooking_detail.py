import pytest
import json
from Features.get_booking import get_booking_ids,get_booking_details

target_url = "https://restful-booker.herokuapp.com/booking/"

booking_body = {'firstname': 'Feed', 
                'lastname': 'Cuong', 
                'totalprice': 2000, 
                'depositpaid': True, 
                'bookingdates': {'checkin': '2023-09-01', 'checkout': '2023-08-10'}, 
                'additionalneeds': 'super bowls'}

booking_data = [(4443, {
  "firstname": "Josh",
  "lastname": "Allen",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "super bowls"
}
)]
# run get_booking.py to get new booking data
with open('booking_data.txt', 'r') as filehandle:
    booking_data2 = json.load(filehandle)
    filehandle.close()
with open('create_booking_data.txt', 'r') as filehandle:
    create_booking_data = json.load(filehandle)
 

def test_get_booking_ids():
    test_response = get_booking_ids()
    for i in test_response:
        booking_key = list(i.keys())
        assert "bookingid" == booking_key[0], f"One of the response have difference key name = {i}"
        assert i.get("bookingid") > 0, f"The response have invalid booking id = {i}"


def test_get_booking_details():
    assert get_booking_details(create_booking_data[0][0]) == booking_body, f"The booking {create_booking_data[0][0]} has different detail"

@pytest.mark.parametrize("bookingid,booking_body",booking_data)
def test_get_booking_details_with_parametrize(bookingid,booking_body):
    assert get_booking_details(bookingid) == booking_body, f"The booking {bookingid} has different detail"

@pytest.mark.parametrize("bookingid2,booking_body2",booking_data2)
def test_get_booking_details_with_parametrize2(bookingid2,booking_body2):
    assert get_booking_details(bookingid2) == booking_body2, f"The booking {bookingid2} has different detail"

@pytest.mark.parametrize("create_booking_id,create_booking_body",create_booking_data)
def test_get_created_booking_details(create_booking_id,create_booking_body):
    assert get_booking_details(create_booking_id) == create_booking_body, f"The booking {create_booking_id} has different detail"