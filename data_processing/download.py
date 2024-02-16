import requests

def download_json(url, filename):
    # HTTP GET to URL
    response = requests.get(url)

    # success (200)
    if response.status_code == 200:

        #write the answer in a file
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File '{filename}' downloaded with success.")

    else:
        raise Exception(f"File download failed with status code: {response.status_code}")