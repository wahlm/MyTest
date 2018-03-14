from conans import ConanFile

class libC(ConanFile):
    name="libC"
    version = "0.1.0-special.1"
#    requires = "libD/0.1.latest@mawa/test"
    generators = "cmake"

    def configure(self):
        self.requires("libD/0.1.15@mawa/test")

#    def requirements(self):
#        self.requires("libD/0.1.latest@mawa/test")
