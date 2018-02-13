# Kibana

## 설치

키바나를 [다운로드](https://www.elastic.co/downloads/kibana) 한다.

압축을 풀고 `경로/bin`을 환경변수 `PATH`에 등록한다.

    ex: `C:\dev\tools\kibana-6.1.2-windows-x86_64\bin`

압축을 풀고 `config/kibana.yml`을 다음과 같이 수정한다.

    # The URL of the Elasticsearch instance to use for all your queries.
    elasticsearch.url: "http://localhost:9200"

키바나를 실행한다.

    > kibana

브라우저로 `http://localhost:5601`에 접속한다.