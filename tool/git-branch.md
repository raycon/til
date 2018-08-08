# Git branch

> <https://git-scm.com/book/ko/v1/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EC%99%80-Merge%EC%9D%98-%EA%B8%B0%EC%B4%88> 참고

## Checkout

브랜치 만들기:

    $ git branch hotfix

브랜치 변경:

브랜치를 변경할 때에는 워킹 디렉토리를 정리하는 것이 좋다.

    $ git checkout hotfix

브랜치를 만들고 체크아웃:

    $ git checkout -b hotfix
    Switched to a new branch 'hotfix'

브랜치 합치기:

    $ git checkout master
    $ git merge hotfix

브랜치 삭제:

    $ git branch -d hotfix

## Merge

Merge 종류:

- Fast Forward: 브랜치의 포인터가 앞으로 이동한다.
- 3-way Merge: 각 브랜치가 가리키는 커밋 두 개와 공통 조상 하나를 사용하여 merge한다. merge의 결과를 별도의 커밋으로 만들고 브랜치의 포인터가 그 커밋을 가리키도록 이동한다.

Merge 충돌:

Merge 하려는 두 브랜치에서 같을 파일의 한 부분을 동시에 수정했을 경우 충돌이 발생한다. 이 때는 새로운 커밋이 생성되지 않는다. `git status` 명령어로 어떤 파일이 충돌이 났는지 확인할 수 있다.

    $ git status
    On branch master
    You have unmerged paths.
      (fix conflicts and run "git commit")

    Unmerged paths:
      (use "git add <file>..." to mark resolution)

            both modified:      index.html

    no changes added to commit (use "git add" and/or "git commit -a")

unmerged 상태의 파일을 열어서 충돌된 내용을 확인하고 수정한다. `git add` 명령으로 충돌이 해결된 파일을 Staging area에 저장한다. 커밋할 때는 어떻게 충돌을 해결했고 좀 더 확인해야 하는 부분은 무엇을 어떻게 했는지 자세하게 기록한다.

Merge 취소:

충돌이 발생한 이후 Merge를 취소하려면 다음 명령어를 입력한다.

    git merge --abort

## Mergetool

충돌이 있는 파일을 수정할 때에는 `git mergetool` 명령어로 외부 프로그램을 실행할 수 있다. Merge 도구를 종료하면 Git은 잘 Merge했는지 물어본다. 잘 마쳤다고 입력하면 자동으로 `git add`가 수행되고 해당 파일이 Staging Area에 저장된다.

### VSCode

`~/.gitconfig` 파일에 아래 내용을 추가한다.

    [merge]
        tool = vscode
    [mergetool]
      keepBackup = false
    [mergetool "vscode"]
        cmd = code --wait $MERGED
    [diff]
        tool = vscode
    [difftool "vscode"]
        cmd = code --wait --diff $LOCAL $REMOTE

`keepBackup`은 `.orig` 파일을 생성하지 않기 위해 `false`로 지정한다.

### KDiff3

최신버전을 [다운로드](https://sourceforge.net/projects/kdiff3/files/latest/download)한다.

`~/.gitconfig` 파일에 아래 내용을 추가한다.

    [merge]
      tool = kdiff3
    [mergetool]
      keepBackup = false
    [mergetool "kdiff3"]
      path = C:/Program Files/KDiff3/kdiff3.exe
      trustExitCode = false
    [diff]
      guitool = kdiff3
    [difftool "kdiff3"]
      path = C:/Program Files/KDiff3/kdiff3.exe
      trustExitCode = false