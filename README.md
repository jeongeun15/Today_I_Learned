# Today_I_Learned

## <span style="color:#DF01A5">Git</span>



>  오른쪽 마우스 클릭  ->  더 많은 옵션 보기  -> Git Bash Here

* 명령어  `start.`
* 시간 `date`
* 루트, 홈 디렉토리 `~`
* 현재 디렉토리 내의 폴더 & 파일을 보여줌 `ls`(list segments)
  - all 숨긴 폴더 & 파일까지 `ls -a`
* 스크롤 내리기 `ctrl + l`
* 다 없애기 `clear`
* 최근 기입 확인 ` 화살표 키`
* 앞, 뒤 이동 `ctrl + a, e`



### <span style="color:#F8B2DF">경로</span>

> 상대경로 =  내 위치 기준
>
> 절대경로 = 어디든 상관없는 위치

* '파일'을 만드는 경우 `touch a.txt`

* '폴더' 만들기 `mkdir 폴더이름` (make directory)

* 다른 폴더로 이동하기 `cd` (change directory)

  - .  => 현재 위치

    현재 위치로 이동 `cd .`

  - .. => 현재 위치에서 상대 경로로 상위

    상위 폴더로 이동 `cd ..`

* 이동 + 이름 바꾸기 `mv`

* 제거 `rm`

  - 파일 삭제  `rm a.txt`
  - 폴더 삭제 `rm -r 폴더이름`
  - 모든 파일 삭제 `rm *.txt`

  ​       이건 절대 쓰지 않기! 

  ​       '*' : asterisk , wildcard  ->  all 이라는 뜻

  

### <span style="color:#F8B2DF">깃 명령어 정리</span>

* `git init`
  - 현재 폴더를 깃이 관리하는 폴더로 만들어줘
  - **홈폴더에서 기입하지 않기!**
  - 내가 관리하고 싶은 최상의 폴더 하나에만 기입
* `git status`
  - 현 상황을 보고싶다
* `git add a.txt`
  - 전부 다 올리기
* `git commit -m "메시지"
  - 찰칵! 후 저장소
* `git log`
  - 버전들 확인하기

  ## <span style="color:#DF01A5">Git 명령어 정리</span>



* Please tell me who you are. 이라고 나오면 아래와 같이 입력

  `git config --global user.name "본인 깃허브 아이디"`

  `git config --global user.email "이메일"`

* 확인하기 `git config --global --list` 

* 유저 이름이랑 이메일 수정하고 싶을때

  - 기존 저장되어 있던 이름, 이메일 삭제 

  ​       `git config --global --unset user.name`

  ​       `git config --global --unset user.email`

  - 새로 입력

    `git config --global user.name "깃허브 아이디"`

    `git config --global user.email "이메일"`

* 돌아가보기

  `git checkout 해쉬값`

   (git log --oneline 치면 앞에 노란색으로 나오는게 해쉬값이다.)

  `git checkout head~3`

* 다시 나오기

  `git checkout master`

6. 브릿지 잇기

   `git remote add origin 주소`

   이어진거 확인

   `git remote -v`

7. 깃허브에 올리기

   `git push origin master`

   

   <span style="color:thistle">**순서**</span>

   git init -> git add . -> git commit -m'메세지' -> git remote add origin 주소 -> git remote -v -> git push origin master 

   

* 특정 파일과 폴더를 올리기 싫을 때

   vscode에 `touch .gitignore`  입력하여 생성하기

  - gitignore에 올리기 싫은 파일을 입력하고 git init을 입력하면 올리기 싫은 파일에만 U가 생성되지 않는다. 
  - add하기 전에 올리기 싫은 파일을 저장해놔야 된다.

* `git clone 주소`

  -  복제된 폴더 자체를 이 장소로 가져와죠!

  - 복제할때 폴더째로 복제해 오기 때문에 그 장소로 복제한 폴더를 가져온다. 홈폴더에서 해도 된다.
