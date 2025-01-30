import requests


def email_validaitor(email):
    url = "https://api.usebouncer.com/v1.1/email/verify"
    query = {"email":email}
    headers = {"x-api-key": "MNE8pMW5d8yXp5EQGo6k0iKOvNFFyVkpg10jelhO"}

    response = requests.request("GET", url, headers=headers, params=query)

    rs = response.text
    ans = rs.split(',')[1].split(':')[1].replace('"', '')

    if ans == 'deliverable' or ans == 'risky':
        return True
    else:
        return False
