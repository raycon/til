# Elasticsearch Field

매핑으로 필드 추가:

    PUT '{{index}}/_mapping/{{type}}'
    {
      "{{type}}" : {
        "properties" : {
            //your new mapping properties
        }
      }
    }

쿼리로 필드 추가:

[Update by query](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-update-by-query.html) 참고

    POST {{index}}/_update_by_query?conflicts=proceed
    {
      "script": {
        "source": "ctx._source.test_field=1000"
      }
    }

`wait_for_completion=false` 옵션을 주면 `task`를 응답으로 받는다. [Task API](https://www.elastic.co/guide/en/elasticsearch/reference/current/tasks.html)를 통해서 상태를 확인하거나 취소할 수 있다.

필드 이름 변경, 삭제:

만들어진 필드를 삭제할 수는 없다. 새로운 인덱스를 만들어서 매핑을 변경하는게 최선이다. 인덱스를 변경하는 동안 서비스 다운이 발생할 수 있으므로 아래 내용을 참고한다.

- [서비스 중단 없이 인덱스 변경](https://www.elastic.co/guide/en/elasticsearch/guide/current/index-aliases.html#index-aliases)
- [Reindex API 사용](https://stackoverflow.com/questions/43120430/elasticsearch-mapping-rename-existing-field)