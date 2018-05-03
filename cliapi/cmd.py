import subprocess
import shlex

from . import decoders
from . import logger
from . import config


logger = logger.get_logger(__name__)


def run_command(command, args=None, shell=None, output_decoder=None):
    if shell is None:
        shell = False

    if output_decoder is None:
        output_decoder = decoders.utf8

    _args = shlex.split(command)
    if args:
        _args.extend(args)

    try:
        output = subprocess.check_output(_args, shell=shell)
    except subprocess.CalledProcessError as exc:
        logger.exception('run_command failed', exc)
        return command_error(exc, exc.returncode)
    except OSError as exc:
        logger.exception('run_command failed', exc)
        return command_error(exc)

    return {'success': True, 'output': output_decoder(output)}


def command_error(exc, returncode=None):
    result = {'success': False, 'returncode': returncode}
    if config.get('expose_errors'):
        result['_error'] = str(exc)
    return result


def command_success(output, output_decoder):
    return {'success': True, 'output': output_decoder(output)}
