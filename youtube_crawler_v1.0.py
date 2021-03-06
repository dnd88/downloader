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
