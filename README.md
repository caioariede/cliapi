# cliapi
Dead simple way to create Web APIs for command-line tools.


### Example server

```python
from cliapi import get, run_server, command_output, Arg

from webargs import fields
from webargs.bottleparser import use_args


@get('/whoami')
def whoami():
    return command_output('whoami')


@get('/echo')
@use_args({
    'name': Arg(fields.Str(), fmt='Hello {}'),
})
def python(args):
    return command_output('echo', args=args)


run_server(host='0.0.0.0', port=8081, debug=True)
```

### Example responses

```bash
⚡️ curl http://localhost:8081/whoami
{"success": true, "output": "caio\n"}
⚡️ curl http://localhost:8081/echo\?name\=foo
{"success": true, "output": "Hello foo\n"}
```
