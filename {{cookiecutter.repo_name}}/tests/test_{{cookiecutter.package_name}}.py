#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.package_name }}` package."""

{%- if cookiecutter.command_line_interface == 'click' %}
from click.testing import CliRunner
{% endif %}
{%- if cookiecutter.c_extension_support != 'no' %}
from {{ cookiecutter.package_name }} import {{ cookiecutter.c_extension_function }}
{%- endif %}
{%- if cookiecutter.command_line_interface != 'no' %}
from {{ cookiecutter.package_name }}.cli import cli
{%- endif %}
{%- if cookiecutter.test_matrix_configurator == 'yes' and cookiecutter.test_matrix_configurator == 'no' or
       cookiecutter.command_line_interface == 'no' %}
from {{ cookiecutter.package_name }} import main
{%- endif %}

# PROTECTED REGION ID({{cookiecutter.package_name}}.tests.test_{{cookiecutter.package_name}}) ENABLED START

def test_{{cookiecutter.package_name}}():
    # from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name }}
    # assert {{ cookiecutter.package_name }}

{% if cookiecutter.test_matrix_configurator == 'yes' and cookiecutter.test_matrix_configurator == 'no' %}
    assert 'site-packages' in {{ cookiecutter.package_name }}.__file__
{%- endif %}
{%- if cookiecutter.command_line_interface == 'click' %}
    runner = CliRunner()
    result = runner.invoke(cli, [])

    assert result.output == 'Hello World!\n'
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface == 'argparse' %}
    main([])
{%- elif cookiecutter.command_line_interface == 'plain' %}
    assert main([]) == 0
{%- else %}
    pass
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' %}


def test_{{ cookiecutter.c_extension_function }}():
    assert {{ cookiecutter.c_extension_function }}([b'a', b'bc', b'abc']) == b'abc'
{%- endif %}


if __name__ == '__main__':
    # to run test file standalone
    test_{{cookiecutter.package_name}}()

# PROTECTED REGION END
