import requests

target_url = "https://restful-booker.herokuapp.com/booking/"
booking_id = None

basic_auth = ("admin","password123")


def delete_booking(booking_id):
    x = requests.delete(target_url+str(booking_id), auth= basic_auth)
    print(x.status_code)
    print(x._content)
    return x.status_code
