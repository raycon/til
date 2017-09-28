# Git in bash

> bash 에서 git 정보를 프롬프트에 보여줄 수 있다.

`bash-git-prompt`를 클론한다.

    git clone https://github.com/magicmonty/bash-git-prompt.git ~/.bash-git-prompt --depth=1

`~/.bashrc`에 아래 내용을 추가한다.

    GIT_PROMPT_ONLY_IN_REPO=1
    source ~/.bash-git-prompt/gitprompt.sh

git 저장소 폴더로 이동하면 다음과 같이 표시된다.

    ✔ ~/workspace/code/TIL [master|✚ 1…4]