import json
import subprocess

# 서브프로세스 실행을 통한 ffmpeg 실행함수
def ffmepg(commandline):
    result = subprocess.Popen(commandline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = result.communicate()
    exitcode = result.returncode
    if exitcode != 0:
        print(exitcode, out.decode('utf8'), err.decode('utf8'))
    else:
        print('Completed')


# json 파싱 및 테스트
json_data = json.load(open('ffmpeg.json',encoding='UTF8'))
clipList = json_data["clipList"]
soundList = json_data["soundList"]
captionList = json_data["captionList"]

for clip in clipList:
    videoFile = clip["videoFile"]
    videoPlayStartPosition = clip["videoPlayStartPosition"]
    videoPlayDuration = clip["videoPlayDuration"]

for sound in soundList:
    soundFadeInDuration = sound["soundFadeInDuration"]
    soundFadeOutDuration = sound["soundFadeOutDuration"]
    soundFile = sound["soundFile"]
    soundPlayStartPosition = sound["soundPlayStartPosition"]
    soundPlayDuration = sound["soundPlayDuration"]
    soundRepeat = sound["soundRepeat"]
    soundVolume = sound["soundVolume"]
    resultPlayStartPosition = sound["resultPlayStartPosition"]
    resultPlayDuration = sound["resultPlayDuration"]


# 테스트를 위해 index를 추가함, 없어도 무관
for index, caption in enumerate(captionList):
    text = caption["text"]
    textAlign = caption["textAlign"]
    textColor = caption["textColor"]
    textFontFile = caption["textFontFile"]
    textFrameImageFile = caption["textFrameImageFile"]
    resultPlayStartPosition = caption["resultPlayStartPosition"]
    resultPlayDuration = caption["resultPlayDuration"]

    # 글자정렬을 ffmpeg에서 지원하는 양식에 맞게 변경
    if textAlign == "center":
        textAlign = ":x=(w/2-tw/2)" # w = 화면너비 / tw = 텍스트너비
    elif textAlign == "right":
        textAlign = ":x=(w-tw-10)"
    else:
        textAlign = ":x=10"

    # 글자색을 ffmpeg에서 지원하는 컬러포맷에 맞게 변경 #AARRGGBB -> 0xRRGGBBAA
    textColor = "0x" + textColor[3:] + textColor[1:3]

    # ffmpeg에서 fontfile 인자 전달시 한글 사용 안 됨. 추후 해당 앱에서 지원하는 폰트들을 일일이 파싱 해주거나 클라와 협의 필요
    if textFontFile == "야놀자 야체 Bold.ttf":
        textFontFile = "font/yanolzaBold.ttf"
    elif textFontFile == "야놀자 야체 Regular.ttf":
        textFontFile = "font/yanolzaRegular.ttf"

    # 테스트용 커맨드라인 생성 및 실행
    commandline = 'ffmpeg -y -i videoA.mp4 -filter_complex "[0:v]drawtext=text='+text+':fontsize=20'+textAlign+\
                  ':y=h*0.9:fontcolor='+textColor+':fontfile='+textFontFile+'" output'+str(index)+'.mp4'

    ffmepg(commandline)