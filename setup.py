from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='getids',
    version='1.0.0',

    packages=['getids'],
    include_package_data=True,

    url='https://github.com/AmanoTeam/python-getids',
    python_requires='>=3.6',

    author='Amano Team',
    author_email='contact@amanoteam.com',

    license='MIT',

    description='Python port of GetIDs engine that calculates Telegram account age based on known account creation dates.',
    long_description=readme,
    long_description_content_type='text/markdown'
)
