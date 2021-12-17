import httplib2
from apiclient import discovery
from config import search_context, call_time
import python_for_gmail  # 先ほど作成したプログラム
import winsound
import time
import datetime

#○秒に一度最新のメール○件をチェック(小さめにしてね)
CHECK_MAIL_NUM = 10
# 1日は1440分だよ、12時間なら720
CALL_TIME = 720

dt_log = datetime.datetime.now()
# 配信画面いくつも開いたりアラートいくつも鳴らないようにcall_time分だけタスク待機させる
crnt = int(time.time())
call_timestamp = 60 * CALL_TIME
num = 0
is_alert = False

with open('exist.txt', 'r') as f:
    line = f.read()
    diff = int(line)
    # diff = int(f.read)
    call_time = crnt - diff - call_timestamp
    if call_time < 0:
        print("[alert] 12時間以内に配信やってるよ")
        with open('res.log', "a", encoding='utf-8') as f:
            f.write(dt_log.strftime('%Y年%m月%d日%H時%M分%S秒') + " res 2\n")
        exit(2)

with open('sample.wav', 'rb') as f:
    data = f.read()



# Gmailのサービスを取得
def gmail_get_service():
    # ユーザー認証の取得
    credentials = python_for_gmail.gmail_user_auth()
    http = credentials.authorize(httplib2.Http())
    # GmailのAPIを利用する
    service = discovery.build('gmail', 'v1', http=http)
    return service

# メッセージの一覧を取得
def gmail_get_messages():
    # http://www.ops.dti.ne.jp/ironpython.beginner/global.html
    global is_alert
    try:
        service = gmail_get_service()
        # メッセージの一覧を取得
        messages = service.users().messages()
        msg_list = messages.list(userId='me', maxResults=10).execute()

        # 取得したメッセージの一覧を表示
        for msg in msg_list['messages']:
            topid = msg['id']
            msg = messages.get(userId='me', id=topid).execute()
            recv_time = int(int(msg['internalDate'])/1000)
            # print(recv_time)
            if search_context in msg['snippet']:
                call_time = crnt - recv_time - call_timestamp
                if call_time < 0:
                    print("---")
                    print(msg['snippet'])  # 要約を表示
                    winsound.PlaySound(data, winsound.SND_MEMORY)
                    is_alert = True
                print(call_time)
        print(crnt)
    except Exception as e:
        print("取得失敗したみたい…")
        print(e)
        return

gmail_get_messages()

if is_alert:
    with open('res.log', "a", encoding='utf-8') as f:
        f.write(dt_log.strftime('%Y年%m月%d日%H時%M分%S秒') + " res 1\n")
    with open('exist.txt', "w", encoding='utf-8') as f:
        f.write(str(crnt))
    print("[alert] メン限始まってるよ")
    winsound.PlaySound(data, winsound.SND_MEMORY)
    exit(1)

with open('res.log', "a", encoding='utf-8') as f:
    f.write(dt_log.strftime('%Y年%m月%d日%H時%M分%S秒') + " res 0\n")
exit(0)
