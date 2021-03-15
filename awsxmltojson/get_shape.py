import json
import os

global_shapes = json.load(open(os.path.join(__file__, "global_shapes.json")))
sqs_structures = json.load(open(os.path.join(__file__, "sqs-2012-11-05.normal.json")))

def get_shape(tag):
    return sqs_structures["shapes"].get(tag) or global_shapes.get(tag)