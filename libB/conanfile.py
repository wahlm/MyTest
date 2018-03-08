from conans import ConanFile

class libB(ConanFile):
    name="libB"
    version = "0.1.0"
    requires = (
                ("libC/0.1.latest@mawa/test")
                )
    generators = "cmake"
