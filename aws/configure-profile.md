# AWS CLI 설정

> 참고 : [Configuring the AWS Command Line Interface](http://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-chap-getting-started.html)

`aws configure` 명령어로 프로필을 설정해서 다수의 계정을 사용할 수 있다.

`~/.aws/config` : Default region 설정 저장
`~/.aws.credentials` : Access, Secret Key 저장

```text
$ aws configure --profile PROFILE_NAME
AWS Access Key ID [None]: ACCESS_KEY
AWS Secret Access Key [None]: SECRET_ACCESS_KEY
Default region name [None]: REGION
```

사용법 :

```cmd
aws s3 ls --profile PROFILE_NAME
```