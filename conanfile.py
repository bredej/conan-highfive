from conans import ConanFile, tools
import os


class HighFiveConan(ConanFile):
    name = "HighFive"
    version = "2.1.1"
    description = "Header-only C++ HDF5 interface"
    topics = ("conan", "HighFive", "HDF5")
    url = "https://github.com/bredej/conan-highfive"
    homepage = "https://github.com/BlueBrain/HighFive"
    author = "Brede Johansen <bredej@gmail.com>"
    license = "BSL-1.0"
    no_copy_source = True
    exports = ["LICENSE"]
    requires = "hdf5/1.10.6"

    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/BlueBrain/HighFive"
        tools.get("{0}/archive/v{1}.zip".format(source_url, self.version), sha256="F08624AFB1F3F28DDEAB60A63A27B592DC6223294EB0324F95D47D2F8A93926E")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
