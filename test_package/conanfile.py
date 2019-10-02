from conans import ConanFile, CMake, RunEnvironment, tools
import os

class HighFiveTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.source_folder, build_dir="./")
        cmake.build()

    def test(self):
        run_env = RunEnvironment(self)
        os.chdir("bin")
        with tools.environment_append(run_env.vars):
            self.run(".%sexample" % os.sep)
