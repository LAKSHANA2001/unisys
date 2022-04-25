import requests

def responseCheck(res):
    flag = -1
    if res>=200 and res<=299:
        print("Request Success")
        flag = 1
    elif res>=300 and res<=399:
        print("Redirection Message")
        flag = -1
    elif res>=400 and res<=499:
        print("Client error")
        flag = -1
    elif res>=500 and res<=599:
        print("Server error")
        flag = -1
    return flag


def auth():
    username = input("Enter Username:")
    password = input("Enter Password:")
    params = (username,password)
    try:
        r = requests.get("https://httpbin.org/basic-auth/unisys/mcp", auth=params,timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.text)
        elif r.status_code == 401:
            print("Username or password is wrong")
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def redirect():
    payload = {'url':'https://github.com/'}
    try:
        r = requests.get('https://httpbin.org/redirect-to', params=payload,timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.url)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def delay():
    try:
        r = requests.get("https://httpbin.org/delay/4",timeout=3)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def post():
    try:
        payload2 = {"test1": "test1Value", "test2": "test2Value"}
        r = requests.post("https://httpbin.org/post", data=payload2,timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.text)
            r_dict = r.json()
            print(r_dict["form"])
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")

def get():
    try:
        payload = {"page": 2, "count": 25}
        r = requests.get("https://httpbin.org/get", params=payload)
        if responseCheck(r.status_code) == 1:
            print(r.url,"\n")
            print(r.text)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


# payload1 = {"page": 2, "count": 25}
# r1 = requests.get("https://httpbin.org/get", params=payload1)

# print(r1.text)


# r2 = requests.post("https://httpbin.org/post", data=payload2)
# r2_dict = r2.json()
# print(r2_dict["form"])


# r = requests.get("https://httpbin.org/basic-auth/unisys/mcp", auth=("unisys", "mcp"))
# print(r)



while True:
    print("\n1.Auth\n2.Redirection\n3.Delay\n4.Post\n5.Get\n9.Exit\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        auth()
    elif ch==2:
        redirect()
    elif ch == 3:
        delay()
    elif ch == 4:
        post()
    elif ch==5:
        get()
    elif ch==9:
        break
    else:
        print("Enter correct choice")
