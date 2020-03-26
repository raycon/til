# Git username and email

## 모든 저장소에 적용되는 설정

Git username 설정 :

    git config --global user.name "User Name"
    git config --global user.email "user@email.com"

Git username 확인 :

    git config --global user.name
    > User Name
    git config --global user.email
    > user@email.com

`~/.gitconfig` 파일에 다음과 같이 저장된다 :

    [user]
        email = user@email.com
        name = User Name

## 특정 저장소에 적용되는 설정

`--global` 옵션을 빼고 설정한다.

    git config user.name "User Name"
    git config user.email "user@email.com"

## 특정 폴더에 적용되는 설정

특정 폴더에만 설정을 다르게 적용할 수 있다. `~/.gitconfig` 파일에 다음 내용을 추가한다. 다음 예제는 폴더 경로에 `github`가 포함되면 `~/.githubconfig`를 사용하도록 설정한다.

    [includeIf "gitdir:*/github/*"]
        path = ~/.githubconfig

`~/.githubconfig`를 다음과 같이 설정한다.

    [user]
        email = github.email@gmail.com
        name = github.name

## 리모트 저장소에 적용되는 설정

Github, Bitbucket 등과 같은 리모트 저장소에서 Commit이 구분되는 방법 :

- Commit은 **이메일 주소**로 구분된다.
    - `user.email`을 갖는 회원이 있을 경우 프로필에 설정된 이름을 표시한다.
    - `user.email`을 갖는 회원이 없을 경우 commit 로그의 `user.name`을 표시한다.
- `Github`
    - 커밋로그에 개인 이메일이 남는게 싫을 경우 Github이 제공하는 `noreply` 이메일을 사용한다.
    - [About commit email addresses](https://help.github.com/articles/about-commit-email-addresses/) 참조
