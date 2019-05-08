# GuardDury-Notice
- AWS GuardDutyを有効化して、結果があればGoogle Hangout Chatsへ通知する
- SAMを使ってdeployします。
  
## SAMの初期化からDeployまでの方法
```
sam init -r python3.7 -n GuardDury-Notice
cd GuardDury-Notice

vi template.yml

sam validate 

sam build 

sam local generate-event cloudwatch scheduled-event > event.json
　(*) GuardDutyのeventがないから、これをつかっておく

sam local invoke --parameter-overrides 'ParameterKey=URL,ParameterValue=/v1/spaces/xxxxx/messages?key=xxxxxxxx'

sam package --s3-bucket s3bucketname --output-template-file deploy.yml --profile hoge

aws cloudformation deploy --template-file deploy.yml --stack-name GuardDuty-SendNotice --parameter-overrides URL='/v1/spaces/xxxxx/messages?key=xxxxxxxx' --profile hoge --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```
## その他
- GuardDutyは有効化しますが、VPC Flowlogなど、必要であれば別途設定してください。