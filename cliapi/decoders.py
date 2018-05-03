import json as _json
import sys


def utf8(output: bytes):
    return output.decode('utf-8')


def json(output: bytes):
    if sys.version_info[:2] < (3, 6):
        return _json.loads(output.decode('utf-8'))
    return _json.loads(output)
