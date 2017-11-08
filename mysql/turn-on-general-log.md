# Turn on general log

MySQL에 입력되는 쿼리를 모두 확인하고 싶을 때, General Log를 활성화 하면 된다.

    SET global general_log_file='c:/Temp/mysql.log';
    SET global general_log = on;
    SET global log_output = 'file';