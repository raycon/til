# Elasticsearch Example

## 설치

엘라스틱 서치를 [다운로드](https://www.elastic.co/downloads/elasticsearch)한다.

압축을 풀고 `경로/bin`을 환경변수 `PATH`에 등록한다.

    ex: `C:\dev\tools\elasticsearch-6.1.2\bin`

엘라스틱 서치를 실행한다

    > elasticsearch

브라우저로 `http://localhost:9200`에 접속한다.

    // 20180130163000
    // http://localhost:9200/

    {
      "name": "sOd4mHx",
      "cluster_name": "elasticsearch",
      "cluster_uuid": "xJFlOTLPS7aYWqe6-_hC6Q",
      "version": {
        "number": "6.1.2",
        "build_hash": "5b1fea5",
        "build_date": "2018-01-10T02:35:59.208Z",
        "build_snapshot": false,
        "lucene_version": "7.1.0",
        "minimum_wire_compatibility_version": "5.6.0",
        "minimum_index_compatibility_version": "5.0.0"
      },
      "tagline": "You Know, for Search"
    }

## Cluster name

엘라스틱서치 경로의 `config/elasticsearch.yml` 파일의 다음 부분을 수정해서 클러스터 이름을 변경할 수 있다.

    cluster.name: application


## 데이터 구조

    RDBMS         : Database  Table   Row       Column    Scheme
    ElasticSearch : Index     Type    Document  Field     Mapping

## HTTP Method

    POST    : Create
    GET     : Read
    PUT     : Update
    DELETE  : Delete

### PUT을 이용한 데이터 생성

`/index/type/id` 로 URL을 구성한다.

    PUT http://localhost:9200/songs/song/1
    {
        "title": "Song Title"
    }

기존에 없던 id 값을 넣으면 `result` 값이 `created`로 전달된다.

    {
        "_index": "songs",
        "_type": "song",
        "_id": "1",
        "_version": 1,
        "result": "created",
        "_shards": {
            "total": 2,
            "successful": 1,
            "failed": 0
        },
        "_seq_no": 0,
        "_primary_term": 1
    }

동일한 값을 한번 더 입력하면 `result` 값이 `updated`로 전달되고, `_version`이 증가한다.

    {
        "_index": "songs",
        "_type": "song",
        "_id": "1",
        "_version": 2,
        "result": "updated",
        "_shards": {
            "total": 2,
            "successful": 1,
            "failed": 0
        },
        "_seq_no": 1,
        "_primary_term": 1
    }

### GET을 이용한 데이터 조회

    GET http://localhost:9200/songs/song/1

`_source`로 입력했던 데이터가 전달된다.

    {
        "_index": "songs",
        "_type": "song",
        "_id": "1",
        "_version": 2,
        "found": true,
        "_source": {
            "title": "Song Title"
        }
    }

없는 값을 조회 할 경우 `found`값이 `false`로 전달된다.

    {
        "_index": "songs",
        "_type": "song",
        "_id": "3",
        "found": false
    }

### POST를 이용한 데이터 입력

POST를 이용하면 ID를 생략하고 입력할 수 있다.

    POST http://localhost:9200/songs/song
    {
        "title": "Post Song Title"
    }

임의의 ID로 Document가 생성된다.

    {
        "_index": "songs",
        "_type": "song",
        "_id": "ixS8VWEBqs8auCt1hcOw",
        "_version": 1,
        "result": "created",
        "_shards": {
            "total": 2,
            "successful": 1,
            "failed": 0
        },
        "_seq_no": 0,
        "_primary_term": 1
    }

### DELETE를 이용한 데이터 삭제

    DELETE http://localhost:9200/songs/song/ixS8VWEBqs8auCt1hcOw

`result` 값이 `deleted`로 전달된다.

    {
        "_index": "songs",
        "_type": "song",
        "_id": "ixS8VWEBqs8auCt1hcOw",
        "_version": 2,
        "result": "deleted",
        "_shards": {
            "total": 2,
            "successful": 1,
            "failed": 0
        },
        "_seq_no": 1,
        "_primary_term": 1
    }

이를 다시 GET 으로 조회해보면 `found`값이 `false`로 전달된다. 메타 정보는 유지되기 때문에 동일한 ID로 다시 입력하면 `_version`이 계속 증가한다.

    {
        "_index": "songs",
        "_type": "song",
        "_id": "ixS8VWEBqs8auCt1hcOw",
        "_version": 8,
        "result": "created",
        "_shards": {
            "total": 2,
            "successful": 1,
            "failed": 0
        },
        "_seq_no": 9,
        "_primary_term": 1
    }

### Bulk API

`/_bulk` API API를 사용하면 한번의 요청으로 여러 데이터를 변경할 수 있다. 다음과 같은 JSON 형태여야 한다.

    action_and_meta_data\n
    optional_source\n
    action_and_meta_data\n
    optional_source\n
    ....
    action_and_meta_data\n
    optional_source\n

사용 가능한 액션은 다음과 같다.

- `index` : 생성하거나 업데이트한다.
- `create` : 생성 (이미 있을 경우 에러)
- `delete` : 삭제
- `update` : 수정

사용 예제는 다음과 같다.

    POST _bulk

    { "index" : { "_index" : "test", "_type" : "type1", "_id" : "1" } }
    { "field1" : "value1" }
    { "delete" : { "_index" : "test", "_type" : "type1", "_id" : "2" } }
    { "create" : { "_index" : "test", "_type" : "type1", "_id" : "3" } }
    { "field1" : "value3" }
    { "update" : {"_id" : "1", "_type" : "type1", "_index" : "test"} }
    { "doc" : {"field2" : "value2"} }


엔드포인트는 `/_bulk`, `/{index}/_bulk`, `/{index}/{type}/_bulk` 이다. 엔드포인트에 `index`와 `type`이 지정되면 바디에 명시적으로 지정되지 않더라도 지정된 값을 사용한다.

벌크로 입력되는 데이터의 사이즈는 건수로는 1,000 ~ 5,000건 용량으로는 5~15MB가 적당하다. [How Big Is Too Big?](https://www.elastic.co/guide/en/elasticsearch/guide/current/bulk.html#_how_big_is_too_big) 참고