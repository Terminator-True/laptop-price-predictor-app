from setuptools import setup, find_packages

setup(
    name='laptop-price-predictor-app',  # Nombre de tu proyecto
    version='0.1',  # Versión de tu proyecto
    packages=find_packages(),  # Encuentra automáticamente todos los paquetes
    install_requires=[
        'Flask>=2.0.0',  # Especifica la versión mínima de Flask
        'numpy>=1.21.0',  # Especifica la versión mínima de numpy
        # No necesitas incluir 'pickle' ya que es parte de la librería estándar de Python
    ],
    entry_points={
        'console_scripts': [
            # Aquí puedes definir scripts de consola si los necesitas
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Versión mínima de Python
)