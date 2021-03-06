#!/bin/bash
# 윈도우 작성 스크립트일시 아래 명령어를 한번 실행후 사용하기
# sed -i -e 's/\r$//' [대상 파일]

arr_playlists=("https://www.youtube.com/playlist?list=PL8uzAiCio-SHQoM1yJ-jwzHHN3-4AAGWg")

var_skip="https://www.youtube.com/watch?v=PbG0gxzg_JQ&list=PL8uzAiCio-SHQoM1yJ-jwzHHN3-4AAGWg&index=22"

for i in ${arr_playlists[@]}; do

    if [[ $i -eq $var_skip ]]; then
      #statements
      continue
    fi

    youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o './download_video/%(title)s.%(ext)s' $i
    if [ $? -eq 0 ]; then
      echo "OK"
    else
      echo $i "fail!!!"
    fi
done
echo "Finish"

# 플레이리스트에 비공개 동영상이 존재할 경우 에러 발생
