import io
import os
import re
from setuptools import find_packages, setup

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

setup(
    name="audioaugmentor",
    version="0.1.0",
    url="https://github.com/lucenfort/audioaugmentor",  # URL do repositório do projeto
    license='MIT',

    author="Luciano Arruda",
    author_email="lucianoarruda@aluno.uema.br",

    description="Pacote de aumento de dados para processamento de áudio.",
    long_description=read("README.md"),  # Alterado para .md, pois o conteúdo do README geralmente está em markdown
    long_description_content_type='text/markdown',  # Especifica que o README está em Markdown

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        "numpy>=1.18.0",
        "librosa>=0.8.0",
        "scipy>=1.4.0",
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',  # O status de desenvolvimento foi atualizado
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
    ],
    python_requires='>=3.6',
)
