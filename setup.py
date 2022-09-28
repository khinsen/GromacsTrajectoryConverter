#!python

package_name = "GromacsTrajectoryConverter"

from distutils.core import setup

setup (name = package_name,
       version = "0.1",
       description = "GROMACS to MMTK trajectory converter",
       long_description=
"""
Reads GROMACS trajectories in XTC format, plus a compatible PDB
file that defines the molecular system, and converts it to an
MMTK trajectory in netCDF format.
""",
       author = "Konrad Hinsen",
       author_email = "konrad.hinsen@cnrs.fr",
       url = "http://github.com/khinsen/GromacsTrajectoryConverter",
       license = "BSD",
       scripts = ['xtc2nc'])
