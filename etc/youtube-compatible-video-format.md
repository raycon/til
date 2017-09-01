# 유투브 업로드용 영상 만들기

> <https://support.google.com/youtube/answer/1722171?hl=ko>

## Davinci Resolve Deliver

Youtube 선택 > 1080p 선택

비디오 : QuickTime H.264
오디오 : AAC 192Kb/s

## MP4 변환

ffmpeg -i in.mov -vcodec copy -acodec aac -strict -2 -b:a 384k out.mp4
ffmpeg -i in.mov -vcodec copy -acodec copy out.mp4

```bat
for %%a in ("*.mov") do ffmpeg -i "%%a" -codec:v libx264 -crf 21 -bf 2 -flags +cgop -pix_fmt yuv420p -codec:a aac -strict -2 -b:a 384k -r:a 48000 -movflags faststart "convert\%%~na.mp4"
pause
```