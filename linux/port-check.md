# 어떤 포트를 쓰고 있는지 확인하는 방법

출처 : <http://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EB%A1%9C%EC%BB%AC%EC%84%9C%EB%B2%84_%EC%97%B4%EB%A6%B0_%ED%8F%AC%ED%8A%B8_%ED%99%95%EC%9D%B8>

    netstat -tnlp
    lsof -i -nP | grep LISTEN | awk '{print $(NF-1)" "$1}' | sort -u
    nmap localhost