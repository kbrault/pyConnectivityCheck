from http.client import HTTPConnection
from urllib.parse import urlparse

def is_online(url, timeout=5):
    parser = urlparse(url)
    error = Exception("unknown error")
    for port in (80, 443):
        connection = HTTPConnection(host=parser.netloc, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()

def main():
    url_to_test = "https://www.python.org"
    if is_online(url_to_test):
        print(url_to_test+" is online")
    else:
        print(url_to_test+" is offline")

if __name__ == "__main__":
    main()