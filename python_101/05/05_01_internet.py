# Get data from internet

import urllib.request

def main():
    # open a url
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode())) # http result code eg 200 / 404
    
    # read data from url
    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()