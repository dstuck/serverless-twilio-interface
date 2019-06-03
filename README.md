Project to spin up the infrastructure for a serverless text
message response interface using twilio, apigateway, and aws lambda.

Setup
=====
1) Create virtualenv and `pip install -e text_message_interface`
2) Install terraform
3) Create twilio account
4) Add credentials and numbers to secrets.yaml
5) Create aws account and setup credentials in ~/.aws
6) From lambda_code directory run `zip -r ../twilioLambda.zip *`

Deploy infrastructure
=====================
Make sure you are using the venv you just created

1) `cd terraform_twilio`
2) `terraform init`
3) `terraform apply`
