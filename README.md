Project to spin up the infrastructure for a serverless text
message response interface using twilio, apigateway, and aws lambda.

Basically a one button operationalizing of [this tutorial](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python-amazon-lambda)

Setup
=====
1) Create a virtualenv and `pip install -e text_message_interface`
2) Install [terraform](https://learn.hashicorp.com/terraform/getting-started/install.html)
3) Create a [twilio](https://www.twilio.com/try-twilio) account and add a phone number
4) Create a secrets.yaml from the secrets.yaml.template setting account info from twilio
5) Create aws account and setup credentials in ~/.aws
6) Modify `handle_text_message` in lambda_code/lambda_function.py to create your responder
7) From lambda_code directory run `zip -r ../twilioLambda.zip *`

Deploy infrastructure
=====================
Make sure you are using the venv you just created

1) `cd terraform_twilio`
2) `terraform init`
3) `terraform apply`
