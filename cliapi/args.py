from marshmallow import fields


class FormattedArg(str):
    arg_str: str

    def __init__(self, arg_str):
        self.arg_str = arg_str


class Arg(fields.Field):
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
