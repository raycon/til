# Git remote repository

원격 저장소 목록 출력 :

    $ git remote -v
    origin  git://github.com/schacon/ticgit.git (fetch)
    origin  git://github.com/schacon/ticgit.git (push)

원격 저장소 추가 :

    $ git remote add pb git://github.com/paulboone/ticgit.git
    $ git remote -v
    origin  git://github.com/schacon/ticgit.git
    pb  git://github.com/paulboone/ticgit.git

원격 저장소 이름 변경 :

    $ git remote rename pb paul
    $ git remote
    origin
    paul

원격 저장소 주소 변경 :

    $ git remote set-url origin https://github.com/user/repo2.git
    # Change the 'origin' remote's URL

원격 저장소 삭제 :

    $ git remote rm paul
    $ git remote
    origin