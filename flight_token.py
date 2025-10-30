import requests


class FlightToken:
    API_ENDPOINT =  "https://test.api.amadeus.com/v1/security/oauth2/token"

    flight_params = {
        "grant_type": "client_credentials",
        "client_id": "GAOW0lNFnIfJaSYd6GbAKduUjiijgRwS",
        "client_secret": "NHd4QYFS4ALuhek7"
    }


    response = requests.post(API_ENDPOINT, data=flight_params)
    print(response.text)