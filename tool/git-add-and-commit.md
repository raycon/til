# Git add and commit in one command

일반적인 파일 추가 후 커밋 하는 방법

    git add .
    git commit -m "message"

은 귀찮다

alias 를 지정해서 사용하면 편하다

    git config --global alias.ac '!git add -A && git commit -m'
