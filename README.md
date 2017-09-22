## Google Speech API with Python + Django

### Purpose
- Using google speech API easily
- Easy follow-up web page for non-developers or beginners
- Upload audio files easily by one-click in web browser 
- Automatically convert to Flac(format that supporting by Google Speech API)

### Workflow
1. Upload audio to web: Flac is recommended, but other formats such as mp3, wav are possible.
> Currently google only supports Flac and LINEAR16.    
> (My guess) It's for increasing accuracy.    
> But I can pull out prett accurate result by mp3 file (after encoding to Flac format).

2. Converting file to Flac format(optional): If audio file is not Flac, automatically convert the file to Flac format with mono type.
> Currently google speech API only supports mono type of audio, not stero. You can easily change the file itself using program like [Audacity](http://www.audacityteam.org/) or [GoldWave](https://www.goldwave.com/). But it's more convenient that one-click uploading.
ㅏ
3. Call request to Google Speech API and return response: If needed, you have to register for google API service. (Maybe later, I will give some easy tutorial or folling contents inside web page for non-programmer)
> If the files are under 1MB or 1 min, you can use just `https://speech.googleapis.com/v1/speech:recognize`. If not, you can use `https://speech.googleapis.com/v1/speech:longrunningrecognize`.     
> If needed, you have to give your `API key` and `Access Token` for call API.

4. Return parsed text result: After receiving result json data, django web page automatically parse json to text. If needed, you can access the json itself.


### TODO
**HotTODO**
- [X]: bitrate 수정하기 (파일에 맞는 bitrate로)
- [X]: staff 권한-home 제외한 페이지에는 staff만 접근 가능
- [X]: suwon 권한-home에서 help-text는 suwon0126에서만
- [X]: 파일 변환중일 때 doing 관련 수정하기-test 필요?
- [X]: notice list bookmark 기능
- [ ]: 배포- docker 사용해서해보기
- [ ]: List page - mdl card 사용해서 front 정렬
- [ ]: List page - speech 완료시 자동으로 변환 파일(docx) 만들어서 업로드 + 변환 status = True

**optional**
- [ ]: react 사용해서 notice 공지 열기/닫기 추가
- [ ]: react 사용해서 filter text 해보기
- [ ]: session; guest일시 session 주기, session 타임아웃 설정(notice crawling 위해서) - 보류, 현재 refresh 버튼 사용
- [ ]: home - 날씨 api 프론트 수정
- [ ]: home - 고려대학교 대학원 공지 붙이기
- [ ]: 고려대 공지 cron/celery로 주기적으로 가져오기
- [ ]: home - 현대시봇, 역사봇 붙이기(db 가져오기)
- [ ]: 수정 완료 text 올리면 수정 후 docx 파일로 저장?
- [ ]: Divide audio file less than 15 min-시간 표시를 위해서 (`https://cloud.google.com/speech/docs/async-time-offsets#speech-async-recognize-gcs-protocol` 참고)
- [ ]: operation이 완료시 알람? 혹은 이메일로 결과값 전송 => 완료시 체크 가능하게 % 표시? (변환중 -> 변환완료) maybe cron or celery
- [ ]: home 만들기-학기 종료시까지 남은 기간을 달리기로 표시 (react?)
- [ ]: 번호 로그인? (캡차 권한 달아보기-번호 인증시에 staff 권한 부여 가능하게)
- [ ]: Notice list page에서 더 보기 기능 구현

**User request**
- [X]: 파일 다운로드 유틸 (mp3 파일을 다운로드)
- [X]: mp3 파일을 자동으로 flac으로 변환 (mono type, 44100)
- [X]: Upload to google cloud api (After divide audio)-utils-upload_cloud 사용
- [X]: content 모델 필드에 저장
- [X]: Save as other file (word file format? or etc)
- [X]: email 등록(smtp)
- [X]: home - 날씨 api로 날씨 표시
- [X]: home - 날씨 api 클릭하면 바로 넘어가게 수정
- [X]: home - 메일 api (daum)

**하드코딩 리펙토링**
- [X]: google storage bucket, api name 하드코딩 리팩토링하기
- [ ]: 페이지별 타이틀 수정하기
- [ ]: Speech List View => 현재는 UploadView로 하드코딩, 추후 formview or ListView로 리팩토링
- [ ]: Convert 했을 때 post_save_signal => FormView에서 모델을 만든 직후, request를 뿌려주고 api는 api대로 그냥 보내면 끊김 없이 될듯? FormView에서 언제 만들어지는지 확인 필요
- [ ]: 변환하기 눌렀을 때 바로 도는게 아니라 페이지 redirect 후 돌리기? 혹은 post 보냈을 때 돌리기(background에서)-firebase? 추후 refactoring

**Making Site**
- [X]: Complete speech call function
- [ ]: Complete front done (MDL + a)
- [ ]: Making DEMO site
- [ ]: Add translation func to Model verbose_name
- [X]: Making AWS server
- [ ]: Deploy

**About Speech API**
- [ ]: Making speech-api tutorial for beginners
