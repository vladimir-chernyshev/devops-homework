Домашнее задание к занятию "7.6. Написание собственных провайдеров для Terraform."
===
Найти в исходном коде провайдера AWS
---

 Найдите, где перечислены все доступные *resource* и *data_source*, приложите ссылку на эти строки в коде на гитхабе.

Если я правильно понял задание, нужно найти все строки кода, в которых переменным с такими что-то присваивают:

		git clone https://github.com/hashicorp/terraform-provider-aws.git
		egrep " (resource|data_source) += +" $(find -name "*.go") | uniq

		./internal/service/appsync/function_test.go:  data_source              = aws_appsync_datasource.test.name
		./internal/service/appsync/resolver_test.go:  data_source = aws_appsync_datasource.test.name
		./internal/service/appsync/resolver_test.go:  data_source = aws_appsync_datasource.test2.name
		./internal/service/appsync/resolver_test.go:  data_source = aws_appsync_datasource.test.name
		./internal/service/appsync/resolver_test.go:  data_source              = aws_appsync_datasource.test.name
		./internal/service/appsync/resolver_test.go:  data_source      = aws_appsync_datasource.test.name
		./internal/service/appsync/resolver_test.go:  data_source = aws_appsync_datasource.test.name
		./internal/service/codestarnotifications/notification_rule_test.go:  resource       = aws_codecommit_repository.test.arn
		./internal/service/codestarnotifications/notification_rule_test.go:  resource = aws_codecommit_repository.test.arn
		./internal/service/elasticbeanstalk/environment_test.go:    resource  = "ScheduledAction01"
		./internal/service/location/place_index_data_source_test.go:  data_source = "Here"
		./internal/service/location/place_index_test.go:  data_source = "Here"
		./internal/service/location/route_calculator_data_source_test.go:  data_source     = "Here"
		./internal/service/location/route_calculator_test.go:  data_source     = "Here"


 Для создания очереди сообщений SQS используется ресурс *aws_sqs_queue* у которого есть параметр *name*.
 - С каким другим параметром конфликтует *name*? Приложите строчку кода, в которой это указано.

file: terraform-provider-aws/internal/service/sqs/queue.go

                "name": {
                        Type:          schema.TypeString,
                        Optional:      true,
                        Computed:      true,
                        ForceNew:      true,
                        ConflictsWith: []string{"name_prefix"},
                },
                "name_prefix": {
                        Type:          schema.TypeString,
                        Optional:      true,
                        Computed:      true,
                        ForceNew:      true,
                        ConflictsWith: []string{"name"},

 - Какая максимальная длина имени?
 - Какому регулярному выражению должно подчиняться имя?

Наверное, имеется в виду следующая [цитата](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html):

		The name of a FIFO queue must end with the .fifo suffix. The suffix counts towards the 80-character queue name quota. 