# This script requires the requests library
import requests


def how_many_astronauts():
    # Send the GET request that no needs authentication neither parameters
    response = requests.get("http://api.open-notify.org/astros.json")
    # Store the response json into a variable
    response_json = response.json()
    # print(response.status_code)
    # print(object)
    # Print the name of the astronauts
    print('There are', len(response_json['people']), 'astronauts on space right now:')
    for i in range(len(response_json['people'])):
        print(response_json['people'][i]['name'], 'is currently now on', response_json['people'][1]['craft'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    how_many_astronauts()
