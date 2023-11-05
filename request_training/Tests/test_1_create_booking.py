target_url = "https://restful-booker.herokuapp.com/booking"

booking_body = {'firstname': 'Feed', 
                'lastname': 'Cuong', 
                'totalprice': 2000, 
                'depositpaid': True, 
                'bookingdates': {'checkin': '2023-09-01', 'checkout': '2023-10-31'}, 
                'additionalneeds': 'super bowls'}



def test_create_booking(create_booking):
    assert create_booking["bookingid"] != None 
    assert create_booking["booking"] == booking_body, "the booking detail did not the same"

# pytest -vv -k test_1 --junitxml="result.xml"