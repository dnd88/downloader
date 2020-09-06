'''
conda install -c conda-forge youtube-dl
conda install -c conda-forge ffmpeg

[그냥 터미널에서 이렇게 명령어 쳐도 다운 받을 수 있음]
youtube-dl -f bestvideo[height=1080]+bestaudio --merge-output-format mkv https://www.youtube.com/watch?v=2DEDNW5Jq4Q
youtube-dl -f bestvideo[height=1080]+bestaudio --merge-output-format mkv [다운받을 유튜브영상 주소 url]

위의 명령어는 1080 화질로 그냥 받으면 소리가 안나오는 파일이 오기때문에
소리 파일을 따로 받아서 merge하는 것!

youtube-dl -f bestvideo[height=1080]+bestaudio --merge-output-format mkv -o './download_video/%(title)s.%(ext)s' https://www.youtube.com/watch?v=Jg5wkZ-dJXA
-o './download_video/%(title)s.%(ext)s'
이 명령어가 다운로드 위치 지정 옵션
mp4 확장자로 했을때 소리 안나옴
mkv 확장자로 했을때 소리 나옴

https://www.youtube.com/playlist?list=블라블라
이런식으로 끝에 플레이리스트 주소를 넣으면 모든 리스트 다운 받음

format code extension resolution  note
140         m4a       audio only  DASH audio , audio@128k (worst)
160         mp4       144p        DASH video , video only
133         mp4       240p        DASH video , video only
134         mp4       360p        DASH video , video only
135         mp4       480p        DASH video , video only
136         mp4       720p        DASH video , video only 소리 없음
17          3gp       176x144
36          3gp       320x240
5           flv       400x240
43          webm      640x360
18          mp4       640x360
22          mp4       1280x720    (best)
'''

import os
import youtube_dl



# 다운로드 디렉토리 만들기
def check_dir():
    download_dir = './download_video'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir


def download_video_and_subtitle(output_dir, youtube_video_list):

    # download_path = os.path.join(output_dir, '%(id)s-%(title)s.%(ext)s')
    download_path = os.path.join(output_dir, '%(title)s.%(ext)s')

    for video_url in youtube_video_list:

        # youtube_dl options
        ydl_opts = {
            'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
            # 'format': '18', # mp4 640x360 화질로 선택(화질을 선택하여 다운로드 가능)
            # 'format': '136', # 소리 없음
            'outtmpl': download_path, # 다운로드 경로 설정
            'writesubtitles': 'best', # 자막 다운로드(자막이 없는 경우 다운로드 X)
            # 'writethumbnail': 'best',  # 영상 thumbnail 다운로드
            'writeautomaticsub': True, # 자동 생성된 자막 다운로드
            'subtitleslangs': 'en'  # 자막 언어가 영어인 경우(다른 언어로 변경 가능)
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            print('error', e)


if __name__ == '__main__':

    VIDEO_DOWNLOAD_PATH = check_dir()

    # 내 리스트 설정 비공개(x), 일부공개로 변경후 리스트 url을 넣어도 작동함 ex) "https://www.youtube.com/playlist?list=블라블라"
    youtube_url_list = [  # 유투브에서 다운로드 하려는 영상의 주소 리스트(아래는 Sample Video 리스트)
        "https://www.youtube.com/watch?v=dP15zlyra3c",
        "https://www.youtube.com/watch?v=0EiV-ERKRRs"
    ]

    download_video_and_subtitle(VIDEO_DOWNLOAD_PATH, youtube_url_list)
    print('Complete download!')
