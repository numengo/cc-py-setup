#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import find_packages
from setuptools import setup

import io
import os
import re
import sys
import subprocess
from os.path import basename
from os.path import dirname
from os.path import join
from glob import glob
{% if cookiecutter.c_extension_support not in ['no', 'cffi'] -%}
from os.path import relpath
{% endif -%}
from os.path import splitext

{% if cookiecutter.c_extension_support not in ['no', 'cffi'] -%}
from setuptools import Extension
{% endif -%}
{%- if cookiecutter.c_extension_support != 'no' -%}
{%- if cookiecutter.c_extension_optional == 'yes' %}
from setuptools.command.build_ext import build_ext
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cython' %}

try:
    # Allow installing package without any Cython available. This
    # assumes you are going to include the .c files in your sdist.
    import Cython
except ImportError:
    Cython = None
{%- endif %}
{%- endif %}

def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


{% if cookiecutter.c_extension_support != 'no' -%}
# Enable code coverage for C code: we can't use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
    os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']

{% if cookiecutter.c_extension_optional == 'yes' %}
class optional_build_ext(build_ext):
    """Allow the building of C extensions to fail."""
    def run(self):
        try:
            build_ext.run(self)
        except Exception as e:
            self._unavailable(e)
            self.extensions = []  # avoid copying missing files (it would fail).

    def _unavailable(self, e):
        print('*' * 80)
        print('''WARNING:

    An optional code optimization (C extension) could not be compiled.

    Optimizations for this package will not be available!
        ''')

        print('CAUSE:')
        print('')
        print('    ' + repr(e))
        print('*' * 80)


{% endif -%}
{% endif -%}

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    dir_path = dirname(os.path.realpath(__file__))
    bumpversion = open(join(dir_path, '.bumpversion.cfg')).read()
    return re.search("^current_version\s*=\s*(\S*)\s*\n",
                     bumpversion, re.MULTILINE).group(1)


name = '{{ cookiecutter.distribution_name }}'
package = '{{ cookiecutter.package_name }}'
description = '{{ cookiecutter.short_description }}'
url = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'
author = {{ '{0!r}'.format(cookiecutter.full_name).lstrip('ub') }}
author_email = {{ '{0!r}'.format(cookiecutter.email).lstrip('ub') }}
license = '{{ cookiecutter.license }}'
version = get_version(package)


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(os.path.join(package))
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]
    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup_requires = [
    'matrix',
{%- if cookiecutter.test_runner == 'pytest' %}
    #'pytest-runner',
{%- endif %}
{%- set s_deps = cookiecutter.test_requirements|replace(' ','') %}
{%- set s_deps_str = "'%s'" % s_deps.split(',')|join("',\n    '") %}
{%- if s_deps|trim %}
    {{s_deps_str}}, {% endif %}
]
{%- if cookiecutter.c_extension_support == 'cython' %}
setup_requires +=  ['cython',] if Cython else [],
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cffi' %}
setup_requires +=  ['cffi>=1.0.0',] if if any(i.startswith('build') or i.startswith('bdist') for i in sys.argv) else []
{%- endif %}

install_requires = [
    'future',
{%- if cookiecutter.gettext == 'yes' %}
    'python-gettext',
{%- endif %}
{%- if cookiecutter.command_line_interface == 'click' %}
    'click',
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cffi' %}
    'cffi>=1.0.0',
{%- endif %}
{%- set i_deps = cookiecutter.requirements_install|replace(' ','') %}
{%- set i_deps_str = "'%s'" % i_deps.split(',')|join("',\n    '") %}
{%- if i_deps|trim %}
    {{i_deps_str}}, {% endif %}
]

test_requires = [
{%- if cookiecutter.test_runner == 'pytest' %}
    'pytest',
    'pytest-logger',
{%- endif %}
{%- set t_deps = cookiecutter.test_requirements|replace(' ','') %}
{%- set t_deps_str = "'%s'" % t_deps.split(',')|join("',\n    '") %}
{%- if t_deps|trim %}
    {{t_deps_str}}, {% endif %}
]

extras_requires = {
}

setup(
    name=name,
    version=version,
    license=license,
    description=description,
    long_description='%s\n%s' % (
        re.compile('^.. skip-next.*', re.M | re.S).
           sub('', re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).
           sub('', read('README.rst'))),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    long_description_content_type='text/x-rst',
    author=author,
    author_email=author_email,
    url=url,
    packages=find_packages(exclude='tests'),
    package_data=get_package_data(package),
    include_package_data=True,
    zip_safe=False,
{#- set kws = cookiecutter.keywords|replace(' ','_') #}
{%- set kws = cookiecutter.keywords %}
{%- set kws_str = '["%s"]' % kws.split(',')|join('", "') %}
    keywords={{kws_str}},
{%- set pyenvs = cookiecutter.python_envs|replace(' ','') %}
{%- set pyvers = {'py27': '!=2.7.*', 'py30': '!=3.0.*', 'py31': '!=3.1.*',
                  'py32': '!=3.2.*', 'py33': '!=3.3.*', 'py34': '!=3.4.*',
                  'py35': '!=3.5.*', 'py36': '!=3.6.*',
                  'py37': '!=3.7.*', 'py38': '!=3.8.*',
                  'py39': '!=3.9.*', 'py310': '!=3.10.*',
                  'py311': '!=3.11.*',
                  'pypy': '!=2.7.*', 'pypy3': '!=3.4.*'} %}
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=test_requires,
    extras_require=extras_requires,
{%- if cookiecutter.command_line_interface != 'no' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.command_line_interface_bin_name }}={{ cookiecutter.package_name }}.cli:cli'
{%- set eps = cookiecutter.entry_points|replace(' ','') %}
{%- if eps != '' %}
{%- for e in eps.split(',') %}
{% set cli = e.split('=')[0] %}
            '{{cli}}={{ cookiecutter.package_name }}.commands.cmd_{{cli}}:cli',
{%- endfor %}
{%- endif %}
        ]
    },
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' -%}
{%- if cookiecutter.c_extension_optional == 'yes' %}
    cmdclass={'build_ext': optional_build_ext},
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cffi' %}
    cffi_modules=[i + ':ffi' for i in glob(package+'/_*_build.py')],
{%- else %}
    ext_modules=[
        Extension(
            splitext(relpath(path).replace(os.sep, '.'))[0],
            sources=[path],
            include_dirs=[dirname(path)]
        )
        for root, _, _ in os.walk(package)
        for path in glob(join(root,
{%- if cookiecutter.c_extension_support == 'cython' %} '*.pyx' if Cython else '*.c'
{%- else %} '*.c'{% endif %}))
    ],
{%- endif %}
{%- endif %}
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
{%- set maturity = {
"Planning": "1 - Planning",
"Pre-Alpha": "2 - Pre-Alpha",
"Alpha": "3 - Alpha",
"Beta": "4 - Beta",
"Production/Stable": "5 - Production/Stable",
"Mature": "6 - Mature",
"Inactive": "7 - Inactive" } %}
        'Development Status :: {{ maturity.get(cookiecutter.dev_status) }}',
        'Intended Audience :: Developers',
{%- if cookiecutter.license.startswith('GNU General Public License') %}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
{%- elif cookiecutter.license in ["BSD 2-Clause License", "BSD 3-Clause License"] %}
        'License :: OSI Approved :: BSD License',
{%- elif cookiecutter.license == "MIT license" %}
        'License :: OSI Approved :: MIT License',
{%- elif cookiecutter.license == "ISC license" %}
        'License :: OSI Approved :: ISC License (ISCL)',
{%- elif cookiecutter.license == "Apache Software License 2.0" %}
        'License :: OSI Approved :: Apache Software License',
{%- endif %}
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
{%- if 'pypy' in pyenvs.split(',') %}
        'Programming Language :: Python :: Implementation :: PyPy',
{%- endif %}
        'Topic :: Utilities',
    ],
)
