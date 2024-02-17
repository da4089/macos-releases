from setuptools import setup

VERSION = '2.0'

setup(
    name = 'macos-releases',
    version = VERSION,
    license='MIT',
    description = 'Get the name and version of macOS releases',
    author = 'XIMet',
    author_email = 'dq.ximet@gmail.com',
    url = 'https://github.com/ximet/macos-releases',
    download_url = f'https://github.com/ximet/macos-releases/archive/v{VERSION}.tar.gz',
    keywords = ['MACOS', 'VERSION', 'DARWIN'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    py_modules = ["macos_releases"],
)
