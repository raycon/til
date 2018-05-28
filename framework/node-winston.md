# Winston

- [Winston](https://github.com/winstonjs/winston#winston) : 여러개의 `Transport`를 지원하는 비동기 로그 라이브러리
- [Transport](https://github.com/winstonjs/winston/blob/master/docs/transports.md) : 콘솔, 파일, DB, 메일 등 로그를 저장하는 저장소.

## 모듈 설치

    npm install winston --save

## 기본 사용법

모듈이 설치된 상태에서 다음과 같이 작성한다 :

```javascript
var winston = require('winston');

var logger = new(winston.Logger)({
  transports: [
    new(winston.transports.Console)()
  ]
});

logger.info('info log')
```

콘솔에 다음과 같이 출력된다 :

    info: info log

## 로그 레벨

노드는 다음과 같은 로그 레벨을 사용한다. 작은 값일 수록 우선 순위가 높다. :

    { error: 0, warn: 1, info: 2, verbose: 3, debug: 4, silly: 5 }

`transport`에 로그 레벨을 지정해서 출력된 로그를 필터링 할 수 있다. 지정된 레벨보다 우선 순위가 낮은 로그는 출력되지 않는다..

```javascript
var winston = require('winston');

var logger = new(winston.Logger)({
  transports: [
    new(winston.transports.Console)({
      level: 'warn'   // error, warn 로그만 출력된다.
    })
  ]
});
```

## 파일에 저장

콘솔과 `file.log` 파일에 출력하도록 설정 :

```javascript
var winston = require('winston');

var logger = new(winston.Logger)({
  transports: [
    new(winston.transports.Console)({
      level: 'debug'
    }),
    new(winston.transports.File)({
      filename: 'file.log',
      level: 'info'
    })
  ]
});

logger.info('info log');
```

파일에 다음과 같이 출력된다 :

    {"level":"info","message":"info log", "timestamp":"2017-03-03T10:26:39.473Z"}

## 출력 형식 변경

`trnasport` 설정에 `json:false`를 추가하면 로그가 한 줄에 출력되서 보기 편리하다.

## 타임스탬프 변경

`2017-03-03T10:26:39.473Z` 형식으로 출력되는 날짜를 읽기 쉽게 변경할 수 있다.

[moment](https://momentjs.com/docs/) 모듈을 설치한다 :

    npm install moment --save

다음과 같이 사용한다 :

```javascript
var winston = require('winston');
var moment = require('moment');

var stamp = function () {
  return moment().format("YYYY-MM-DD HH:mm:ss.SSS");
}

var logger = new(winston.Logger)({
  transports: [
    new(winston.transports.Console)({
      level: 'debug'
    }),
    new(winston.transports.File)({
      filename: 'file.log',
      level: 'info',
      json: false,      // json으로 출력하지 않음
      timestamp: stamp  // 시간 출력 형식 지정
    })
  ]
});

logger.info('info log');
```

파일에 다음과 같이 출력된다 :

    2017-03-03 19:36:02.943 - info: info log

## 포매터 적용

`formatter`를 사용해서 로그를 출력하는 방식을 변경할 수 있다.

```javascript
var winston = require('winston');

var logger = new (winston.Logger)({
  transports: [
    new (winston.transports.Console)({
      formatter: function(options) {
        // 여러 값을 조합해서 출력을 변경할 수 있다.
        return options.timestamp() +' '+ options.level.toUpperCase() +' '+ (options.message ? options.message : '') +
          (options.meta && Object.keys(options.meta).length ? '\n\t'+ JSON.stringify(options.meta) : '' );
      }
    })
  ]
});

logger.info('info log');
```

파일에 다음과 같이 출력된다 :

    2017-03-03 20:30:46.739 INFO info log

## 여러 파일에 출력

로그 레벨에 따라서 출력되는 파일을 다르게 지정할 수 있다. 동일한 `transport`를 여러개 사용할 경우 `name`으로 각기 다른 이름을 지정해주어야 한다.

```javascript
var logger = new (winston.Logger)({
  transports: [
    new (winston.transports.File)({
      name:'info-file',
      filename: 'info.log',
      level: 'info'
    }),
    new (winston.transports.File)({
      name:'error-file',
      filename: 'error.log',
      level: 'error'
    })
  ]
});
```

## 에러 처리

winston은 uncaughtException이 발생하면 종료된다. 이를 방지하기 위해서는 다음과 같이 설정할 수 있다.

예제 1. 기존 `transport`에서 에러를 표시하고 종료하지 않는다 :

```javascript
var logger = new winston.Logger({
  transports: [
    new winston.transports.Console({
      handleExceptions: true,                 // 에러 로그 출력
      humanReadableUnhandledException: true  // 읽기 편하게 출력
    })
  ],
  exitOnError: false
});
```

예제 2. `exceptionHandlers`에 `transport`를 추가한다 :

```javascript
var logger = new (winston.Logger)({
  transports: [
    new winston.transports.File({ filename: 'all-logs.log' })
  ],
  exceptionHandlers: [
    // exceptions.log 파일에 에러를 출력한다.
    new winston.transports.File({ filename: 'exceptions.log' })
  ]
});
```

## 로그 로테이션

로그 파일의 사이즈를 지정하고 특정 사이즈에 도달할 경우 다음 파일로 넘어가게 설정할 수 있다.

```javascript
var winston = require('winston');
var moment = require('moment');

var stamp = function () {
  return moment().format("YYYY-MM-DD HH:mm:ss.SSS");


var logger = new(winston.Logger)({
  transports: [
    new(winston.transports.Console)({
      level: 'debug'
    }),
    new(winston.transports.File)({
      filename: 'file.log',
      level: 'info',
      json: false,
      timestamp: stamp,
      handleExceptions: true,
      humanReadableUnhandledException: true,
      // 최대 파일 사이즈
      maxsize: 1024 * 1024 * 1, // 1MB
      // 최대 파일 개수 지정
      maxFiles: 5
    })
  ],
  exitOnError: false
});

logger.info('info log');
```

`maxFiles`로 생성되는 로그 파일의 최대 개수를 지정할 수 있다. 생성된 파일의 개수가 지정된 값보다 클 경우 오래된 파일이 삭제된다. 옵션을 지정하지 않을 경우 파일이 계속 추가된다.

`maxsize`로 지정된 크기를 넘어가면 `file1.log`, `file2.log` ... 파일이 순차적으로 생성되며 숫자가 높을수록 최신 로그를 갖는다.

    file.log   ← 오래된 로그
    file1.log
    file2.log
    file3.log
    file4.log  ← 새로운 로그

### tailable 옵션

`tailable:true` 옵션을 설정하면 로그가 로테이트되는 동작이 변경된다. 로그 파일은 `maxFiles` 값을 기준으로 로테이트 되고, 새로운 로그는 항상 `filename`에 저장된다.

    file4.log  ← 오래된 로그
    file3.log
    file2.log
    file1.log
    file.log   ← 새로운 로그

다음 명령어로 로그 감시가 가능하다 :

    tail -f file.log

### 날짜 기준 로테이트

파일의 크기와 개수를 지정해서 로그를 로테이트 할 수 있지만, 현실적으로 사용하기 좋은 방법은 날짜별로 로그를 나누는 것이다.

[winston-daily-rotate-file](https://github.com/winstonjs/winston-daily-rotate-file) transport 모듈을 설치한다.

    npm install winston-daily-rotate-file --save

다음과 같이 사용한다 :

```javascript
var winston = require('winston');
var moment = require('moment');
require('winston-daily-rotate-file');

var stamp = function () {
  return moment().format("YYYY-MM-DD HH:mm:ss.SSS");
}

var logger = new(winston.Logger)({
  transports: [
    new(winston.transports.Console)({
      level: 'debug'
    }),
    new winston.transports.DailyRotateFile({
      level: 'info',
      filename: 'file',
      json: false,
      timestamp: stamp,
      handleExceptions: true,
      humanReadableUnhandledException: true,
      // 최대 파일 개수 지정
      maxFiles: 7,
      // filename + datePattern 으로 로그 파일이 생성된다.
      datePattern: '.yyyy-MM-dd.log'
    }),
  ]
});

logger.info('info log');
```

`file.yyyy-MM-dd.log` 파일이 생성되고, `maxFiles`가 7이므로 일주일이 지난 로그는 삭제된다.

## 사용자 지정 레벨 사용

기본 제공되는 레벨 이외에 임의의 레벨을 사용할 수 있다.

```javascript
var winston = require('winston');

var custom = {
  // 사용자 정의 로그 레벨
  levels: {
    aaa: 0,
    bbb: 1,
    ccc: 2,
    ddd: 3,
    eee: 4
  },
  // 로그 레벨별 색상 정의
  colors: {
    aaa: 'red',
    bbb: 'yellow',
    ccc: 'blue',
    ddd: 'green',
    eee: 'gray'
  }
};

var logger = new(winston.Logger)({
  // 레벨 지정
  levels: custom.levels,
  transports: [
    new(winston.transports.Console)({
      name: 'console-log',
      level: 'eee',     // 콘솔 출력 레벨 지정
      colorize: true    // 콘솔 출력에서 colors를 사용해서 표시하도록 설정
    }),
    new(winston.transports.File)({
      name: 'file-log',
      filename: 'ccc.log',
      level: 'ccc',     // 파일 출력 레벨 지정
    })
  ]
});

// 콘솔에 출력될 색 지정
winston.addColors(custom.colors);

logger.aaa('aaa');
logger.bbb('bbb');
logger.ccc('ccc');
logger.ddd('ddd');
logger.eee('eee');
```

위와 같이 설정한 경우, 콘솔에는 다음과 같이 출력된다 :

    aaa: aaa
    bbb: bbb
    ccc: ccc
    ddd: ddd
    eee: eee

`ccc.log` 파일에는 다음과 같이 출력된다. ddd, eee 로그는 출력되지 않는다. :

    {"level":"aaa","message":"aaa","timestamp":"2017-03-06T05:21:21.833Z"}
    {"level":"bbb","message":"bbb","timestamp":"2017-03-06T05:21:21.836Z"}
    {"level":"ccc","message":"ccc","timestamp":"2017-03-06T05:21:21.836Z"}
