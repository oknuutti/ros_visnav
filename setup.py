## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

try:
    from catkin_pkg.python_setup import generate_distutils_setup
    from distutils.core import setup

    # fetch values from package.xml
    setup_args = generate_distutils_setup(
        packages=['pyvio'],
        package_dir={'': 'src'},
        install_requires=['visnav'],
    )
except ModuleNotFoundError:
    from setuptools import setup
    setup_args = dict(
        name='pyvio',
        version='1.0',
        packages=['pyvio'],
        package_dir={'': 'src'},
        install_requires=['visnav'],
    )

setup(**setup_args)
