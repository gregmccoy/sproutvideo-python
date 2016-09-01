from distutils.core import setup

setup(
    name="sproutvideo-python",
    version="0.1",
    license="GPL",
    description="a python wrapper from sproutvideo API",
    author="Greg McCoy",
    author_email="gmccoy4242@gmail.com",
    url="https://github.com/gregmccoy/sproutvideo-python",
    requires=[
        'requests',
    ],
    packages = ['sprout'],
)
