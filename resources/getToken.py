import requests


def get_token(tenant_id, client_id, client_secret):

    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    token_payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://api.businesscentral.dynamics.com/.default'
    }
    token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    token_response = requests.post(token_url, data=token_payload, headers=token_headers)

    if token_response.status_code != 200:
        print("❌ Token ophalen mislukt:")
        print(token_response.text)
        exit()

    access_token = token_response.json()['access_token']
    print("✅ Token succesvol opgehaald")
    return access_token