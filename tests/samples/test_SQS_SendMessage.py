from awsxmltojson import convert_xml_to_dict

sample_input = """
<SendMessageResponse>
    <SendMessageResult>
        <MD5OfMessageBody>fafb00f5732ab283681e124bf8747ed1</MD5OfMessageBody>
        <MD5OfMessageAttributes>3ae8f24a165a8cedc005670c81a27295</MD5OfMessageAttributes>
        <MessageId>5fea7756-0ea4-451a-a703-a558b933e274</MessageId>
    </SendMessageResult>
    <ResponseMetadata>
        <RequestId>27daac76-34dd-47df-bd01-1f6e873584a0</RequestId>
    </ResponseMetadata>
</SendMessageResponse>
""".strip()


def test_sqs_send_message():
    assert convert_xml_to_dict(sample_input) == {
        "SendMessageResponse": {
            "SendMessageResult": {
                "MD5OfMessageAttributes": "3ae8f24a165a8cedc005670c81a27295",
                "MD5OfMessageBody": "fafb00f5732ab283681e124bf8747ed1",
                "MessageId": "5fea7756-0ea4-451a-a703-a558b933e274",
                "RequestId": "27daac76-34dd-47df-bd01-1f6e873584a0",
            }
        }
    }
