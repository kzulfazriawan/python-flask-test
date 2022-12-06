from abc import ABCMeta

from flask import request, jsonify, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email


class RequestValidationException(Exception):
    def __init__(self, exception, message="Invalid requests parse!"):
        self.message = message
        self.exception = exception
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.exception}'


class Requests:
    class parse:
        form = None
        file = None
        args = None

    def __init__(self, class_name):
        """
        Class for parsing and validating requests

        :param class_name:
        """
        self.class_name = class_name.lower()

    def parsing(self):
        try:
            if bool(request.form):
                self.parse.form = request.form.to_dict(flat=False)

            if bool(request.files):
                self.parse.file = request.files.to_dict(flat=False)

            if bool(request.args):
                self.parse.args = request.args

        except AttributeError:
            pass

    def validation(self, **kwargs):
        """
        ## validation

        :param csrf_enable:
        :param kwargs:
        :return:
        """
        try:
            dict_validation = {}

            for k, v in kwargs.items():
                validate = v.split(',')
                tmp_validators = []

                if 'required' in validate:
                    tmp_validators.append(DataRequired(f'field {k} is required'))
                if 'email' in validate:
                    tmp_validators.append(Email(f'field {k} is required and valid email type'))

                # defining field-type
                if 'numeric' in validate:
                    dict_validation[k] = IntegerField(k, validators=tmp_validators)
                else:
                    dict_validation[k] = StringField(k, validators=tmp_validators)

        except KeyError as err:
            raise RequestValidationException.with_traceback(err.__traceback__)

        else:
            forms = type(f'{self.class_name}_forms_validation', (FlaskForm,), dict_validation)
            forms = forms(csrf_enabled=False)

            if not forms.validate():
                return {'errors': forms.errors, 'code': 422}
            else:
                self.parsing()
                return {'code': 200}


class Response:
    def json(self, data, status_code=200):
        """
        Converting the response result as json

        :param data:
        :param status_code:
        :return:
        """
        return jsonify(data), status_code

    def redirect(self, target):
        """
        Converting to redirect response

        :param target:
        :return:
        """
        return redirect(target, 301)


class Resource(metaclass=ABCMeta):
    headers, body = [{}, {}]

    def __init__(self):
        super(Resource, self).__init__()

        self.request = Requests(self.__class__.__name__)
        self.response = Response()
