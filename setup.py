import setuptools
import numpy.distutils.core
import os

from numpy.distutils.core import Extension

# create extension for calling IGRF
extensions = [Extension(name='pysatMagVect.igrf',
                        sources=[os.path.join('pysatMagVect', 'igrf13.f')]),
              Extension(name='pysatMagVect.fortran_coords',
                        sources=[os.path.join('pysatMagVect', '_coords.f')])]

here = os.path.abspath(os.path.dirname(__file__))
version_filename = os.path.join('pysatMagVect', 'version.txt')
with open(os.path.join(here, version_filename)) as version_file:
    version = version_file.read().strip()

# call setup
numpy.distutils.core.setup(
    name='pysatMagVect',
    version=version,
    packages=['pysatMagVect', 'pysatMagVect.tests'],
    description='Orthogonal geomagnetic vector basis and field-line mapping for multipole magnetic fields.',
    url='http://github.com/pysat/pysatMagVect',

    # Author details
    author='Russell Stoneback',
    author_email='rstoneba@utdallas.edu',
    data_files=[('pysatMagVect', ['pysatMagVect/version.txt'])],
    include_package_data=True,

    # required modules
    install_requires=['numpy', 'scipy'],
    ext_modules=extensions,
)
