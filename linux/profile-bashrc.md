# .profile .bashrc .bash_profile

`man bash`에 다음과 같은 내용이 있다.

    /bin/bash
          The bash executable
    /etc/profile
          The systemwide initialization file, executed for login shells
    ~/.bash_profile
          The personal initialization file, executed for login shells
    ~/.bashrc
          The individual per-interactive-shell startup file
    ~/.bash_logout
          The individual login shell cleanup file, executed when a login shell exits
    ~/.inputrc
          Individual readline initialization file

다음과 같이 이해하면 된다.

- `.profile` : 로그인 할 때, bash와 관련 없는 내용 (환경변수 등)을 설정할 때 사용한다.
- `.bashrc` : bash 실행 할 때, bash 관련 설정은 여기에 추가한다.
- `.bash_profile` : bash 로그인 할 때, 16.04 버전에서 이 파일은 기본으로 존재하지 않는다. Ubuntu 데스크탑에서 터미널 실행 시 로드되지 않는다.