# Install Ubuntu

## 파티션 나누기

- Swap : 메모리의 1~2배로 잡는다.
- /home : 홈 영역으로 설정할 크기. 파티션 지정해놔야 나중에 재설치할 때 편리하다.
- / : 나머지 영역 전체 지정

## 네트워크 설정

- `/etc/environment`에 [프록시 설정](../etc/proxy-settings.md) 추가
- `System Settings > Network > Network proxy`에 IP 및 프록시 설정 추가

## apt-get 업데이트

    sudo apt-get update

## Samba 설치

    sudo apt-get install samba
    sudo vi /etc/samba/smb.conf

접속을 허용할 IP 입력

    ;  interfaces = 127.0.0.0/8 eth0
    hosts allow = a.b.c.d

공유할 폴더 입력

    [Downloads]
      comment = Ubuntu Downloads
      path = /home/user/Downloads
      writable = yes
      guest ok = yes
      create mask = 0664
      directory mask = 0755
      browsable = yes
      public = no

삼바 재시작

    sudo service smbd restart

## Synergy 설치

[공식 홈페이지](https://symless.com) 에서 구매하는게 속 편하다.

## Eclipse 설치

- [공식 홈페이지](http://www.eclipse.org) 에서 EE 버전을 받는다.
- `tar.gz` 압축을 풀고 `/opt/eclipse`에 복사한다.
- [데스크톱 아이콘](create-desktop-icon.md)을 만든다.

## JAVA 설치

    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer

## SDKMAN 설치

[SDKMAN](http://sdkman.io/install.html) : 패키지 관리해주는 프로그램.

다음 명령어는 sudo로 실행하지 않아도 된다.

    curl -s "https://get.sdkman.io" | bash
    source "$HOME/.sdkman/bin/sdkman-init.sh"
    sdk version

## gradle 설치

    sdk install gradle 4.2

## Unity Tweak Tool 설치

    sudo apt-get install unity-tweak-tool

`Dash > Unity Tweak Tool` 실행해서 다음 항목 설정

Launcher :

- 투명도 0
- Position Bottom
- Icon size 36

Panel :

- 투명도 100
- Indicators > Date 체크

Switcher :

- 모두 체크 해제

Numix 테마 설치 :

    sudo add-apt-repository ppa:numix/ppa
    sudo apt-get update
    sudo apt-get install numix-*

- Theme > Numix
- Icons > Numix Circle

## Theme 설치

    sudo add-apt-repository ppa:noobslab/themes
    sudo apt-get update

여러 테마를 설치할 수 있다.

## Chrome 설치

    sudo dpkg -i google-chrome-stable_current_amd64.deb
    sudo apt-get -f install

## Monaco Linux 폰트 설치

- 폰트 [다운로드](https://github.com/hbin/top-programming-fonts/raw/master/Monaco-Linux.ttf)
- `~/.local/share/fonts` 에 추가
- `sudo fc-cache -fv`

## Consolas-powerline-vim 폰트 설치

    git clone https://github.com/eugeii/consolas-powerline-vim.git
    cp consolas-powerline-vim/CONSOLA* ~/.loca/share/fonts/
    fc-cache -fv
    rm -rf consolas-powerline-vim/

## VSCode 설치

[Running VS Code on Linux](https://code.visualstudio.com/docs/setup/linux) 참조

    sudo dpkg -i <file>.deb
    sudo apt-get install -f # Install dependencies