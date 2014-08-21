[Deploy to GoogleAppEngine with SublimeText2]

0. 사건의 발단
MacOS에서 지원하는 아이디/비밀번호 저장하기가 탐났음

1. Save ID/PASSWD 
MENU - cmd
code> python (appcfg.py path) --oauth2 update (project path)
e.g.> python "C:\Program Files (x86)\Google\google_appengine\appcfg.py" --oauth2 update "C:\Users\pjhjohn\Desktop\test-gae-projects\test-gallery"

[장점]
- 최초 시도시 허가를 요하는 웹창이 뜨고, 이걸 승인하면 이후 해당 코드에 대해 아이디/비밀번호를 묻지 않음
- cmd창에서 위쪽 키를 누르면 바로 이전 명령어가 보이기 때문에 위-엔터 로 간단하게 디플로이 가능
- Deploy log를 위한 별도의 창이 생기지 않음
- update -> rollback 으로만 바꿔주면 롤백할 수 있다.
- 익숙해지면 코드 치는것도 별로 불편하지 않다.
[단점]
- 여러개의 google 계정을 사용하려면 저걸 해제해줘야 하는 불편함이 있음.
- cmd가 싫다
- cmd 켤 때마다 일일이 마우스 우클릭을 하기 귀찮다

2. With Sublime
[장점]
- SublimeText2 안에서 다 할 수 있다.
- 코드 붙여넣기 안해도 된다
- (사실 이제 맨날 디플로이 할 상황이므로) 확실히 편할 듯.
- 여전히 로그인 안해도 됨.

[설치 방법]
0. "Deploy AppEngine Project.sublime-build"를 복사.
1. Preferences > Browse Packages 를 클릭하면 Package라는 폴더가 하나 나온다.
2. User로 들어가서 "Deploy AppEngine Project.sublime-build"를 붙여넣기 한다.
3. "Deploy Current Project.sublime-build" 에서, appcfg.py와 프로젝트 폴더명을 재설정해준다.
3. Tools > Build System > Deploy AppEngine Project
4. 이때부터는 ctrl+b로 디플로이가 가능. [Tools > Build 에 있는 단축키]

[단점]
- Deployment Log가 디플로이 종료 후 나타난다.
- 디플로이를 한번 더 실행하면 로그가 덮어씌워진다.
- rollback을 하거나 프로젝트 경로를 바꾸고 싶다면 "Deploy AppEngine Project.sublime-build" 파일을 수정해야 한다.