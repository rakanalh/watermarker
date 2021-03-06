from setuptools import setup


setup(
    name='watermarker',
    version='1.1',
    packages=['watermarker'],
    install_requires=[
        'pillow',
    ],
    author='Pavel Zhukov',
    author_email='gelios@gmail.com',
    description='Library for add text watermarks to images using PIL, '
                'support sorl-thumbnail integration',
    long_description=open('README.md').read(),
    license='GPL',
    keywords='watermark, library',
    url='http://bitbucket.org/zeus/watermarker'
)
