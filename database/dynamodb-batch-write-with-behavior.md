# Batch Write with Behavior

DynamoDB 에 데이터를 저장할 경우 `SaveBehavior`를 지정할 수 있고, 다음과 같은 방식으로 작동한다.

```plain
SaveBehavior                On unmodeled attribute  On null-value attribute     On set attribute
UPDATE                      keep                    remove                      override
UPDATE_SKIP_NULL_ATTRIBUTES keep                    keep                        override
CLOBBER                     remove                  remove                      override
APPEND_SET                  keep                    keep                        append
```

[BatchWrite](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/datamodeling/DynamoDBMapper.html#batchWrite-java.lang.Iterable-java.lang.Iterable-com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapperConfig-)의 경우 다음과 같은 시그니쳐를 갖는다.

```java
public List<DynamoDBMapper.FailedBatch> batchWrite(Iterable<? extends Object> objectsToWrite,
                                                   Iterable<? extends Object> objectsToDelete,
                                                   DynamoDBMapperConfig config)
```

`batchWrite` 메소드는 `DynamoDBMapperConfig`에 `SaveBehavior`를 지정해도 무시되고, `CLOBBER` 모드로 작동하도록 구현되어 있다. 따라서 업데이트 되는 항목에 null이 포함될 경우 해당 항목은 삭제된다.

기존 항목을 유지한 채 추가되는 컬럼을 업데이트 하고 싶은 경우 `DynamoDBMapperConfig`에 `SaveBehavior`를 지정하고, 이를 사용하는 `DynamoDBMapper`를 생성해서 `save` 메소드를 사용해야 한다.

```java
public void write(List<?> items) {
    DynamoDBMapperConfig config = DynamoDBMapperConfig.builder()
                                        .withSaveBehavior(SaveBehavior.UPDATE_SKIP_NULL_ATTRIBUTES)
                                        .build();
    DynamoDBMapper mapper = new DynamoDBMapper(dynamoDB, config);
    items.forEach(mapper::save);
}
```