from Features.change_booking import update_full_booking, update_part_booking
from Features.get_booking import get_booking_details_statuscode
import json

with open('create_booking_data.txt', 'r') as filehandle:
    booking_data = json.load(filehandle)
    filehandle.close()

booking_id = booking_data[0][0]
booking_body = booking_data[0][1]

change_body = {
    "firstname" : "Feed",
    "lastname" : "Brown",
    "totalprice" : 4250,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-09-02",
        "checkout" : "2023-09-03"
    },
    "additionalneeds" : "Breakfast, parking, car rent"
}

path_body = {
    "firstname" : "FeedChangePath",
    "lastname" : "FeedChangePath",
    "bookingdates" : {
        "checkin" : "2023-09-04",
        "checkout" : "2023-09-05"
    }    
}


def test_update_full_booking():
    assert get_booking_details_statuscode(booking_id) == 200, f"Failed to get booking, Get reponse code {get_booking_details_statuscode(booking_id)}"
    assert update_full_booking(booking_id,change_body) != booking_body, f"The booking {booking_id} has different detail"

def test_update_part_booking():
    assert get_booking_details_statuscode(booking_id) == 200, f"Failed to get booking, Get reponse code {get_booking_details_statuscode(booking_id)}"
    response = update_part_booking(booking_id,path_body)
    for i in path_body.keys():
        assert response[i] == path_body[i], f"The booking attribute {i} is not the same as expected"

