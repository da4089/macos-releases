# Copyright (c) 2020 XIMet
# Copyright (C) 2023-2024 David Arnold
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__all__ = ["OS",
           "lookup",
           "get_host_os",
           "getMacOSRelease"]

import datetime
import email.utils
import os
from typing import Optional, Sequence


class OS:
    """ """

    def __init__(self, product: str, name: str, version: str, build: str, darwin: str = None, kernel: str = None, date: str = None):
        """(Internal) Constructor."""
        self.product = product
        self.name = name
        self.version = version
        self.build = build
        self.darwin = darwin
        self.kernel = kernel
        self.date = date

    @property
    def full_name(self) -> str:
        """Return the full product name including version string."""
        return f"{self.product} {self.name} {self.version}"

    @property
    def datetime(self) -> Optional[datetime.datetime]:
        """Return the kernel build date as a datetime, or None."""
        try:
            return email.utils.parsedate_to_datetime(self.date)
        except:
            return None


# Sources
#  Wikipedia
#  betawiki.net

_BUILDS = [
    # Pre-releases
    OS("Mac OS X", "Beaker",  "10.0 DP1", "Beaker1N5", "1.0", "xnu-24.6.obj~2", "Fri Apr 30 23:26:14 PDT 1999"), # v521
    OS("Mac OS X", "Beaker",  "10.0 DP1", "Beaker1P2", "1.0", "xnu-25.1.obj~5", "Wed May 19 01:31:37 PDT 1999"),
    OS("Mac OS X", "Beaker",  "10.0 DP2", "???", "1.0", "xnu-44.obj~1", "Mon Oct 25 23:31:09 PDT 1999"),
    OS("Mac OS X", "Bunsen",  "10.0 DP3", "???", "1.0"),
    OS("Mac OS X", "Gonzo",   "10.0 DP4", "???", "1.1"),
    OS("Mac OS X", "Cheetah", "10.0 Beta", "1H39", "1.2.1"),
    OS("Mac OS X", "Cheetah", "10.0 Beta", "2E14", "1.2.1"),

    # Cheetah
    OS("Mac OS X", "Cheetah", "10.0",   "4K78", "1.3"),  # RTM
    OS("Mac OS X", "Cheetah", "10.0",   "1P2",  "1.3"),  # Server Beta
    OS("Mac OS X", "Cheetah", "10.0",   "1W2",  "1.3"),  # Server Beta
    OS("Mac OS X", "Cheetah", "10.0.1", "4L5",  "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.1", "4L7",  "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.1", "4L8",  "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.1", "4L13", "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.2", "4P12", "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.3", "4P13", "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.3", "4M23", "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.4", "2G7",  "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.4", "4Q12", "1.3.1"),
    OS("Mac OS X", "Cheetah", "10.0.4", "4R14", "1.3.1"), # PowerMac G4
    OS("Mac OS X", "Cheetah", "10.0.4", "4R15", "1.3.1"), # iMac
    OS("Mac OS X", "Cheetah", "10.0.4", "4S10", "1.3.1"), # PowerMac G4

    # Puma
    OS("Mac OS X", "Puma", "10.1", "5G64", "1.4.1"),
    OS("Mac OS X", "Puma", "10.1.1", "5M28", "5.1"),
    OS("Mac OS X", "Puma", "10.1.2", "5P48", "5.2"),
    OS("Mac OS X", "Puma", "10.1.3", "5Q45", "5.3"),
    OS("Mac OS X", "Puma", "10.1.4", "5Q125", "5.4"),
    OS("Mac OS X", "Puma", "10.1.5", "5S60", "5.5"),

    # Jaguar
    OS("Mac OS X", "Jaguar", "10.2", "6C115", "6.0"),
    OS("Mac OS X", "Jaguar", "10.2", "6C115a", "6.0"),
    OS("Mac OS X", "Jaguar", "10.2.1", "6D52", "6.1"),
    OS("Mac OS X", "Jaguar", "10.2.2", "6F21", "6.2"),
    OS("Mac OS X", "Jaguar", "10.2.3", "6G30", "6.3"),
    OS("Mac OS X", "Jaguar", "10.2.3", "6G37", "6.3"),
    OS("Mac OS X", "Jaguar", "10.2.3", "6G50", "6.3"),
    OS("Mac OS X", "Jaguar", "10.2.4", "6I32", "6.4"),
    OS("Mac OS X", "Jaguar", "10.2.5", "6L29", "6.5"),
    OS("Mac OS X", "Jaguar", "10.2.6", "6L60", "6.6"),
    OS("Mac OS X", "Jaguar", "10.2.7", "6R65", "6.7"),
    OS("Mac OS X", "Jaguar", "10.2.8", "6R73", "6.8"),
    OS("Mac OS X", "Jaguar", "10.2.8", "6S90", "6.8"),

    # Panther
    OS("Mac OS X", "Panther", "10.3", "7B85", "7.0"),
    OS("Mac OS X", "Panther", "10.3", "7B86", "7.0"),
    OS("Mac OS X", "Panther", "10.3.1", "7C107", "7.1"),
    OS("Mac OS X", "Panther", "10.3.2", "7D24", "7.2"),
    OS("Mac OS X", "Panther", "10.3.2", "7D28", "7.2"),
    OS("Mac OS X", "Panther", "10.3.3", "7F44", "7.3"),
    OS("Mac OS X", "Panther", "10.3.4", "7H63", "7.4"),
    OS("Mac OS X", "Panther", "10.3.5", "7M34", "7.5"),
    OS("Mac OS X", "Panther", "10.3.6", "7R28", "7.6"),
    OS("Mac OS X", "Panther", "10.3.7", "7S215", "7.7"),
    OS("Mac OS X", "Panther", "10.3.8", "7U16", "7.8"),
    OS("Mac OS X", "Panther", "10.3.9", "7W98", "7.9"),

    # Tiger
    OS("Mac OS X", "Tiger", "10.4", "8A428", "8.0"),
    OS("Mac OS X", "Tiger", "10.4", "8A432", "8.0"),
    OS("Mac OS X", "Tiger", "10.4.1", "8B15", "8.1"),
    OS("Mac OS X", "Tiger", "10.4.1", "8B17", "8.1"),
    OS("Mac OS X", "Tiger", "10.4.2", "8C46", "8.2"),
    OS("Mac OS X", "Tiger", "10.4.2", "8C47", "8.2"),
    OS("Mac OS X", "Tiger", "10.4.2", "8E102", "8.2"),
    OS("Mac OS X", "Tiger", "10.4.2", "8E45", "8.2"),
    OS("Mac OS X", "Tiger", "10.4.2", "8E90", "8.2"),
    OS("Mac OS X", "Tiger", "10.4.3", "8F46", "8.3"),
    OS("Mac OS X", "Tiger", "10.4.4", "8G32", "8.4"),
    OS("Mac OS X", "Tiger", "10.4.4", "8G1165", "8.4"),
    OS("Mac OS X", "Tiger", "10.4.5", "8H14", "8.5"),
    OS("Mac OS X", "Tiger", "10.4.5", "8H1454", "8.5"),
    OS("Mac OS X", "Tiger", "10.4.6", "8I127", "8.6"),
    OS("Mac OS X", "Tiger", "10.4.6", "8I1119", "8.6"),
    OS("Mac OS X", "Tiger", "10.4.7", "8J135", "8.7"),
    OS("Mac OS X", "Tiger", "10.4.7", "8J2135a", "8.7"),
    OS("Mac OS X", "Tiger", "10.4.7", "8J1079", "8.7"),
    OS("Mac OS X", "Tiger", "10.4.7", "8J5107", "8.7"),
    OS("Mac OS X", "Tiger", "10.4.8", "8L127", "8.8"),
    OS("Mac OS X", "Tiger", "10.4.8", "8L2127", "8.8"),
    OS("Mac OS X", "Tiger", "10.4.9", "8P135", "8.9"),
    OS("Mac OS X", "Tiger", "10.4.9", "8P2137", "8.9"),
    OS("Mac OS X", "Tiger", "10.4.10", "8R218", "8.10"),
    OS("Mac OS X", "Tiger", "10.4.10", "8R2218", "8.10"),
    OS("Mac OS X", "Tiger", "10.4.10", "8R2232", "8.10"),
    OS("Mac OS X", "Tiger", "10.4.11", "8S165", "8.11"),
    OS("Mac OS X", "Tiger", "10.4.11", "8S2167", "8.11"),

    # Leopard
    OS("Mac OS X", "Leopard", "10.5", "9A581", "9.0"),
    OS("Mac OS X", "Leopard", "10.5.1", "9B18", "9.1"),
    OS("Mac OS X", "Leopard", "10.5.1", "9B2117", "9.1.1"),
    OS("Mac OS X", "Leopard", "10.5.2", "9C31", "9.2"),
    OS("Mac OS X", "Leopard", "10.5.2", "9C7010", "9.2"),
    OS("Mac OS X", "Leopard", "10.5.3", "9D34", "9.3"),
    OS("Mac OS X", "Leopard", "10.5.4", "9E17", "9.4"),
    OS("Mac OS X", "Leopard", "10.5.5", "9F33", "9.5"),
    OS("Mac OS X", "Leopard", "10.5.6", "9G55", "9.6"),
    OS("Mac OS X", "Leopard", "10.5.6", "9G66", "9.6"),
    OS("Mac OS X", "Leopard", "10.5.6", "9G71", "9.6"),
    OS("Mac OS X", "Leopard", "10.5.7", "9J61", "9.7"),
    OS("Mac OS X", "Leopard", "10.5.8", "9L30", "9.8"),
    OS("Mac OS X", "Leopard", "10.5.8", "9L34", "9.8"),

    # Snow Leopard
    OS("Mac OS X", "Snow Leopard", "10.6", "10A432", "10.0"),
    OS("Mac OS X", "Snow Leopard", "10.6", "10A433", "10.0"),
    OS("Mac OS X", "Snow Leopard", "10.6.1", "10B504", "10.1"),
    OS("Mac OS X", "Snow Leopard", "10.6.2", "10C540", "10.2"),
    OS("Mac OS X", "Snow Leopard", "10.6.3", "10D573", "10.3"),
    OS("Mac OS X", "Snow Leopard", "10.6.3", "10D575", "10.3"),
    OS("Mac OS X", "Snow Leopard", "10.6.3", "10D578", "10.3"),
    OS("Mac OS X", "Snow Leopard", "10.6.4", "10F569", "10.4"),
    OS("Mac OS X", "Snow Leopard", "10.6.5", "10H574", "10.5"),
    OS("Mac OS X", "Snow Leopard", "10.6.6", "10J567", "10.6"),
    OS("Mac OS X", "Snow Leopard", "10.6.7", "10J869", "10.7"),
    OS("Mac OS X", "Snow Leopard", "10.6.7", "10J3250", "10.7"),
    OS("Mac OS X", "Snow Leopard", "10.6.7", "10J4138", "10.7"),
    OS("Mac OS X", "Snow Leopard", "10.6.8", "10K540", "10.8"),
    OS("Mac OS X", "Snow Leopard", "10.6.8", "10K549", "10.8"),

    # Lion
    OS("Mac OS X", "Lion", "10.7", "11A511", "11.0"),
    OS("Mac OS X", "Lion", "10.7", "11A511s", "11.0"),
    OS("Mac OS X", "Lion", "10.7", "11A2061", "11.0.2"),
    OS("Mac OS X", "Lion", "10.7", "11A2063", "11.0.2"),
    OS("Mac OS X", "Lion", "10.7.1", "11B26", "11.1.0"),
    OS("Mac OS X", "Lion", "10.7.1", "11B2118", "11.1.0"),
    OS("Mac OS X", "Lion", "10.7.2", "11C74", "11.2"),
    OS("Mac OS X", "Lion", "10.7.3", "11D50", "11.3"),
    OS("Mac OS X", "Lion", "10.7.4", "11E53", "11.4"),
    OS("Mac OS X", "Lion", "10.7.5", "11G56", "11.4.2"),
    OS("Mac OS X", "Lion", "10.7.5", "11G63", "11.4.2"),

    # Mountain Lion
    OS("OS X", "Mountain Lion", "10.8", "12A269", "12.0"),
    OS("OS X", "Mountain Lion", "10.8.1", "12B19", "12.1"),
    OS("OS X", "Mountain Lion", "10.8.2", "12C54", "12.2"),
    OS("OS X", "Mountain Lion", "10.8.2", "12C60", "12.2"),
    OS("OS X", "Mountain Lion", "10.8.2", "12C2034", "12.2"),
    OS("OS X", "Mountain Lion", "10.8.2", "12C3104", "12.2"),
    OS("OS X", "Mountain Lion", "10.8.3", "12D78", "12.3"),
    OS("OS X", "Mountain Lion", "10.8.4", "12E55", "12.4"),
    OS("OS X", "Mountain Lion", "10.8.4", "12E3067", "12.4"),
    OS("OS X", "Mountain Lion", "10.8.4", "12E4022", "12.4"),
    OS("OS X", "Mountain Lion", "10.8.5", "12F37", "12.5"),
    OS("OS X", "Mountain Lion", "10.8.5", "12F45", "12.5"),  # FIXME: build 12F45 has both 12.5 and 12.6 Darwin?
    OS("OS X", "Mountain Lion", "10.8.5", "12F2501", "12.6"),
    OS("OS X", "Mountain Lion", "10.8.5", "12F2518", "12.6"),
    OS("OS X", "Mountain Lion", "10.8.5", "12F2542", "12.6"),
    OS("OS X", "Mountain Lion", "10.8.5", "12F2560", "12.6"),

    # Mavericks
    OS("OS X", "Mavericks", "10.9", "13A603", "13.0"),
    OS("OS X", "Mavericks", "10.9.1", "13B42", "13.0"),
    OS("OS X", "Mavericks", "10.9.2", "13C64", "13.1"),
    OS("OS X", "Mavericks", "10.9.2", "13C1021", "13.1"),
    OS("OS X", "Mavericks", "10.9.3", "13D65", "13.2"),
    OS("OS X", "Mavericks", "10.9.4", "13E28", "13.3"),
    OS("OS X", "Mavericks", "10.9.5", "13F34", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1066", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1077", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1096", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1112", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1134", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1507", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1603", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1712", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1808", "13.4"),
    OS("OS X", "Mavericks", "10.9.5", "13F1911", "13.4"),

    # Yosemite
    OS("OS X", "Yosemite", "10.10", "14A389", "14.0"),
    OS("OS X", "Yosemite", "10.10.1", "14B25", "14.0"),
    OS("OS X", "Yosemite", "10.10.2", "14C109", "14.1"),
    OS("OS X", "Yosemite", "10.10.2", "14C1510", "14.1"),
    OS("OS X", "Yosemite", "10.10.2", "14C2043", "14.1"),
    OS("OS X", "Yosemite", "10.10.2", "14C1514", "14.1"),
    OS("OS X", "Yosemite", "10.10.2", "14C2513", "14.1"),
    OS("OS X", "Yosemite", "10.10.3", "14D131", "14.3"),
    OS("OS X", "Yosemite", "10.10.3", "14D136", "14.3"),
    OS("OS X", "Yosemite", "10.10.4", "14E46", "14.4"),
    OS("OS X", "Yosemite", "10.10.5", "14F27", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1021", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1505", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1509", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1605", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1713", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1808", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1909", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F1912", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F2009", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F2109", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F2315", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F2411", "14.5"),
    OS("OS X", "Yosemite", "10.10.5", "14F2511", "14.5"),

    # El Capitan
    OS("OS X", "El Capitan", "10.11", "15A284", "15.0.0"),
    OS("OS X", "El Capitan", "10.11.1", "15B42", "15.0.0"),
    OS("OS X", "El Capitan", "10.11.2", "15C50", "15.2.0"),
    OS("OS X", "El Capitan", "10.11.3", "15D21", "15.3.0"),
    OS("OS X", "El Capitan", "10.11.4", "15E65", "15.4.0"),
    OS("OS X", "El Capitan", "10.11.5", "15F34", "15.5.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G31", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1004", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1011", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1108", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1212", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1217", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1421", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1510", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G1611", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G17023", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G18013", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G19009", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G20015", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G21013", "15.6.0"),
    OS("OS X", "El Capitan", "10.11.6", "15G22010", "15.6.0"),

    # Sierra
    OS("macOS", "Sierra", "10.12", "16A323", "16.0.0"),
    OS("macOS", "Sierra", "10.12.1", "16B2555", "16.1.0"),
    OS("macOS", "Sierra", "10.12.1", "16B2657", "16.1.0"),
    OS("macOS", "Sierra", "10.12.2", "16C67", "16.3.0"),
    OS("macOS", "Sierra", "10.12.2", "16C68", "16.3.0"),
    OS("macOS", "Sierra", "10.12.3", "16D32", "16.4.0"),
    OS("macOS", "Sierra", "10.12.4", "16E195", "16.5.0"),
    OS("macOS", "Sierra", "10.12.5", "16F73", "16.6.0"),
    OS("macOS", "Sierra", "10.12.6", "16G29", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1036", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1114", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1212", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1314", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1408", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1510", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1618", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1710", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1815", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1917", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G1918", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G2016", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G2127", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G2128", "16.7.0"),
    OS("macOS", "Sierra", "10.12.6", "16G2136", "16.7.0"),

    # High Sierra
    OS("macOS", "High Sierra", "10.13", "17A365", "17.0.0"),
    OS("macOS", "High Sierra", "10.13", "17A405", "17.0.0"),
    OS("macOS", "High Sierra", "10.13.1", "17B48", "17.2.0"),
    OS("macOS", "High Sierra", "10.13.1", "17B1002", "17.2.0"),
    OS("macOS", "High Sierra", "10.13.1", "17B1003", "17.2.0"),
    OS("macOS", "High Sierra", "10.13.2", "17C88", "17.3.0"),
    OS("macOS", "High Sierra", "10.13.2", "17C89", "17.3.0"),
    OS("macOS", "High Sierra", "10.13.2", "17C205", "17.3.0"),
    OS("macOS", "High Sierra", "10.13.2", "17C2205", "17.3.0"),
    OS("macOS", "High Sierra", "10.13.3", "17D47", "17.4.0"),
    OS("macOS", "High Sierra", "10.13.3", "17D2047", "17.4.0"),
    OS("macOS", "High Sierra", "10.13.3", "17D102", "17.4.0"),
    OS("macOS", "High Sierra", "10.13.3", "17D2102", "17.4.0"),
    OS("macOS", "High Sierra", "10.13.4", "17E199", "17.5.0"),
    OS("macOS", "High Sierra", "10.13.4", "17E202", "17.5.0"),
    OS("macOS", "High Sierra", "10.13.5", "17F77", "17.6.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G65", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G2208", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G2307", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G3025", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G4015", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G5019", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G6029", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G6030", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G7024", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G8029", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G8030", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G8037", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G9016", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G10021", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G11023", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G12034", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G13033", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G13035", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G14019", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G14033", "17.7.0"),
    OS("macOS", "High Sierra", "10.13.6", "17G14042", "17.7.0"),

    # Mojave
    OS("macOS", "Mojave", "10.14", "18A391", "18.0.0"),
    OS("macOS", "Mojave", "10.14.1", "18B75", "18.2.0"),
    OS("macOS", "Mojave", "10.14.1", "18B2107", "18.2.0"),
    OS("macOS", "Mojave", "10.14.1", "18B3094", "18.2.0"),
    OS("macOS", "Mojave", "10.14.2", "18C54", "18.2.0"),
    OS("macOS", "Mojave", "10.14.3", "18D42", "18.2.0"),
    OS("macOS", "Mojave", "10.14.3", "18D43", "18.2.0"),
    OS("macOS", "Mojave", "10.14.3", "18D109", "18.2.0"),
    OS("macOS", "Mojave", "10.14.4", "18E226", "18.5.0"),
    OS("macOS", "Mojave", "10.14.4", "18E227", "18.5.0"),
    OS("macOS", "Mojave", "10.14.5", "18F132", "18.6.0"),
    OS("macOS", "Mojave", "10.14.6", "18G84", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G87", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G95", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G103", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G1012", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G2022", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G3020", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G4032", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G5033", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G6020", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G6032", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G7016", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G8012", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G8022", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G9028", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G9216", "18.7.0"),
    OS("macOS", "Mojave", "10.14.6", "18G9323", "18.7.0"),

    # Catalina
    OS("macOS", "Catalina", "10.15", "19A583", "19.0.0"),
    OS("macOS", "Catalina", "10.15", "19A602", "19.0.0"),
    OS("macOS", "Catalina", "10.15", "19A603", "19.0.0"),
    OS("macOS", "Catalina", "10.15.1", "19B88", "19.0.0"),
    OS("macOS", "Catalina", "10.15.2", "19C57", "19.2.0"),
    OS("macOS", "Catalina", "10.15.2", "19C58", "19.2.0"),
    OS("macOS", "Catalina", "10.15.3", "19D76", "19.3.0"),
    OS("macOS", "Catalina", "10.15.4", "19E266", "19.4.0"),
    OS("macOS", "Catalina", "10.15.4", "19E287", "19.4.0"),
    OS("macOS", "Catalina", "10.15.5", "19F96", "19.5.0"),
    OS("macOS", "Catalina", "10.15.5", "19F101", "19.5.0"),
    OS("macOS", "Catalina", "10.15.6", "19G73", "19.6.0"),
    OS("macOS", "Catalina", "10.15.6", "19G2021", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H2", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H4", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H15", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H114", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H512", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H524", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1030", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1217", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1323", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1417", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1419", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1519", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1615", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1713", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1715", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1824", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H1922", "19.6.0"),
    OS("macOS", "Catalina", "10.15.7", "19H2026", "19.6.0"),

    # Big Sur
    OS("macOS", "Big Sur", "10.16 Beta", "20A2261g", "20.0.0"),  # DTK prototype; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A4299v", "20.0.0"),  # Dev beta 1; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5299w", "20.0.0"),  # DTK/SDK/Xcode beta 1; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A4300b", "20.0.0"),  # Dev beta 2; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5323l", "20.0.0"),  # Dev beta 3; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5343i", "20.0.0"),  # Dev beta 4; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5343j", "20.0.0"),  # Public Beta 1; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5354i", "20.0.0"),  # Dev Beta 5/Public Beta 2; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5364e", "20.0.0"),  # Dev Beta 6/Public Beta 3; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5374f", "20.0.0"),  # DTK/SDK/Xcode beta 7; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5374g", "20.0.0"),  # Dev Beta 7; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5374i", "20.0.0"),  # Dev Beta 8/Public Beta 4; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5384c", "20.0.0"),  # Dev Beta 9/Public Beta 5; Darwin unknown
    OS("macOS", "Big Sur", "10.16 Beta", "20A5395g", "20.0.0"),  # Dev Beta 10/Public Beta 6; Darwin unknown
    OS("macOS", "Big Sur", "11.0",       "20A2411",  "20.1.0"),  # RTM
    OS("macOS", "Big Sur", "11.0.1",     "20B5012d", "20.1.0"),  # Beta 1
    OS("macOS", "Big Sur", "11.0.1",     "20B5022a", "20.1.0"),  # Beta 2 / Release candidate
    OS("macOS", "Big Sur", "11.0.1",     "20B28",    "20.1.0"),  # Release Candidate 2
    OS("macOS", "Big Sur", "11.0.1",     "20B29",    "20.1.0"),  # RTM
    OS("macOS", "Big Sur", "11.0.1",     "20B50",    "20.1.0"),  # Revised update
    OS("macOS", "Big Sur", "11.1",       "20C69",    "20.2.0"),
    OS("macOS", "Big Sur", "11.2",       "20D64",    "20.3.0"),
    OS("macOS", "Big Sur", "11.2.1",     "20D74",    "20.3.0"),
    OS("macOS", "Big Sur", "11.2.1",     "20D75",    "20.3.0"),
    OS("macOS", "Big Sur", "11.2.2",     "20D80",    "20.3.0"),
    OS("macOS", "Big Sur", "11.2.3",     "20D91",    "20.3.0"),
    OS("macOS", "Big Sur", "11.3",       "20E232",  "20.4.0"),
    OS("macOS", "Big Sur", "11.3.1",     "20E241",  "20.4.0"),
    OS("macOS", "Big Sur", "11.4",       "20F71",   "20.5.0"),
    OS("macOS", "Big Sur", "11.5",       "20G71",   "20.6.0"),
    OS("macOS", "Big Sur", "11.5.1",     "20G80",   "20.6.0"),
    OS("macOS", "Big Sur", "11.5.2",     "20G95",   "20.6.0"),
    OS("macOS", "Big Sur", "11.6",       "20G165",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.1",     "20G224",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.2",     "20G314",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.3",     "20G415",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.4",     "20G417",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.5",     "20G527",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.6",     "20G624",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.7",     "20G630",  "20.6.0"),
    OS("macOS", "Big Sur", "11.6.8",     "20G730",  "20.6.0"),
    OS("macOS", "Big Sur", "11.7",       "20G817",  "20.6.0"),
    OS("macOS", "Big Sur", "11.7.1 RC3", "20G916",  "20.6.0"),
    OS("macOS", "Big Sur", "11.7.1",     "20G918",  "20.6.0"),
    OS("macOS", "Big Sur", "11.7.2",     "20G1020", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.3",     "20G1116", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.4",     "20G1120", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.5 RC",  "20G1205", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.5 RC3", "20G1215", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.5 RC4", "20G1220", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.5",     "20G1225", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.6 RC",  "20G1329", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.6",     "20G1331", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.7 RC3", "20G1338", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.7 RC4", "20G1342", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.7",     "20G1345", "20.6.0"),  # RC5 has same versions
    OS("macOS", "Big Sur", "11.7.8 RC2", "20G1407", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.9 RC3", "20G1413", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.8",     "20G1351", "20.6.0"),  # check version
    OS("macOS", "Big Sur", "11.7.9 RC3", "20G1413", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.9 RC4", "20G1416", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.9 RC5", "20G1424", "20.6.0"),
    OS("macOS", "Big Sur", "11.7.9",     "20G1426", "20.6.0", "xnu-7195.141.49.702.12~1", "Thu Jul  6 22:12:47 PDT 2023"),
    OS("macOS", "Big Sur", "11.7.10",    "20G1427", "20.6.0", "xnu-7195.141.49.702.12~1", "Thu Jul  6 22:12:47 PDT 2023"),

    # Monterey
    OS("macOS", "Monterey", "12.0", "21A344", "21.0.1"),
    OS("macOS", "Monterey", "21.0.1", "21A559", "21.1.0"),
    OS("macOS", "Monterey", "12.1", "21C52", "21.2.0"),
    OS("macOS", "Monterey", "12.2", "21D49", "21.3.0"),
    OS("macOS", "Monterey", "12.2.1", "21D62", "21.3.0"),
    OS("macOS", "Monterey", "12.3", "21E230", "21.4.0"),
    OS("macOS", "Monterey", "12.3.1", "21E258", "21.4.0"),
    OS("macOS", "Monterey", "12.4", "21F79", "21.5.0"),
    OS("macOS", "Monterey", "12.4", "21F2081", "21.5.0"),
    OS("macOS", "Monterey", "12.4", "21F2092", "21.5.0"),
    OS("macOS", "Monterey", "12.5", "21G72", "21.6.0"),
    OS("macOS", "Monterey", "12.5.1", "21G83", "21.6.0"),
    OS("macOS", "Monterey", "12.6", "21G115", "21.6.0"),
    OS("macOS", "Monterey", "12.6.1", "21G217", "21.6.0"),
    OS("macOS", "Monterey", "12.6.2", "21G320", "21.6.0"),
    OS("macOS", "Monterey", "12.6.3", "21G419", "21.6.0"),
    OS("macOS", "Monterey", "12.6.4 RC", "21G506", "21.6.0"),
    OS("macOS", "Monterey", "12.6.4 RC3", "21G516", "21.6.0"),
    OS("macOS", "Monterey", "12.6.4 RC4", "21G521", "21.6.0"),
    OS("macOS", "Monterey", "12.6.4", "21G526", "21.6.0"),  # also RC5
    OS("macOS", "Monterey", "12.6.5 RC", "21G630", "21.6.0"),
    OS("macOS", "Monterey", "12.6.5", "21G531", "21.6.0"),
    OS("macOS", "Monterey", "12.6.6 RC2", "21G633", "21.6.0"),
    OS("macOS", "Monterey", "12.6.6 RC3", "21G639", "21.6.0"),
    OS("macOS", "Monterey", "12.6.6 RC4", "21G644", "21.6.0"),
    OS("macOS", "Monterey", "12.6.6", "21G646", "21.6.0"),
    OS("macOS", "Monterey", "12.6.7 RC2", "21G708", "21.6.0"),
    OS("macOS", "Monterey", "12.6.8 RC3", "21G713", "21.6.0"),
    OS("macOS", "Monterey", "12.6.7", "21G651", "21.6.0"),
    OS("macOS", "Monterey", "12.6.8 RC4", "21G716", "21.6.0"),
    OS("macOS", "Monterey", "12.6.8 RC5", "21G724", "21.6.0"),
    OS("macOS", "Monterey", "12.6.8", "21G725", "21.6.0"), # also RC6
    OS("macOS", "Monterey", "12.6.9", "21G726", "21.6.0"),
    OS("macOS", "Monterey", "12.7 RC", "21G808", "21.6.0"),
    OS("macOS", "Monterey", "12.7 RC2", "21G813", "21.6.0"),
    OS("macOS", "Monterey", "12.7 RC3", "21G814", "21.6.0"),
    OS("macOS", "Monterey", "12.7",       "21G816",  "21.6.0"),
    OS("macOS", "Monterey", "12.7.1 RC",  "21G913",  "21.6.0"),
    OS("macOS", "Monterey", "12.7.1 RC2", "21G918",  "21.6.0"),
    OS("macOS", "Monterey", "12.7.1",     "21G920",  "21.6.0"),
    OS("macOS", "Monterey", "12.7.2 RC",  "21G1925", "21.6.0"),
    OS("macOS", "Monterey", "12.7.2 RC2", "21G1965", "21.6.0"),
    OS("macOS", "Monterey", "12.7.2 RC3", "21G1967", "21.6.0"),
    OS("macOS", "Monterey", "12.7.2 RC4", "21G1971", "21.6.0"),
    OS("macOS", "Monterey", "12.7.2",     "21G1974", "21.6.0"), # also RC5
    OS("macOS", "Monterey", "12.7.3 RC",  "21H1006", "21.6.0"),
    OS("macOS", "Monterey", "12.7.3 RC2", "21H1009", "21.6.0"),
    OS("macOS", "Monterey", "12.7.3 RC3", "21H1013", "21.6.0"),
    OS("macOS", "Monterey", "12.7.3",     "21H1015", "21.6.0"), # also RC4
    OS("macOS", "Monterey", "12.7.4 RC",  "21H1105", "21.6.0"),
    OS("macOS", "Monterey", "12.7.4 RC2", "21H1111", "21.6.0"),

    # Ventura
    OS("macOS", "Ventura", "13.0",       "22A380",     "22.1.0", "xnu-8792.41.9~2", "Sun Oct 9 20:15:52 PDT 2022"),
    OS("macOS", "Ventura", "13.0",       "22A8380",    "22.1.0", "xnu-8792.41.9~2", "Sun Oct 9 20:15:52 PDT 2022"),
    OS("macOS", "Ventura", "13.0.1",     "22A400",     "22.1.0", "xnu-8792.41.9~2", "Sun Oct 9 20:15:52 PDT 2022"),
    OS("macOS", "Ventura", "13.1",       "22C65",      "22.2.0", "xnu-8792.61.2~4", "Fri Nov 11 02:06:26 PST 2022"),
    OS("macOS", "Ventura", "13.2",       "22D49",      "22.3.0", "xnu-8792.81.2~2", "Thu Jan 5 20:53:49 PST 2023"),
    OS("macOS", "Ventura", "13.2.1",     "22D68",      "22.3.0", "xnu-8792.81.3~2", "Mon Jan 30 20:38:43 PST 2023"),
    OS("macOS", "Ventura", "13.3",       "22E252",     "22.4.0", "xnu-8796.101.5~3", "Mon Mar 6 20:59:28 PST 2023"),
    OS("macOS", "Ventura", "13.3.1",     "22E261",     "22.4.0", "xnu-8796.101.5~3", "Mon Mar 6 20:59:28 PST 2023"),
    OS("macOS", "Ventura", "13.3.1 (a)", "22E772610a", "22.4.0", "xnu-8796.101.5~3", "Mon Mar 6 20:59:28 PST 2023"),
    OS("macOS", "Ventura", "13.4",       "22F66",      "22.5.0", "xnu-8796.121.2~5", "Mon Apr 24 20:52:43 PDT 2023"),
    OS("macOS", "Ventura", "13.4.1",     "22F82",      "22.5.0", "xnu-8796.121.3~7", "Thu Jun 8 22:22:22 PDT 2023"),
    OS("macOS", "Ventura", "13.4.1 (a)", "22F770820b", "22.5.0", "xnu-8796.121.3~7", "Thu Jun 8 22:22:22 PDT 2023"),
    OS("macOS", "Ventura", "13.4.1 (c)", "22F770820d", "22.5.0", "xnu-8796.121.3~7", "Thu Jun 8 22:22:22 PDT 2023"),
    OS("macOS", "Ventura", "13.5",       "22G74",      "22.6.0", "xnu-8796.141.3~6", "Wed Jul 5 22:21:56 PDT 2023"),
    OS("macOS", "Ventura", "13.5.1",     "22G90",      "22.6.0", "xnu-8796.141.3~6", "Wed Jul 5 22:21:56 PDT 2023"),
    OS("macOS", "Ventura", "13.5.2",     "22G91",      "22.6.0", "xnu-8796.141.3~6", "Wed Jul 5 22:21:56 PDT 2023"),
    OS("macOS", "Ventura", "13.6",       "22G120",     "22.6.0", "xnu-8796.141.3.700.8~1", "Fri Sep 15 13:39:52 PDT 2023"),
    OS("macOS", "Ventura", "13.6.1",     "22G313",     "22.6.0", "xnu-8796.141.3.701.17~4", "Wed Oct 4 21:25:26 PDT 2023"),
    OS("macOS", "Ventura", "13.6.2",     "22G320",     "22.6.0", "xnu-8796.141.3.701.17~6", "Thu Nov 2 07:43:57 PDT 2023"),
    OS("macOS", "Ventura", "13.6.3",     "22G436",     "22.6.0", "xnu-8796.141.3.702.9~2", "Tue Nov 7 21:48:06 PST 2023"),
    OS("macOS", "Ventura", "13.6.4",     "22G513",     "22.6.0", "xnu-8796.141.3.703.2~2", "Sun Dec 17 22:18:09 PST 2023"),

    # Sonoma
    OS("macOS", "Sonoma", "14.0 B1",  "23A5257q", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B2",  "23A5276g", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B3",  "23A5286g", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B3",  "23A5286i", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B4",  "23A5301g", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B4",  "23A5301h", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B5",  "23A5312d", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B6",  "23A5328b", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 B7",  "23A5337a", "23.0.0"),
    OS("macOS", "Sonoma", "14.0 RC",  "23A339",   "23.0.0"),
    OS("macOS", "Sonoma", "14.0 RC2", "23A344",   "23.0.0"),
    OS("macOS", "Sonoma", "14.0",     "23A344",   "23.0.0", "xnu-10002.1.13~1", "Fri Sep 15 14:41:34 PDT 2023"),
    OS("macOS", "Sonoma", "14.1",     "23B74",    "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:27:27 PDT 2023"),
    OS("macOS", "Sonoma", "14.1.1",   "23B81",    "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:26:29 PDT 2023"),
    OS("macOS", "Sonoma", "14.1.1",   "23B2082",  "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:26:29 PDT 2023"),
    OS("macOS", "Sonoma", "14.1.2",   "23B92",    "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:27:27 PDT 2023"),
    OS("macOS", "Sonoma", "14.1.2",   "23B2091",  "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:27:27 PDT 2023"),
    OS("macOS", "Sonoma", "14.2",     "23C64",    "23.2.0", "xnu-10002.61.3~2", "Wed Nov 15 21:54:10 PST 2023"),
    OS("macOS", "Sonoma", "14.2.1",   "23C71",    "23.2.0", "xnu-10002.61.3~2", "Wed Nov 15 21:54:10 PST 2023"),
    OS("macOS", "Sonoma", "14.3",     "23D56",    "23.3.0", "xnu-10002.81.5~7", "Wed Dec 20 21:30:27 PST 2023"),
    OS("macOS", "Sonoma", "14.3.1",   "23D60",    "23.3.0", "xnu-10002.81.5~7", "Wed Dec 20 21:28:58 PST 2023"),
]


def _read_sw_vers():
    """(Internal) Read software version information from sw_vers command."""
    info = {}

    p = os.popen("sw_vers")
    lines = p.readlines()
    p.close()

    for line in lines:
        bits = line.strip().split()
        info[bits[0][:-1]] = bits[1]

    return info


def get_host_os():
    """Get OS instance describing the current host environment.

    :returns: an OS class instance"""

    # Read output from sw_vers utility
    sw_vers = {}
    with os.popen("sw_vers") as p:
        lines = p.readlines()

        for line in lines:
            bits = line.strip().split()
            sw_vers[bits[0][:-1]] = bits[1]

    build = sw_vers.get("BuildVersion")

    # Get uname(3) info.
    posix_attrs = os.uname()

    darwin_version = posix_attrs.release

    bits = posix_attrs.version.split(': ', 1)
    if len(bits) != 2:
        raise ValueError(f"Unrecognized uname version: [{posix_attrs.version}]")

    bits = bits[1].split('; ', 1)
    if len(bits) != 2:
        raise ValueError(f"Unrecognized uname version: [{posix_attrs.version}]")

    kernel_date = bits[0]

    bits = bits[1].split(':', 1)
    if len(bits) != 2:
        raise ValueError(f"Unrecognized uname version: [{posix_attrs.version}]")

    bits = bits[1].split('/', 1)
    if len(bits) != 2:
        raise ValueError(f"Unrecognized uname version: [{posix_attrs.version}]")

    kernel_version = bits[0]

    # Lookup based on host properties.
    l = lookup(build=build, darwin=darwin_version, kernel=kernel_version, date=kernel_date)
    if (len(l)) != 1:
        raise ValueError(f"Unable to match version: Build {build} Darwin {darwin_version}, Kernel {kernel_version}, Date {kernel_date}")

    return l[0]


def lookup(**args) -> Sequence[OS]:
    """Look up a release by its attributes.

    Possible attribute names are:
    product: the product name, so far one of: "Mac OS X" or "macOS"
    name: the release name, eg. "Ventura"
    version: the string product version, eg. "13.6.4"
    build: the string build number, eg. "22G513"
    darwin: the Darwin kernel version number string, eg. "22.6.0"
    kernel: the kernel build string, eg. "xnu-8796.141.3.703.2~2"
    date: the kernel build date in RFC-2822 format, eg. "Sun Dec 17 22:18:09 PST 2023"

    You can supply zero or more attributes, and the result must match all of them.

    :returns: a list of matching OS instances"""

    for key in args:
        if key not in ("product", "name", "version", "build", "darwin", "kernel", "date"):
            raise KeyError(f"Unsupported release attribute: [{key}]")

    l = _BUILDS

    if "product" in args:
        l = [release for release in l if release.product == args["product"]]

    if "name" in args:
        l = [release for release in l if release.name == args["name"]]

    if "version" in args:
        l = [release for release in l if release.version == args["version"]]

    if "build" in args:
        l = [release for release in l if release.build == args["build"]]

    if "darwin" in args:
        l = [release for release in l if release.darwin == args["darwin"]]

    if "kernel" in args:
        l = [release for release in l if release.kernel == args["kernel"]]

    if "date" in args:
        l = [release for release in l if release.date == args["date"]]

    return l


def getMacOSRelease(darwin_version: str = None) -> (str, str):
    """(Deprecated) Return tuple of product name and version string.

    :param darwin_version: optional Darwin kernel version to get earliest release with that kernel
    :returns: product name, product version string"""

    if not darwin_version:
        release = get_host_os()
        return (release.name, release.version)

    # Return earliest release matching Darwin version.
    releases = sorted(lookup(darwin=darwin_version), key=lambda r: r.date or " ")
    if len(releases) < 1:
        raise KeyError(f"Unable to match Darwin version {darwin_version} to a release.")
    return (releases[0].name, releases[0].version)


if __name__ == "__main__":
    print(get_host_os().full_name)
    print(getMacOSRelease())
    print(getMacOSRelease("21.6.0"))
    print(getMacOSRelease("20.6.0"))
    print(getMacOSRelease("20.0.0"))
