from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from communicate import Mqtt

try:
    import argparse

except ImportError:
    flags = None

def run(vid, flags):

    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()

    if not creds or creds.invalid:
        print("make new storage data file ")
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES) # 인증정보 파일
        creds = tools.run_flow(flow, store, flags) if flags else tools.run(flow, store)

    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    folder_id = '1k0gHQTVcDD09LkLaS0eS0zHkHEhb0Qka' # 업로드 될 구글 드라이브의 위치 

    file_name = "vids/" + vid
    metadata = {'name': vid, # 업로드 될 파일 이름
                'parents' : [folder_id],
                'mimeType': None
                }

    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
    if res:
        print("Upload %s (%s)" % (file_name, res["mimeType"]))
        mqtt_filename = Mqtt('delivery_publisher' ,'delivery/received')
        mqtt_filename.pub(vid)

def parse_opt():
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument("--vid", type=str, help="video name")
    flags = parser.parse_args()
    opt = vars(flags)
    vid = opt["vid"]
    return vid, flags

if __name__ == "__main__":
    vid, flags = parse_opt()
    run(vid, flags)
