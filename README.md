# AWS XML to JSON

This module converts AWS API XML responses to JSON, it
matches the output of AWS APIs where `Accept: application/json` is provided
as a header.

<!-- GENERATED_SAMPLE_DOCS_START -->
<!-- GENERATED_SAMPLE_DOCS_STOP -->

## Want to add another AWS API?

1. Download the XML to JSON mapping helper file from the [aws javascript sdk](https://github.com/aws/aws-sdk-js/tree/master/apis)
2. Add it so it's loaded in `get_shape.py`
3. Write a couple sample tests use example responses from the AWS documentation to make sure
   it's working