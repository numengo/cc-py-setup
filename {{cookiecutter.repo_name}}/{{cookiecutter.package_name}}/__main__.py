"""Allow {{ cookiecutter.package_name }} to be executable from a checkout or zip file."""
import runpy


if __name__ == "__main__":
    runpy.run_module("_{{ cookiecutter.package_name }}", run_name="__main__")
