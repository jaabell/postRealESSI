from distutils.core import setup
setup(
    name = "postRealESSI",
    packages = ["postRealESSI"],
    version = "0.1",
    description = "A simple post-processor for RealESSI HDF5 outputs",
    author = "Jose Abell",
    author_email = "info@joseabell.com",
    url = "http://www.joseabell.com",
    download_url = "tbd",
    keywords = ["RealESSI", "HDF5", "post-processing", "scipy"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: Beta",
        "Environment :: Other Environment",
        "Intended Audience :: GMSH Users",
        "License :: GPL",
        "Operating System :: OS Independent",
        "Topic :: TBD",
        "Topic :: TBD2",
        ],
    long_description = """\
postRealESSI
-------------------------------------

Parser for gmsh `.msh` files.

"""
)
