import requests
import json
target_url = "https://restful-booker.herokuapp.com/booking/"
booking_id = []
booking_details= []
booking_data = []

def get_booking_ids():
    x = requests.get(target_url)
    return x.json()

def get_booking_details(booking_id):
    x = requests.get(target_url+str(booking_id))
    assert x.status_code == 200, f"Request has return status code = {x.status_code} as not expected"
    return x.json()

def get_booking_details_statuscode(booking_id):
    x = requests.get(target_url+str(booking_id)).status_code
    return x
# I use this script to save a booking id and detail on a text file 

if __name__ == '__main__':
    for i in get_booking_ids():
            booking_id.append(i['bookingid'])
    print(booking_id)
    print(get_booking_details(booking_id[0]))
    booking_details.append(get_booking_details(booking_id[0]))
    booking_details.append(get_booking_details(booking_id[-1]))
    booking_data = [(booking_id[0],booking_details[0]),(booking_id[-1],booking_details[1])] 
    # I just save 2 record of booking detail, so the last record have index =1
    print(booking_data)

    with open('booking_data.txt', 'w') as filehandle:
        json.dump(booking_data, filehandle)
        filehandle.close()
