import requests

def main():
    res=requests.get("http://127.0.0.1:5000/api/flights/2")
    if res.status_code!=200:
        raise Exception("Error")
    data=res.json()
    print(data)

if __name__=="__main__":
    main()
    