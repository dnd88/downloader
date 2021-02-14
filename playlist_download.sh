#!/bin/bash
arr_playlists=("https://www.youtube.com/playlist?list=PL8uzAiCio-SEKN0g7v46Dn3nU3BFWLcD7" "https://www.youtube.com/playlist?list=PL8uzAiCio-SE2BQrc8u7qilw06CD7LU3w")

for i in ${arr_playlists[@]}; do
    youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o './download_video/%(title)s.%(ext)s' $i
done
echo "Finish"
