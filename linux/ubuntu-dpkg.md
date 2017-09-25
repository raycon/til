# Ubuntu dpkg

우분투에서 deb 파일을 사용해서 패키지를 설치, 삭제하는 방법

설치 :

    sudo dpkg -i /home/user/app.deb


패키지 상태 확인 :

    dpkg -s app

패키지 삭제 (설정 파일 미포함) :

    sudo dpkg -r app

패키지 삭제 (설정 파일 포함) :

    sudo dpkg -P app