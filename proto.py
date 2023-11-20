from linebot.v3.messaging import Configuration, MessagingApi, ApiClient, PushMessageRequest, ApiException

configuration = Configuration(
    access_token = 'access_token'
)

message_dict = {
    'to': 'channel_id',
    'messages': [
        {
            'type': 'text',
            'text': 'テストメッセージ'
        },
    ]
}

with ApiClient(configuration) as api_client:
    api_instance = MessagingApi(api_client)
    push_message_request = PushMessageRequest.from_dict(message_dict)
    try:
        push_message_result = api_instance.push_message_with_http_info(push_message_request, _return_http_data_only=False)
        print(f'The response of MessagingApi->push_message status code => {push_message_result.status_code}')
    except ApiException as e:
        print('Exception when calling MessagingApi->push_message: %s\\n' % e)
