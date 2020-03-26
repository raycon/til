# Spring Batch Meta-Data

> <https://docs.spring.io/spring-batch/3.0.x/reference/html/metaDataSchema.html> 내용 요약 정리

## Overview

![meta-data-erd](https://docs.spring.io/spring-batch/3.0.x/reference/html/images/meta-data-erd.png)

Domain object - table 매핑

    JobInstance : BATCH_JOB_INSTANCE
    JobExecution : BATCH_JOB_EXECUTION
    JobParameters : BATCH_JOB_EXECUTION_PARAMS
    StepExecution : BATCH_STEP_EXECUTION
    ExecutionContext : BATCH_JOB_EXECUTION_CONTEXT, BATCH_STEP_EXECUTION_CONTEXT

`JobRepository`가 위의 Object 들을 각각의 테이블에 저장/조회하는 역할을 한다.

이 테이블을 생성하는 스크립트는 `org.springframework.batch.core`에 `schema-[DB].sql`로 정의되어 있다.

스프링 배치는 데이터베이스를 업데이트 할 때 낙관적 락 전략을 사용한다. 데이터가 업데이트 될 때 Version 컬럼이 1 증가한다. 값을 변경하려고 할 때 Version 값이 전과 다르면 `OptimisticLockingFailureException`을 발생한다. 이는 서로 다른 장치에서 같은 DB를 사용해서 Job을 수행할 수 있으므로 필요하다.

`BATCH_JOB_INSTANCE`, `BATCH_JOB_EXECUTION`, `BATCH_STEP_EXECUTION`의 경우 `ID`값을 가지고 있고 이는 시퀀스로 관리된다. 시퀀스를 지원하지 않는 DB를 위한 대안도 제공한다.

## BATCH_JOB_INSTANCE

```sql
CREATE TABLE BATCH_JOB_INSTANCE  (
  JOB_INSTANCE_ID BIGINT  PRIMARY KEY ,
  VERSION BIGINT,
  JOB_NAME VARCHAR(100) NOT NULL ,
  JOB_KEY VARCHAR(2500)
);
```

- `JOB_INSTANCE_ID`: JobInstance.getId 로 반환되는 고유한 값
- `JOB_KEY`: 직렬화된 JobParameters 값. 특정 JobInstance를 다른 instance와 구분하는데 사용되므로 같은 JOB_NAME을 갖는 instance들은 JOB_KEY가 달라야한다.


## BATCH_JOB_EXECUTION_PARAMS

```sql
CREATE TABLE BATCH_JOB_EXECUTION_PARAMS  (
  JOB_EXECUTION_ID BIGINT NOT NULL ,
  TYPE_CD VARCHAR(6) NOT NULL ,
  KEY_NAME VARCHAR(100) NOT NULL ,
  STRING_VAL VARCHAR(250) ,
  DATE_VAL DATETIME DEFAULT NULL ,
  LONG_VAL BIGINT ,
  DOUBLE_VAL DOUBLE PRECISION ,
  IDENTIFYING CHAR(1) NOT NULL ,
  constraint JOB_EXEC_PARAMS_FK foreign key (JOB_EXECUTION_ID)
  references BATCH_JOB_EXECUTION(JOB_EXECUTION_ID)
);
```

`BATCH_JOB_INSTANCE`와 1대다로 매핑된다. 타입별로 테이블을 나누지 않고 컬럼을 사용한다.

- `TYPE_CD`: 어떤 값이 저장되어있는지 나타낸다. (string, date, long, double)
- `IDENTIFYING`: job을 식별하는데 사용된 파라미터는 1로 설정된다.

## BATCH_JOB_EXECUTION

Job이 실행될 때 마다 JobExecution이 생성되고 새로운 레코드가 생성된다.

```sql
CREATE TABLE BATCH_JOB_EXECUTION  (
  JOB_EXECUTION_ID BIGINT  PRIMARY KEY ,
  VERSION BIGINT,
  JOB_INSTANCE_ID BIGINT NOT NULL,
  CREATE_TIME TIMESTAMP NOT NULL,
  START_TIME TIMESTAMP DEFAULT NULL,
  END_TIME TIMESTAMP DEFAULT NULL,
  STATUS VARCHAR(10),
  EXIT_CODE VARCHAR(20),
  EXIT_MESSAGE VARCHAR(2500),
  LAST_UPDATED TIMESTAMP,
  JOB_CONFIGURATION_LOCATION VARCHAR(2500) NULL,
  constraint JOB_INSTANCE_EXECUTION_FK foreign key (JOB_INSTANCE_ID)
  references BATCH_JOB_INSTANCE(JOB_INSTANCE_ID)
) ;
```

- `END_TIME`: 성공/실패 여부에 상관 없이 종료된 시간을 나타낸다. job이 수행중이 아닌데 비어있을 경우 에러가 발생했고 프레임워크가 저장하지 못한 상황을 의미한다.
- `STATUS`: 상태 코드. `BatchStatus` enumeration 에 정의된 값이 사용된다.
  - [BatchStatus vs ExitStatus](https://docs.spring.io/spring-batch/trunk/reference/htmlsingle/#batchStatusVsExitStatus): BatchStatus는 기록용, ExitStatus는 스텝의 조건 분기에 사용된다.
- EXIT_CODE: 커맨드라인 잡일 경우 숫자로 변환된다.

## BATCH_STEP_EXECUTION

```sql
CREATE TABLE BATCH_STEP_EXECUTION  (
  STEP_EXECUTION_ID BIGINT  PRIMARY KEY ,
  VERSION BIGINT NOT NULL,
  STEP_NAME VARCHAR(100) NOT NULL,
  JOB_EXECUTION_ID BIGINT NOT NULL,
  START_TIME TIMESTAMP NOT NULL ,
  END_TIME TIMESTAMP DEFAULT NULL,
  STATUS VARCHAR(10),
  COMMIT_COUNT BIGINT ,
  READ_COUNT BIGINT ,
  FILTER_COUNT BIGINT ,
  WRITE_COUNT BIGINT ,
  READ_SKIP_COUNT BIGINT ,
  WRITE_SKIP_COUNT BIGINT ,
  PROCESS_SKIP_COUNT BIGINT ,
  ROLLBACK_COUNT BIGINT ,
  EXIT_CODE VARCHAR(20) ,
  EXIT_MESSAGE VARCHAR(2500) ,
  LAST_UPDATED TIMESTAMP,
  constraint JOB_EXECUTION_STEP_FK foreign key (JOB_EXECUTION_ID)
  references BATCH_JOB_EXECUTION(JOB_EXECUTION_ID)
) ;
```

- TODO: 각 Count는 언제 업데이트 되는가?

## BATCH_JOB_EXECUTION_CONTEXT

`JobExecution`당 하나의 `ExecutionContext`가 생성된다. Context는 Job-level 의 데이터를 저장하는데, 이는 주로 상태를 나타내는 값 들이다. Job 이 실패한 시점부터 다시 시작하기 위해 필요한 값들이 저장된다.

```sql
CREATE TABLE BATCH_JOB_EXECUTION_CONTEXT  (
  JOB_EXECUTION_ID BIGINT PRIMARY KEY,
  SHORT_CONTEXT VARCHAR(2500) NOT NULL,
  SERIALIZED_CONTEXT CLOB,
  constraint JOB_EXEC_CTX_FK foreign key (JOB_EXECUTION_ID)
  references BATCH_JOB_EXECUTION(JOB_EXECUTION_ID)
) ;
```

- `SHORT_CONTEXT`: SERIALIZED_CONTEXT의 문자열 버전
- `SERIALIZED_CONTEXT`: 직렬화 된 context

## BATCH_STEP_EXECUTION_CONTEXT

`StepExecution`당 하나의 `ExecutionContext`가 생성된다. Step이 실패한 시점부터 다시 시작하기 위해 필요한 값들이 저장된다.

```sql
CREATE TABLE BATCH_STEP_EXECUTION_CONTEXT  (
  STEP_EXECUTION_ID BIGINT PRIMARY KEY,
  SHORT_CONTEXT VARCHAR(2500) NOT NULL,
  SERIALIZED_CONTEXT CLOB,
  constraint STEP_EXEC_CTX_FK foreign key (STEP_EXECUTION_ID)
  references BATCH_STEP_EXECUTION(STEP_EXECUTION_ID)
) ;
```

## Archiving

- 프레임워크는 테이블에 있는 정보를 특정 JobInstance가 실행된 적이 있는지 판단하는 용도로 사용한다. 만약 실행된 적이 있고 job을 재시작 할 수 없다면 예외를 던진다.
- `JobInstance`에 저장된 값이 성공적으로 종료되지 않고 삭제된다면, 프레임워크는 Job을 재시작하지 않고 새로 생성한다.
- Job이 재시작되면서 ExecutionContext에 있는 값을 복원해서 사용한다. 성공적으로 종료되지 않은 Job의 값을 지운다면 적절한 위치에서 재시작되지 않는다.

## International and Multi-byte Characters

- 멀티바이트 언어를 사용한다면 스키마의 VARCHAR 값을 두배로 바꾸는게 간단하다.
- `JobRepository`의 `max-varchar-length`를 VARCHAR 값의 1/2로 설정 할 수도 있다.
- VARCHAR를 NVARCHAR로 대신 할 수도 있다.

## 인덱싱

사용자별로 인덱스를 지정하고 싶은 컬럼이 다르기 때문에 프레임워크는 인덱스 정의를 하지 않는다. 다음 구문은 배치 코어의 DAO 에서 사용하는 WHERE 절이다. 여기에 인덱스를 걸어서 성능을 향상시킬 수 있다.

| Table | Where | Frequency |
|--|--|--|
| BATCH_JOB_INSTANCE | JOB_NAME = ? and JOB_KEY = ? | Every time a job is launched |
| BATCH_JOB_EXECUTION | JOB_INSTANCE_ID = ? | Every time a job is restarted |
| BATCH_EXECUTION_CONTEXT | EXECUTION_ID = ? and KEY_NAME = ? | On commit interval, a.k.a. chunk |
| BATCH_STEP_EXECUTION | VERSION = ? | On commit interval, a.k.a. chunk (and at start and end of step) |
| BATCH_STEP_EXECUTION | STEP_NAME = ? and JOB_EXECUTION_ID = ? | Before each step execution |

