from conans import ConanFile

class libA(ConanFile):
    name="libA"
    version = "0.1.0"
    requires = (
                ("libC/0.1.latest@mawa/test")
                )
    generators = "cmake"
