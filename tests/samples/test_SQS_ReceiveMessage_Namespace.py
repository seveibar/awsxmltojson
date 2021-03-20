from awsxmltojson import convert_xml_to_dict

sample_input = """<?xml version="1.0"?><ReceiveMessageResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/"><ReceiveMessageResult><Message><MessageId>6ad8eab5-49e2-439f-941b-b1c5b7ebed97</MessageId><ReceiptHandle>AQEBi2yVsGeY6NQvKhycAZwa6y6m5fPn3ZBzXVAJLxdnbCd/usLGpFpnnblgLYupm8Edhxlxoei32xuO37RpHWUqeqXkVV4c2TbGFDEpvHIVEi5n+xFNrqeAuvllReBpv7zs3ta5QYGUfYGL7nMXK7mPdFm91dXDBUQ3YAJUSenFIL0ES3DpjFxBFSvq0ZJbAECDUNLRl2EVJCCDfEYGw97Oy4QBhXIQT4FbFDNkM1jazwDV6STnVgkpz5GqkKc386pfsOMcacM/kVS4SjFgEhuv2oY0+ciKrUIVGgaxmlN+NJuuVB7aHgISwjnJ3DgPFyK7+Gx1E/XhQCYyH5q+4HLBkA==</ReceiptHandle><MD5OfBody>0177857163504bc71bd8f9d47dc092c2</MD5OfBody><Body>{&quot;msg&quot;:&quot;752782b1-efe2-4b40-b0c5-83c5759e9eef, may the force with you!&quot;}</Body></Message></ReceiveMessageResult><ResponseMetadata><RequestId>e079e802-8722-58e5-9832-b0cddcb18722</RequestId></ResponseMetadata></ReceiveMessageResponse>"""

def test_sqs_receive_message_namespace():
    assert convert_xml_to_dict(sample_input) == {
        "ReceiveMessageResponse": {
            "ReceiveMessageResult": {
                "messages": [
                    {
                        "MessageId": "6ad8eab5-49e2-439f-941b-b1c5b7ebed97",
                        "ReceiptHandle": "AQEBi2yVsGeY6NQvKhycAZwa6y6m5fPn3ZBzXVAJLxdnbCd/usLGpFpnnblgLYupm8Edhxlxoei32xuO37RpHWUqeqXkVV4c2TbGFDEpvHIVEi5n+xFNrqeAuvllReBpv7zs3ta5QYGUfYGL7nMXK7mPdFm91dXDBUQ3YAJUSenFIL0ES3DpjFxBFSvq0ZJbAECDUNLRl2EVJCCDfEYGw97Oy4QBhXIQT4FbFDNkM1jazwDV6STnVgkpz5GqkKc386pfsOMcacM/kVS4SjFgEhuv2oY0+ciKrUIVGgaxmlN+NJuuVB7aHgISwjnJ3DgPFyK7+Gx1E/XhQCYyH5q+4HLBkA==",
                        "MD5OfBody": "0177857163504bc71bd8f9d47dc092c2",
                        "Body": '{"msg":"752782b1-efe2-4b40-b0c5-83c5759e9eef, may the force with you!"}',
                    }
                ]
            },
            "ResponseMetadata": {"RequestId": "e079e802-8722-58e5-9832-b0cddcb18722"},
        }
    }
