 # TIL (Today I Learned)



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



---



## <span style="color:#DF01A5">Typora</span>

* 문서의 논리적 흐름 `#`
  - 대제목, 소제목 쓸 때 사용
  - **주의!** 글씨 크기를 키우기 위해 사용하지 않는다. 

* 인용문 `>`

* 리스트 `*`  or  `-`

  - tab으로 안으로 들어간다. 
  - shift +tab으로 밖으로 나온다.

* 이미지 `![보여질 제목][실제 링크]`

* 링크 `[보여질 제목][실제 링크]`

* 수평선 만들기 `---`

* 표 만들기 `| space |  enter`

  







