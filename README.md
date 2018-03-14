aws-lambda
==========

A generic role for managing AWS Lambda functions

Requirements
------------

boto3

Role Variables
--------------

### Inputs

* `aws_lambda_function_name` - Name of the Lambda function. Mandatory
* `aws_lambda_handler` - Name of the Lambda handler. Mandatory
* `aws_lambda_runtime` - Runtime used by the lambda. Mandatory
* `aws_lambda_timeout` - Timeout in seconds. Defaults to 30
* `aws_lambda_memory` - Maximum memory allowed. Defaults to 128MB
* `aws_lambda_iam_role` - Name of the IAM role used by the Lambda. Mandatory
* `aws_lambda_iam_role_policy` - JSON policy document for the IAM role.
  Required if the role doesn't yet exist.
* `aws_lambda_iam_role_trust_policy` - JSON trust policy document for the IAM role.
  Required if the role doesn't yet exist.
* `aws_lambda_zip_file` - Zip file containing the Lambda function.
  Mutually exclusive with `aws_lambda_s3_bucket` and `aws_lambda_s3_key`
* `aws_lambda_s3_bucket` - S3 bucket containing the lambda. Mutually exclusive with `aws_lambda_zip_file`
* `aws_lambda_s3_key` - Key of the S3 object containing the lambda. Mutually exclusive with `aws_lambda_zip_file`
* `aws_lambda_environment` - a dictionary of environment variables
* `aws_lambda_vpc_security_group_ids` - List of security group IDs the Lambda belongs to, if the Lambda
  should be in a VPC.
* `aws_lambda_vpc_security_group_filters` - A dictionary of filters that can be used to search for the Lambda
  security groups. An alternative to specifying security group IDs.
* `aws_lambda_vpc_subnet_ids` - List of subnet IDs the Lambda belongs to, if the Lambda should be in a VPC.
* `aws_lambda_vpc_subnet_filters` - A dictionary of filters that can be used to search for the Lambda
  subnets. An alternative to specifying subnet IDs.
* `aws_lambda_schedule_rule_name` - Name of scheduled rule to create/update (if needed). Required if
  `aws_lambda_schedule_rule_expression` is set.
* `aws_lambda_schedule_rule_description` - Optional description of scheduled rule
* `aws_lambda_schedule_rule_expression` - Scheduled expression for scheduled rule. Required if
  `aws_lambda_schedule_rule_name` is set.
* `aws_lambda_region` - AWS region containing the Lambda. Needs to be set if not set elsewhere (e.g. environment
  variable, `.aws/config` etc.)
* `aws_lambda_profile` - boto profile used to connect to AWS. An alternative to environment variables.
* `aws_lambda_access_key` - AWS access key. An alternative to environment variables or profile.
* `aws_lambda_secret_key` - AWS secret key. An alternative to environment variables or profile.
* `aws_lambda_security_token` - AWS security token. An alternative to environment variables or profile.

### Output

* `aws_lambda_result` - result variable from the call to the `lambda` module.

Dependencies
------------


Example Playbook
----------------

    - hosts: scheduled-lambda:api-gateway-lambda
      vars:
        aws_lambda_function_name: my_function
        aws_lambda_handler: my_function.handler
        aws_lambda_runtime: python3.6
        aws_lambda_iam_role: my-function-iam-role
        aws_lambda_iam_role_policy: "{{ lookup('template', 'policy.json', convert_data=False) }}"
        aws_lambda_iam_role_trust_policy: "{{ lookup('template', 'trust-policy.json', convert_data=False) }}"
        aws_lambda_vpc_security_group_filters:
          tag:Environment: test
          tag:Application: my_function
        aws_lambda_vpc_subnet_filters:
          tag:Environment: test
          tag:Application: my_function
        aws_lambda_environment:
          ENVIRONMENT: test
          HELLO: world
        aws_lambda_s3_bucket: my_lambda_bucket
        aws_lambda_s3_key: path/to/my_function.zip
        aws_lambda_schedule_rule_name: my-function-schedule-rule
        aws_lambda_schedule_rule_description: Run my function every 5 minutes
        aws_lambda_schedule_rule_expression: 'rate(5 minutes)'

      roles:
         - aws-lambda

License
-------

BSD

Author Information
------------------

Will Thames, XVT Solutions (will.thames@xvt.com.au)
