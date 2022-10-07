import requests
import argparse

def upload(vid):
    url = "http://localhost:3000/package/"
    data = {'title':'metadata','timeDuration':120}
    file = open("vids/"+vid, 'rb')
    files = {'messageFile': file}

    req = requests.post(url, files=files, json=data)
    # print (req.status_code)
    # print (req.content)
    print (req)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vid", type=str, help="video name")
    flags = parser.parse_args()
    opt = vars(flags)
    vid = opt["vid"]
    return vid

if __name__ == "__main__":
    vid = parse_opt()
    upload(vid)