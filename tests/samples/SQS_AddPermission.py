from awsxmltojson import convert_xml_to_dict

sample_input = """
<AddPermissionResponse>
    <ResponseMetadata>
        <RequestId>9a285199-c8d6-47c2-bdb2-314cb47d599d</RequestId>
    </ResponseMetadata>
</AddPermissionResponse>
""".strip()


def test_sqs_add_permission():
    assert convert_xml_to_dict(sample_input) == {
        "AddPermissionResponse": {"ResponseMetadata": {}}
    }