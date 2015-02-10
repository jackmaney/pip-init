from . import Question


class SetupQuestion(Question):

    def __init__(self, name, template_vars, default=None, key_name=None):
        self.default = default
        if key_name:
            self.key_name = key_name
        else:
            self.key_name = name.lower()

        super(SetupQuestion, self).__init__(name, template_vars)

    def _get_message(self):

        if self.default:
            return "{} ({}): ".format(self.name, self.default)
        else:
            return super(SetupQuestion, self)._get_message()

    def process(self, user_input):

        if "setup_kwargs" not in self.template_vars:
            self.template_vars["setup_kwargs"] = {}

        if not user_input and self.default:
            user_input = self.default

        if user_input:
            self.template_vars["setup_kwargs"][
                self.key_name] = "'{}'".format(user_input)


class VariableQuestion(SetupQuestion):

    def __init__(self, name, template_vars, variable_name,
                 default=None, key_name=None):

        self.variable_name = variable_name
        super(VariableQuestion, self).__init__(name, template_vars,
                                               default=default,
                                               key_name=key_name)

    def process(self, user_input):

        if not user_input and self.default:
            user_input = self.default

        if user_input:
            self.template_vars[self.variable_name] = "'{}'".format(user_input)
