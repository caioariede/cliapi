_CONFIG = {
    'expose_errors': False,
}

_CONFIGURED = False


def get(name):
    return _CONFIG.get(name)


def configure(settings):
    global _CONFIGURED, _CONFIG

    if _CONFIGURED:
        # configure should be called only once
        raise RuntimeError('already configured')

    _CONFIGURED = True
    _CONFIG.update(settings)
