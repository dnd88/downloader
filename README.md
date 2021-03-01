# 사용법

```
source activate my_env

conda install -c conda-forge youtube-dl
conda install -c conda-forge ffmpeg
```
[그냥 터미널에서 이렇게 명령어 쳐도 다운 받을 수 있음]
```
youtube-dl -f bestvideo[height=1080]+bestaudio --merge-output-format mkv https://www.youtube.com/watch?v=2DEDNW5Jq4Q
youtube-dl -f bestvideo[height=1080]+bestaudio --merge-output-format mkv [다운받을 유튜브영상 주소 url]
```

위의 명령어는 1080 화질로 그냥 받으면 소리가 안나오는 파일이 오기때문에
소리 파일을 따로 받아서 merge하는 것!
```
youtube-dl -f bestvideo[height=1080]+bestaudio --merge-output-format mkv -o './download_video/%(title)s.%(ext)s' https://www.youtube.com/watch?v=Pnz9h33LvdE
```
```
-o './download_video/%(title)s.%(ext)s'
```
이 명령어가 다운로드 위치 지정 옵션
mp4 확장자로 했을때 소리 안나옴
mkv 확장자로 했을때 소리 나옴

https://www.youtube.com/playlist?list=블라블라
이런식으로 끝에 플레이리스트 주소를 넣으면 모든 리스트 다운 받음

### [사용추천]
```
youtube-dl -f 137+140 -o './download_video/%(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLtKvrJm1v37KUgodxA8Satr3A5E5LzjAm
이렇게도 가능 , 이런식으로 하면 mp4로도 잘 merge 됨
```
### [최대퀄리티]
```
# Download best mp4 format available or any other best if no mp4 available
$ youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o './download_video/%(title)s.%(ext)s'

# Download best format available via direct link over HTTP/HTTPS protocol
$ youtube-dl -f '(bestvideo+bestaudio/best)[protocol^=http]'
```

### [플레이리스트에서 특정 인덱스파일만 선택하기]
```
--playlist-start NUMBER
--playlist-end NUMBER
--playlist-items 1-3,7,10-13

ex) $ "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o './download_video/%(title)s.%(ext)s' --playlist-start 23 --playlist-end 56 https://www.youtube.com/playlist?list=PL8uzAiCio-SHQoM1yJ-jwzHHN3-4AAGWg"
$ youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o './download_video/%(title)s.%(ext)s' --playlist-items 1-2,4-6,8-18 https://www.youtube.com/playlist?list=PL8uzAiCio-SFIq9mv9FQbY09Ey4TdRM4C
```

### [720이 최대일: 1080으로 요청하면 ERROR: requested format not available 라고 뜸]
```
youtube-dl -f 136+140 -o './download_video/%(title)s.%(ext)s'

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
```

### [pip 로 버전 업그레이드 시]

이슈: ERROR: YPRwIeZQJ8Q: YouTube said: Unable to extract video data
    다운로드 시도때마다 이런 에러 뜸
```
pip install --upgrade youtube-dl

(youtube-dl --update  이렇게만 명령어 사용하면,
It looks like you installed youtube-dl with a package manager, pip, setup.py or a tarball. Please use that to update. 이렇게 나옴)
```

### [mp3파일만 받기]
```
youtube-dl -x --audio-format mp3 --audio-quality 0 -o './download_video/%(title)s.%(ext)s' [download video url]
```
--audio-quality 0 가 최고 음질

### [자막만 받기]
### [가능한 자막 리스트 확인]
```
youtube-dl --list-subs [down video url]
youtube-dl --write-sub --sub-lang ko --convert-subs srt -o './download_video/%(title)s.%(ext)s' --skip-download [download video url]

--write-auto-sub 자동생성자막
--write-sub 일반등록자막
```
아직 smi 자막파일 지원안함!

### 로그인 필요시
```
ex) $ youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o './download_video/%(title)s.%(ext)s' \
--cookies ./youtubecom_cookies.txt [download video url]
```
Chrome 브라우저로 해당 영상에 로그인 후 Chrome plugin Cookie.txt 를 사용하여 쿠키 파일을 만든 뒤
--cookies /path/to/cookies/file.txt 이 flag 사용할 것

### [에러 케이스]
[download] Got server HTTP error: HTTP Error 404: Not Found. Retrying fragment 1 (attempt 1 of 10)...
이런 에러를 만났을때
```
youtube-dl -f best [download video url]
```
이렇게 해결 
