# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

from simple_settings import LazySettings
from ngoschema.config.utils import search_app_config_files

settings = LazySettings(
    '{{ cookiecutter.package_name }}.config.settings',
    *search_app_config_files('{{ cookiecutter.package_name }}', '{{ cookiecutter.github_username }}'),
    '{{ cookiecutter.package_name|upper }}_.environ'
)

{%- if cookiecutter.c_extension_support == 'cffi' %}

from .{{ cookiecutter.c_extension_module }} import ffi as _ffi
from .{{ cookiecutter.c_extension_module }} import lib as _lib


def {{ cookiecutter.c_extension_function }}(args):
    args = [_ffi.new('char[]', arg) for arg in args]
    result = _lib.{{ cookiecutter.c_extension_function }}(len(args), _ffi.new('char *[]', args))
    if result == _ffi.NULL:
        return ''
    else:
        return _ffi.string(result)
{%- elif cookiecutter.c_extension_support != 'no' %}

from .{{ cookiecutter.c_extension_module }} import {{ cookiecutter.c_extension_function }}  # noqa
{%- endif %}

# PROTECTED REGION ID({{cookiecutter.package_name}}.init) ENABLED START
from ngoschema import DEFAULT_CONTEXT, APP_CONTEXT
DEFAULT_CONTEXT.add_local_entries(**getattr(settings, 'DEFAULT_CONTEXT', {}))
APP_CONTEXT.add_local_entries(_{{cookiecutter.package_name}}_env=settings.as_dict())

from ngoschema.loaders import register_module
register_module('{{cookiecutter.package_name}}')

from ._{{cookiecutter.package_name}} import *
__all__ = [
    'settings',
]
# PROTECTED REGION END
