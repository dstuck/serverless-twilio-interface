import urllib


def lambda_handler(event, context):
    print("Received event: " + str(event))
    message_text = event['Body']
    text_response = urllib.parse.unquote_plus(handle_text_message(message_text))
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>{}</Message></Response>'.format(text_response)


def handle_text_message(message_text):
    """
    :param message_text: String representing the message sent
    :return: String response to be texted back to messager
    """
    response = "{} to you too".format(message_text)
    return response
