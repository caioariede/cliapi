from marshmallow import fields as ma_fields

from webargs import fields
from webargs.bottleparser import use_args


class FormattedArg(str):
    def __init__(self, arg_str):
        self.arg_str = arg_str


class Arg(ma_fields.Field):
    def __init__(self, field, fmt=None, coerce=lambda v: v):
        self.field = field
        self.fmt = fmt
        self.coerce = coerce
        super().__init__()

    def _deserialize(self, value, attr, data):
        result = self.coerce(self.field._deserialize(value, attr, data))
        if self.fmt:
            return FormattedArg(self.fmt.format(result))
        return result


__all__ = (
    'fields',
    'use_args',
    'Arg',
)
