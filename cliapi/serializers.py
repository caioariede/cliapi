import json as _json


def json(output):
    return {
        'content': _json.dumps(output),
        'content_type': 'application/json',
    }


default_serializer = json
