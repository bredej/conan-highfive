from conans import ConanFile, tools
import os


class HighFiveConan(ConanFile):
    name = "HighFive"
    version = "2.0"
    description = "Header-only C++ HDF5 interface"
    topics = ("conan", "HighFive", "HDF5")
    url = "https://github.com/bredej/conan-highfive"
    homepage = "https://github.com/BlueBrain/HighFive"
    author = "Brede Johansen <bredej@gmail.com>"
    license = "BSL-1.0"
    no_copy_source = True
    exports = ["LICENSE"]
    requires = "hdf5/1.10.5-dm1@ess-dmsc/stable"
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/BlueBrain/HighFive"
        tools.get("{0}/archive/v{1}.zip".format(source_url, self.version), sha256="35D594207CE7971D257AAFE92C0299DD9C1E749E244A39F0A6479818C96087A1")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
