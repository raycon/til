# Git 로그 출력

- <https://git-scm.com/book/ko/v1/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%BB%A4%EB%B0%8B-%ED%9E%88%EC%8A%A4%ED%86%A0%EB%A6%AC-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0>
- <https://www.atlassian.com/git/tutorials/git-log>
- <https://coderwall.com/p/euwpig/a-better-git-log>

기본 :

    $ git log

한줄로 표시:

    $ git log --oneline

한줄에 그래프 표시:

    $ git log --oneline --graph

수정사항 표시:

    $ git log -p

수정된 통계 정보 표시:

    $ git log --stat

author 단위로 그루핑해서 수정 표시:

    $ git log --shortlog

Pretty 적용:

    $ git log --pretty=[oneline, full, fuller]

Format 적용:

    $ git log --pretty=format:"%h - %an, %ar : %s"

## 필터링

갯수 제한:

    $ git log -2

커밋 날짜 제한:

    $ git log --after="2018-1-1"
    $ git log --after="yesterday"
    $ git log --after="2 years 1 day 3 minutes ago"
    $ git log --after="2017-1-1" --before="2018-1-1"

Author 제한:

    $ git log --author="John"
    $ git log --author="John\|Mary"

커밋 메시지로 제한:

    $ git log --grep="JRA-224:"

특정 파일로 제한:

    $ git log -- foo.py bar.py

수정된 컨텐츠로 제한:

    $ git log -S"Hello, World!"

두 브랜치의 공통 조상으로부터 조회:

    $ git log <since>..<until>
    $ git log master..feature

Merge 커밋만 조회:

    $ git log --merges

Merge 커밋 제외:

    $ git log --no-merges

## 기본 출력 변경

`--pretty` 옵션을 기본으로 지정하려면 `~/.gitconfig`에 다음 내용을 추가한다.

    [format]
      pretty = %h - %an, %ar : %s

alias 를 지정해서 편리하게 사용할 수 있다.

    [alias]
      lg = "log --pretty=format:'%Cred%h %Creset%ad %Cblue%an %Creset-%C(yellow)%d %Creset%s' --abbrev-commit --date=format:'%Y-%m-%d' --graph --color"
