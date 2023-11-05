from Features.delete_booking import delete_booking
from Features.get_booking import get_booking_details,get_booking_details_statuscode
import json

with open('create_booking_data.txt', 'r') as filehandle:
    booking_data = json.load(filehandle)
    filehandle.close()

booking_id = booking_data[0][0]
response_status_delete = None


def test_delete_booking():
    assert get_booking_details(booking_id) != None , f"Delete booking failed, booking {booking_id} not exist"
    assert delete_booking(booking_id) == 201, f"Failed when deleting booking, get reponse code {delete_booking(booking_id)}"
    assert get_booking_details_statuscode(booking_id) == 404, f"Delete booking failed, get reponse code {get_booking_details_statuscode(booking_id)}"
    # Not found status code = 404