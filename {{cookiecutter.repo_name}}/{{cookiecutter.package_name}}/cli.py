"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?
  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:
  - When you run `python -m{{cookiecutter.package_name}}` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.
Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration

{% if cookiecutter.command_line_interface == 'click' %}
The command line interface loads subcommands dynamically from a plugin folder and other things.

All the commands are implemented as plugins in the `{{cookiecutter.package_name}}.commands` package.
If a python module is placed named "cmd_foo" it will show up as "foo" command and the `cli` object
within it will be loaded as nested Click command.
{% endif -%}
"""
{%- if cookiecutter.command_line_interface == 'click' %}
import os, sys
import click
from ngoschema.cli import ComplexCLI, base_cli, run_cli
{%- elif cookiecutter.command_line_interface == 'argparse' %}
import argparse
{%- else %}
import sys
from ngoschema import APP_CONTEXT, DEFAULT_CONTEXT
from {{cookiecutter.packagename}}.config import settings

{%- endif %}

# PROTECTED REGION ID({{cookiecutter.package_name}}.cli) ENABLED START
{%- if cookiecutter.command_line_interface == 'click' %}

CONTEXT_SETTINGS = dict(auto_envvar_prefix="{{cookiecutter.package_name|upper}}", show_default=True)
CMD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))

# in init, settings are available in app context whereas it is in default context in cli
DEFAULT_CONTEXT.add_local_entries(settings=settings, **getattr(settings, 'DEFAULT_CONTEXT', {}))
APP_CONTEXT.add_local_entries(_{{cookiecutter.package_name|lower}}_env=settings)


cli = click.command(
    cls=ComplexCLI,
    name='{{cookiecutter.command_line_interface_bin_name}}',
    module_name='{{cookiecutter.package_name}}',
    cmd_folder=CMD_FOLDER,
    help='{{cookiecutter.short_description}}',
    no_args_is_help=True,
    context_settings=CONTEXT_SETTINGS)(base_cli)

if __name__ == "__main__":
    # used for debug - allows to run the file and pass arguments to command line
    run_cli(cli, sys.argv[1:])
{%- elif cookiecutter.command_line_interface == 'argparse' %}

parser = argparse.ArgumentParser(description='{{cookiecutter.short_description}}')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(args=None):
    args = parser.parse_args(args=args)
    print("Hello World!")
{%- else %}


def main(argv=sys.argv):
    """
    {{cookiecutter.short_description}}

    :param argv: List of arguments
    :return: a return code
    """
    print("Hello World!")
    return 0
{%- endif %}

# PROTECTED REGION END
