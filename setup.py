from setuptools import setup


setup(
    name='isthistruebot',
    version='0.0.1',
    description='A simple bot that responds to tweets with potential fact checks.',
    author='Andrew Briz, Caitlin Ostroff',
    author_email='briz.andrew@gmail.com',
    url='https://github.com/weimer-coders/is-this-true-bot',
    license="MIT",
    packages=("isthistruebot",),
    test_suite="isthistruebot.tests",
    include_package_data=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ),
)
