# MySQL 변수 사용하기

> <https://stackoverflow.com/questions/11754781/how-to-declare-a-variable-in-mysql> 참고

초기화:

    SET @start = 1, @finish = 10;
    or
    SELECT @start := 1, @finish := 10;

사용:

    SELECT * FROM places WHERE place BETWEEN @start AND @finish;


