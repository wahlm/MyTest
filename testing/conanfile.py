from conans import ConanFile
import os

class TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "libA/0.1.latest@mawa/test", \
                "libB/0.1.latest@mawa/test", \
                "libD/0.1.latest@mawa/test"
				
    generators = "visual_studio"
