from bottle import response, get, run as run_server  # noqa

from . import serializers
from . import cmd
from .args import FormattedArg


def command_output(command, args=None, shell=None,
                   serializer=serializers.default_serializer):
    if args:
        args = _parse_args(args)
    output = cmd.run_command(command, args=args, shell=shell)
    serialized = serializer(output)
    response.content_type = serialized['content_type']
    return serialized['content']


def _parse_args(args: dict):
    final_args = []
    for arg, value in args.items():
        if isinstance(value, FormattedArg):
            final_args.append(value.arg_str)
        elif isinstance(value, bool) and value:
            final_args.append('--{}'.format(arg))
        else:
            final_args.append('--{} {}'.format(arg, value))
    return final_args
