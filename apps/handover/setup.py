from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='uniflex_app_handover',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/uniflex',
    license='',
    author='Anatolij Zubow, Piotr Gawlowicz',
    author_email='zubow|gawlowicz@tu-berlin.de',
    description='WiFi (802.11) Handover Module',
    long_description='Implementation of the handover app for different wireless technologies: i) IEEE 802.11 WiFi, ii) ...',
    keywords='wireless control',
    install_requires=[]
)
