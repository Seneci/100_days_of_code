import requests
import tkinter
from functools import partial


def killme():
    window.quit()
    window.destroy()


def obtain_coordiantes():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    latitude = response.json()['iss_position']['latitude']
    longitude = response.json()['iss_position']['longitude']
    return latitude, longitude


def reverse_geocoding(latitude, longitude):
    # 04cc7aaf77053dfab3a1ec5c51dad841
    geo_response = requests.get('http://api.openweathermap.org/geo/1.0/reverse?lat=' + latitude + \
                                '&lon=' + longitude + '&limit=1&appid=04cc7aaf77053dfab3a1ec5c51dad841')

    return geo_response.json()


def print_in_window(lat, long, message_2):
    result['text'] = 'The ISS is on latitude', lat, 'and longitude', long, '.', message_2


if __name__ == '__main__':
    lat = obtain_coordiantes()[0]
    long = obtain_coordiantes()[1]

    geo_response = requests.get('http://api.openweathermap.org/geo/1.0/reverse?lat=' + lat + '&lon=' + long + '&limit=1&appid=04cc7aaf77053dfab3a1ec5c51dad841')
    print(geo_response.status_code)
    print(geo_response.json())

    if len(reverse_geocoding(lat, long)) == 0:
        message_2 = "The ISS is on unknown location"
    else:
        message_2 = "The ISS is on", geo_response.json()

    window = tkinter.Tk()
    window.geometry('600x200')

    text = tkinter.Label(window, text="Would you like to know where is the ISS?", font='Roboto 12')
    text.pack()

    button_yes = tkinter.Button(window, text='Yes!', command=partial(print_in_window, lat, long, message_2))
    button_yes.pack()

    button_no = tkinter.Button(window, text='No', command=killme)
    button_no.pack()

    result = tkinter.Label(window)
    result.pack()

    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
