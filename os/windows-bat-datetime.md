# 배치 파일에서 날짜, 시간 쓰는법

    @echo off
    set YE=%date:~2,2%
    set MO=%date:~5,2%
    set DA=%date:~8,2%
    set HH=%time:~0,2%
    set MM=%time:~3,2%
    set SS=%time:~6,2%
