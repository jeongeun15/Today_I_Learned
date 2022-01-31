# TIL (Today I Learned)



## <span style="color:#DF01A5">Git 명령어 정리</span>

1. `git init`
   - 현재 폴더를 깃이 관리하는 폴더로 만들어줘
2.  `git status`
   - 현 상황을 보고싶어
3.  `git add a.txt`
   - 무대에 올리기 
   - `git add .` 전부 다 올리기
4. `git commit -m "메시지"`
   - 찰칵! 후 저장소
5. `git log`
   - 버전들 확인할래
   - Author, Date 등이 나옴

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

    

