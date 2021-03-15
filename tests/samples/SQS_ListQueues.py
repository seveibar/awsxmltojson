from awsxmltojson import convert_xml_to_dict

sample_input = """
<ListQueuesResponse>
    <ListQueuesResult>
        <QueueUrl>https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue</QueueUrl>
    </ListQueuesResult>
    <ResponseMetadata>
        <RequestId>725275ae-0b9b-4762-b238-436d7c65a1ac</RequestId>
    </ResponseMetadata>
</ListQueuesResponse>
""".strip()


def test_sqs_list_queues():
    assert convert_xml_to_dict(sample_input) == {
        "ListQueuesResponse": {
            "ListQueuesResult": {
                "queueUrls": [
                    "https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue"
                ]
            }
        }
    }