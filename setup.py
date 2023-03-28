from setuptools import setup, find_packages

setup(
    name="everest-coding",
    version="0.1.0",
    packages=['delivery_cost', 'delivery_time'],
    install_requires=['pytest'],
    entry_points={
        'console_scripts': [
            'delivery_cost=delivery_cost.delivery_cost:main',
            'delivery_time=delivery_time.delivery_time:main'
        ]
    }
)