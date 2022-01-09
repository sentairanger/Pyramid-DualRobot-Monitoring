from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'pyramid_chameleon',
]

dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]

setup (
    name='dual',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = dual:main'
            
            ],
        
    },
)
