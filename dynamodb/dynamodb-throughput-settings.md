# DynamoDB Throughput Settings

DynamoDB는 읽기, 쓰기 용량을 정해놓고, 사용한 시간 만큼 요금을 지불한다.

## Capacity Units

`Unit`은 1초 기준으로 1번의 읽기, 쓰기를 의미한다. 하나의 Unit은 데이터를 읽을 때 최대 4KB의 사이즈를 갖는다. 데이터를 입력할 때는 최대 1KB의 사이즈를 갖는다.

8KB 데이터를 읽을 경우: 2 units
4KB 데이터를 쓰는 경우: 4 units

## AutoScailing



## Limits

읽기, 쓰기 용량의 최소값은 1이다. 최대값은 지역별로 다르다.

- US East
  - 테이블 당: 읽기 40,000, 쓰기 40,000
  - 계정 당: 읽기 80,000, 쓰기 80,000
- 다른 지역
  - 테이블 당: 읽기 10,000, 쓰기 20,000
  - 계정 당: 읽기 20,000, 쓰기 20,000

`DescribeLimits` 오퍼레이션으로 이 값을 확인할 수 있다.

    aws dynamodb describe-limits --region ap-northeast-2
    {
        "TableMaxWriteCapacityUnits": 40000,
        "TableMaxReadCapacityUnits": 40000,
        "AccountMaxReadCapacityUnits": 80000,
        "AccountMaxWriteCapacityUnits": 80000
    }

## Change Provisioned Throughput

AWS 콘솔이나 `UpdateTable` 오퍼레이션을 통해서 읽기 용량과 쓰기 용량을 필요에 따라 증가시킬 수 있다.

- 용량 늘이기: 필요한 만큼 사용 가능
- 용량 줄이기: 하루(GMT 기준)에 최대 27번 가능
  - 첫 한시간 동안 4번 감소
  - 다음 1시간 마다 1번씩 감소

## 참고

- <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html>
- <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#default-limits-capacity-units-provisioned-throughput>
- <https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-dynamodb.html>