from awsxmltojson import convert_xml_to_dict

sample_input = """
<ErrorResponse>
    <Error>
        <Type>Sender</Type>
        <Code>AccessDenied</Code>
        <Message>Access to the resource https://sqs.us-east-1.amazonaws.com/ is denied.</Message>
        <Detail/>
    </Error>
    <RequestId>2d121ac6-aeee-515c-8d04-420e02b34285</RequestId>
</ErrorResponse>
""".strip()


def test_sqs_list_queues():
    assert convert_xml_to_dict(sample_input) == {
        "ErrorResponse": {
            "Error": {
                "Code": "AccessDenied",
                "Message": "Access to the resource https://sqs.us-east-1.amazonaws.com/ is denied.",
                "Type": "Sender",
            }
        }
    }
