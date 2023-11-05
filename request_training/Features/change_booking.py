import requests
import json
target_url = "https://restful-booker.herokuapp.com/booking/"

basic_auth = ("admin","password123")

with open('create_booking_data.txt', 'r') as filehandle:
    booking_data = json.load(filehandle)

booking_id = booking_data[0][0]
# booking_body = booking_data[0][1]

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



def update_full_booking(booking_id,change_body):
    x = requests.put(url=target_url+str(booking_id),json = change_body, auth=basic_auth)
    print(x.json())
    assert x.status_code == 200,f"Request has return status code = {x.status_code} as not expected"
    return x.json()

def update_part_booking(booking_id,path_body):
    x = requests.patch(url = target_url+str(booking_id), json = path_body, auth = basic_auth)
    print(x.json())
    assert x.status_code == 200,f"Request has return status code = {x.status_code} as not expected"
    return x.json()    

