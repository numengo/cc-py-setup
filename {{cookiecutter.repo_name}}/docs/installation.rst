============
Installation
============

At the command line::

    pip install {{ cookiecutter.distribution_name }}

Settings are managed using
`simple-settings <https://github.com/drgarcia1986/simple-settings>`__
and can be overriden with configuration files (cfg, yaml, json) or with environment variables
prefixed with {{ cookiecutter.package_name|upper }}_.
