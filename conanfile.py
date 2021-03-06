# Range v3 library
#
#  Copyright Luis Martinez de Bartolome Izquierdo 2016
#
#  Use, modification and distribution is subject to the
#  Boost Software License, Version 1.0. (See accompanying
#  file LICENSE_1_0.txt or copy at
#  http://www.boost.org/LICENSE_1_0.txt)
#
# Project home: https://github.com/ericniebler/range-v3
#

from conans import ConanFile
import platform


class Rangev3Conan(ConanFile):
    name = "range-v3"
    version = "0.2.5"
    license = "Boost Software License - Version 1.0 - August 17th, 2003"
    url = "https://github.com/ericniebler/range-v3"
    exports = "*"

    def package(self):
        self.copy("*.hpp", src="include", dst="include", keep_path=True)
