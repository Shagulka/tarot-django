import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response.get("ip")


def get_utc_offset():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    return response.get("utc_offset")
