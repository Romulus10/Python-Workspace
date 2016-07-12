from distutils.core import setup

setup(
    name='Bitcoin Account',
    version='0.0.0.1',
    packages=['', 'test'],
    url='romulus10.github.io',
    license='GNU General Public License',
    author='Romulus10',
    author_email='',
    description='Watches a bitcoin exchange price and determines account value based on that.',
    requires=["requests"]
)
