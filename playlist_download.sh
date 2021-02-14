#!/bin/bash
# 윈도우 작성 스크립트일시 아래 명령어를 한번 실행후 사용하기
# sed -i -e 's/\r$//' [대상 파일]
arr_playlists=("https://www.youtube.com/playlist?list=PL8uzAiCio-SEKN0g7v46Dn3nU3BFWLcD7" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SE2BQrc8u7qilw06CD7LU3w" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SH1-_3sh_e9osCO4QZ_Gdk_" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SGHXZyqrFw-eWJ-m_Uj1TsS" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SHN-QrbgcKFUsSn0u3eZPeR" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SGdalMT9i0Xmx5qzoLjmevt" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SHX_SnfRmlJM6Zq8F1jNqmS" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SEF01u6LWEHbvKZn4B3UjDc" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SHYEjCAUyJP8Q2CLnrwRYkT" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SH5P2oxELeZ092xP6XUrUH5" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SECLpeqm00RLUqHbI--23lE" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SFW7iEQI78-J6zxXuAc_tq3" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SHzDI0rpYGmc_IV4Q9hFnef" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SHeMjzKzzgGVNvhfNNbfaMx" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SFukGOKEq9nJR74wNZMDTpU" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SFnU576rYfOsQirrQHKQ4D7" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SFC4srkfgfOFlbvnGGLqQ5t" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SEA3g4BvezGLtXKe-MZYJm8" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SFzo0M_gm70CUvvndQD50rP" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SE_GKkmsuXAuHxN_pyroxfT" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SFG5Rduvdc1o86GJxAcFfS-" \
"https://www.youtube.com/playlist?list=PL8uzAiCio-SHQoM1yJ-jwzHHN3-4AAGWg")

for i in ${arr_playlists[@]}; do
    youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o './download_video/%(title)s.%(ext)s' $i
done
echo "Finish"

# 플레이리스트에 비공개 동영상이 존재할 경우 에러 발생 
