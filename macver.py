__all__ = ["get_macos_product_name",
           "get_macos_version",
           "get_macos_build",
           "get_macos_darwin_version",
           "get_macos_full_name"]

import os
from typing import Optional


class OS:
    def __init__(self, product: str, name: str, version: str, darwin: str = None, release: str = None, date: str = None):
        self.product = product
        self.name = name
        self.version = version
        self.darwin = darwin if darwin is not None else ""
        self.release = release if release is not None else ""
        self.date = date if date is not None else ""


#1    OS("Mac OS X", "Developer Preview 3").codename("Bunsen"),
#1    OS("Mac OS X", "Developer Preview 4").codename("Gonzo"),
#1    OS("Mac OS X", "10.0 CHeetah Public Beta").codename("Kodiak"),
#1    OS("Mac OS X", "Public Release 1").codename("Hera"),
#1    OS("Mac OS X", "Public Release 2").codename("Beaker"),


BUILDS = {
    # Cheetah
    "4K78": OS("Mac OS X", "Cheetah", "10.0", "1.3"),
    "4L13": OS("Mac OS X", "Cheetah", "10.0.1", "1.3.1"),
    "4P12": OS("Mac OS X", "Cheetah", "10.0.2", "1.3.1"),
    "4P13": OS("Mac OS X", "Cheetah", "10.0.3", "1.3.1"),
    "4Q12": OS("Mac OS X", "Cheetah", "10.0.4", "1.3.1"),
    "4R14": OS("Mac OS X", "Cheetah", "10.0.4", "1.3.1"),
    "4S10": OS("Mac OS X", "Cheetah", "10.0.4", "1.3.1"),

    # Puma
    "5G64": OS("Mac OS X", "Puma", "10.1", "1.4.1"),
    "5M28": OS("Mac OS X", "Puma", "10.1.1", "5.1"),
    "5P48": OS("Mac OS X", "Puma", "10.1.2", "5.2"),
    "5Q45": OS("Mac OS X", "Puma", "10.1.3", "5.3"),
    "5Q125": OS("Mac OS X", "Puma", "10.1.4", "5.4"),
    "5S60": OS("Mac OS X", "Puma", "10.1.5", "5.5"),

    # Jaguar
    "6C115": OS("Mac OS X", "Jaguar", "10.2", "6.0"),
    "6C115a": OS("Mac OS X", "Jaguar", "10.2", "6.0"),
    "6D52": OS("Mac OS X", "Jaguar", "10.2.1", "6.1"),
    "6F21": OS("Mac OS X", "Jaguar", "10.2.2", "6.2"),
    "6G30": OS("Mac OS X", "Jaguar", "10.2.3", "6.3"),
    "6G37": OS("Mac OS X", "Jaguar", "10.2.3", "6.3"),
    "6G50": OS("Mac OS X", "Jaguar", "10.2.3", "6.3"),
    "6I32": OS("Mac OS X", "Jaguar", "10.2.4", "6.4"),
    "6L29": OS("Mac OS X", "Jaguar", "10.2.5", "6.5"),
    "6L60": OS("Mac OS X", "Jaguar", "10.2.6", "6.6"),
    "6R65": OS("Mac OS X", "Jaguar", "10.2.7", "6.7"),
    "6R73": OS("Mac OS X", "Jaguar", "10.2.8", "6.8"),
    "6S90": OS("Mac OS X", "Jaguar", "10.2.8", "6.8"),

    # Panther
    "7B85": OS("Mac OS X", "Panther", "10.3", "7.0"),
    "7B86": OS("Mac OS X", "Panther", "10.3", "7.0"),
    "7C107": OS("Mac OS X", "Panther", "10.3.1", "7.1"),
    "7D24": OS("Mac OS X", "Panther", "10.3.2", "7.2"),
    "7D28": OS("Mac OS X", "Panther", "10.3.2", "7.2"),
    "7F44": OS("Mac OS X", "Panther", "10.3.3", "7.3"),
    "7H63": OS("Mac OS X", "Panther", "10.3.4", "7.4"),
    "7M34": OS("Mac OS X", "Panther", "10.3.5", "7.5"),
    "7R28": OS("Mac OS X", "Panther", "10.3.6", "7.6"),
    "7S215": OS("Mac OS X", "Panther", "10.3.7", "7.7"),
    "7U16": OS("Mac OS X", "Panther", "10.3.8", "7.8"),
    "7W98": OS("Mac OS X", "Panther", "10.3.9", "7.9"),

    # Tiger
    "8A428": OS("Mac OS X", "Tiger", "10.4", "8.0"),
    "8A432": OS("Mac OS X", "Tiger", "10.4", "8.0"),
    "8B15": OS("Mac OS X", "Tiger", "10.4.1", "8.1"),
    "8B17": OS("Mac OS X", "Tiger", "10.4.1", "8.1"),
    "8C46": OS("Mac OS X", "Tiger", "10.4.2", "8.2"),
    "8C47": OS("Mac OS X", "Tiger", "10.4.2", "8.2"),
    "8E102": OS("Mac OS X", "Tiger", "10.4.2", "8.2"),
    "8E45": OS("Mac OS X", "Tiger", "10.4.2", "8.2"),
    "8E90": OS("Mac OS X", "Tiger", "10.4.2", "8.2"),
    "8F46": OS("Mac OS X", "Tiger", "10.4.3", "8.3"),
    "8G32": OS("Mac OS X", "Tiger", "10.4.4", "8.4"),
    "8G1165": OS("Mac OS X", "Tiger", "10.4.4", "8.4"),
    "8H14": OS("Mac OS X", "Tiger", "10.4.5", "8.5"),
    "8H1454": OS("Mac OS X", "Tiger", "10.4.5", "8.5"),
    "8I127": OS("Mac OS X", "Tiger", "10.4.6", "8.6"),
    "8I1119": OS("Mac OS X", "Tiger", "10.4.6", "8.6"),
    "8J135": OS("Mac OS X", "Tiger", "10.4.7", "8.7"),
    "8J2135a": OS("Mac OS X", "Tiger", "10.4.7", "8.7"),
    "8J1079": OS("Mac OS X", "Tiger", "10.4.7", "8.7"),
    "8J5107": OS("Mac OS X", "Tiger", "10.4.7", "8.7"),
    "8L127": OS("Mac OS X", "Tiger", "10.4.8", "8.8"),
    "8L2127": OS("Mac OS X", "Tiger", "10.4.8", "8.8"),
    "8P135": OS("Mac OS X", "Tiger", "10.4.9", "8.9"),
    "8P2137": OS("Mac OS X", "Tiger", "10.4.9", "8.9"),
    "8R218": OS("Mac OS X", "Tiger", "10.4.10", "8.10"),
    "8R2218": OS("Mac OS X", "Tiger", "10.4.10", "8.10"),
    "8R2232": OS("Mac OS X", "Tiger", "10.4.10", "8.10"),
    "8S165": OS("Mac OS X", "Tiger", "10.4.11", "8.11"),
    "8S2167": OS("Mac OS X", "Tiger", "10.4.11", "8.11"),

    # Leopard
    "9A581": OS("Mac OS X", "Leopard", "10.5", "9.0"),
    "9B18": OS("Mac OS X", "Leopard", "10.5.1", "9.1"),
    "9B2117": OS("Mac OS X", "Leopard", "10.5.1", "9.1.1"),
    "9C31": OS("Mac OS X", "Leopard", "10.5.2", "9.2"),
    "9C7010": OS("Mac OS X", "Leopard", "10.5.2", "9.2"),
    "9D34": OS("Mac OS X", "Leopard", "10.5.3", "9.3"),
    "9E17": OS("Mac OS X", "Leopard", "10.5.4", "9.4"),
    "9F33": OS("Mac OS X", "Leopard", "10.5.5", "9.5"),
    "9G55": OS("Mac OS X", "Leopard", "10.5.6", "9.6"),
    "9G66": OS("Mac OS X", "Leopard", "10.5.6", "9.6"),
    "9G71": OS("Mac OS X", "Leopard", "10.5.6", "9.6"),
    "9J61": OS("Mac OS X", "Leopard", "10.5.7", "9.7"),
    "9L30": OS("Mac OS X", "Leopard", "10.5.8", "9.8"),
    "9L34": OS("Mac OS X", "Leopard", "10.5.8", "9.8"),

    # Snow Leopard
    "10A432": OS("Mac OS X", "Snow Leopard", "10.6", "10.0"),
    "10A433": OS("Mac OS X", "Snow Leopard", "10.6", "10.0"),
    "10B504": OS("Mac OS X", "Snow Leopard", "10.6.1", "10.1"),
    "10C540": OS("Mac OS X", "Snow Leopard", "10.6.2", "10.2"),
    "10D573": OS("Mac OS X", "Snow Leopard", "10.6.3", "10.3"),
    "10D575": OS("Mac OS X", "Snow Leopard", "10.6.3", "10.3"),
    "10D578": OS("Mac OS X", "Snow Leopard", "10.6.3", "10.3"),
    "10F569": OS("Mac OS X", "Snow Leopard", "10.6.4", "10.4"),
    "10H574": OS("Mac OS X", "Snow Leopard", "10.6.5", "10.5"),
    "10J567": OS("Mac OS X", "Snow Leopard", "10.6.6", "10.6"),
    "10J869": OS("Mac OS X", "Snow Leopard", "10.6.7", "10.7"),
    "10J3250": OS("Mac OS X", "Snow Leopard", "10.6.7", "10.7"),
    "10J4138": OS("Mac OS X", "Snow Leopard", "10.6.7", "10.7"),
    "10K540": OS("Mac OS X", "Snow Leopard", "10.6.8", "10.8"),
    "10K549": OS("Mac OS X", "Snow Leopard", "10.6.8", "10.8"),

    # Lion
    "11A511": OS("Mac OS X", "Lion", "10.7", "11.0"),
    "11A511s": OS("Mac OS X", "Lion", "10.7", "11.0"),
    "11A2061": OS("Mac OS X", "Lion", "10.7", "11.0.2"),
    "11A2063": OS("Mac OS X", "Lion", "10.7", "11.0.2"),
    "11B26": OS("Mac OS X", "Lion", "10.7.1", "11.1.0"),
    "11B2118": OS("Mac OS X", "Lion", "10.7.1", "11.1.0"),
    "11C74": OS("Mac OS X", "Lion", "10.7.2", "11.2"),
    "11D50": OS("Mac OS X", "Lion", "10.7.3", "11.3"),
    "11E53": OS("Mac OS X", "Lion", "10.7.4", "11.4"),
    "11G56": OS("Mac OS X", "Lion", "10.7.5", "11.4.2"),
    "11G63": OS("Mac OS X", "Lion", "10.7.5", "11.4.2"),

    # Mountain Lion
    "12A269": OS("OS X", "Mountain Lion", "10.8", "12.0"),
    "12B19": OS("OS X", "Mountain Lion", "10.8.1", "12.1"),
    "12C54": OS("OS X", "Mountain Lion", "10.8.2", "12.2"),
    "12C60": OS("OS X", "Mountain Lion", "10.8.2", "12.2"),
    "12C2034": OS("OS X", "Mountain Lion", "10.8.2", "12.2"),
    "12C3104": OS("OS X", "Mountain Lion", "10.8.2", "12.2"),
    "12D78": OS("OS X", "Mountain Lion", "10.8.3", "12.3"),
    "12E55": OS("OS X", "Mountain Lion", "10.8.4", "12.4"),
    "12E3067": OS("OS X", "Mountain Lion", "10.8.4", "12.4"),
    "12E4022": OS("OS X", "Mountain Lion", "10.8.4", "12.4"),
    "12F37": OS("OS X", "Mountain Lion", "10.8.5", "12.5"),
    "12F45": OS("OS X", "Mountain Lion", "10.8.5", "12.5"),  # FIXME: build 12F45 has both 12.5 and 12.6 Darwin?
    "12F2501": OS("OS X", "Mountain Lion", "10.8.5", "12.6"),
    "12F2518": OS("OS X", "Mountain Lion", "10.8.5", "12.6"),
    "12F2542": OS("OS X", "Mountain Lion", "10.8.5", "12.6"),
    "12F2560": OS("OS X", "Mountain Lion", "10.8.5", "12.6"),

    # Mavericks
    "13A603": OS("OS X", "Mavericks", "10.9", "13.0"),
    "13B42": OS("OS X", "Mavericks", "10.9.1", "13.0"),
    "13C64": OS("OS X", "Mavericks", "10.9.2", "13.1"),
    "13C1021": OS("OS X", "Mavericks", "10.9.2", "13.1"),
    "13D65": OS("OS X", "Mavericks", "10.9.3", "13.2"),
    "13E28": OS("OS X", "Mavericks", "10.9.4", "13.3"),
    "13F34": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1066": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1077": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1096": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1112": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1134": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1507": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1603": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1712": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1808": OS("OS X", "Mavericks", "10.9.5", "13.4"),
    "13F1911": OS("OS X", "Mavericks", "10.9.5", "13.4"),

    # Yosemite
    "14A389": OS("OS X", "Yosemite", "10.10", "14.0"),
    "14B25": OS("OS X", "Yosemite", "10.10.1", "14.0"),
    "14C109": OS("OS X", "Yosemite", "10.10.2", "14.1"),
    "14C1510": OS("OS X", "Yosemite", "10.10.2", "14.1"),
    "14C2043": OS("OS X", "Yosemite", "10.10.2", "14.1"),
    "14C1514": OS("OS X", "Yosemite", "10.10.2", "14.1"),
    "14C2513": OS("OS X", "Yosemite", "10.10.2", "14.1"),
    "14D131": OS("OS X", "Yosemite", "10.10.3", "14.3"),
    "14D136": OS("OS X", "Yosemite", "10.10.3", "14.3"),
    "14E46": OS("OS X", "Yosemite", "10.10.4", "14.4"),
    "14F27": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1021": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1505": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1509": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1605": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1713": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1808": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1909": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F1912": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F2009": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F2109": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F2315": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F2411": OS("OS X", "Yosemite", "10.10.5", "14.5"),
    "14F2511": OS("OS X", "Yosemite", "10.10.5", "14.5"),

    # El Capitan
    "15A284": OS("OS X", "El Capitan", "10.11", "15.0.0"),
    "15B42": OS("OS X", "El Capitan", "10.11.1", "15.0.0"),
    "15C50": OS("OS X", "El Capitan", "10.11.2", "15.2.0"),
    "15D21": OS("OS X", "El Capitan", "10.11.3", "15.3.0"),
    "15E65": OS("OS X", "El Capitan", "10.11.4", "15.4.0"),
    "15F34": OS("OS X", "El Capitan", "10.11.5", "15.5.0"),
    "15G31": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1004": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1011": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1108": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1212": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1217": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1421": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1510": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G1611": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G17023": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G18013": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G19009": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G20015": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G21013": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),
    "15G22010": OS("OS X", "El Capitan", "10.11.6", "15.6.0"),

    # Sierra
    "16A323": OS("macOS", "Sierra", "10.12", "16.0.0"),
    "16B2555": OS("macOS", "Sierra", "10.12.1", "16.1.0"),
    "16B2657": OS("macOS", "Sierra", "10.12.1", "16.1.0"),
    "16C67": OS("macOS", "Sierra", "10.12.2", "16.3.0"),
    "16C68": OS("macOS", "Sierra", "10.12.2", "16.3.0"),
    "16D32": OS("macOS", "Sierra", "10.12.3", "16.4.0"),
    "16E195": OS("macOS", "Sierra", "10.12.4", "16.5.0"),
    "16F73": OS("macOS", "Sierra", "10.12.5", "16.6.0"),
    "16G29": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1036": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1114": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1212": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1314": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1408": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1510": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1618": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1710": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1815": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1917": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G1918": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G2016": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G2127": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G2128": OS("macOS", "Sierra", "10.12.6", "16.7.0"),
    "16G2136": OS("macOS", "Sierra", "10.12.6", "16.7.0"),

    # High Sierra
    "17A365": OS("macOS", "High Sierra", "10.13", "17.0.0"),
    "17A405": OS("macOS", "High Sierra", "10.13", "17.0.0"),
    "17B48": OS("macOS", "High Sierra", "10.13.1", "17.2.0"),
    "17B1002": OS("macOS", "High Sierra", "10.13.1", "17.2.0"),
    "17B1003": OS("macOS", "High Sierra", "10.13.1", "17.2.0"),
    "17C88": OS("macOS", "High Sierra", "10.13.2", "17.3.0"),
    "17C89": OS("macOS", "High Sierra", "10.13.2", "17.3.0"),
    "17C205": OS("macOS", "High Sierra", "10.13.2", "17.3.0"),
    "17C2205": OS("macOS", "High Sierra", "10.13.2", "17.3.0"),
    "17D47": OS("macOS", "High Sierra", "10.13.3", "17.4.0"),
    "17D2047": OS("macOS", "High Sierra", "10.13.3", "17.4.0"),
    "17D102": OS("macOS", "High Sierra", "10.13.3", "17.4.0"),
    "17D2102": OS("macOS", "High Sierra", "10.13.3", "17.4.0"),
    "17E199": OS("macOS", "High Sierra", "10.13.4", "17.5.0"),
    "17E202": OS("macOS", "High Sierra", "10.13.4", "17.5.0"),
    "17F77": OS("macOS", "High Sierra", "10.13.5", "17.6.0"),
    "17G65": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G2208": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G2307": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G3025": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G4015": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G5019": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G6029": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G6030": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G7024": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G8029": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G8030": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G8037": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G9016": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G10021": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G11023": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G12034": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G13033": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G13035": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G14019": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G14033": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),
    "17G14042": OS("macOS", "High Sierra", "10.13.6", "17.7.0"),

    # Mojave
    "18A391": OS("macOS", "Mojave", "10.14", "18.0.0"),
    "18B75": OS("macOS", "Mojave", "10.14.1", "18.2.0"),
    "18B2107": OS("macOS", "Mojave", "10.14.1", "18.2.0"),
    "18B3094": OS("macOS", "Mojave", "10.14.1", "18.2.0"),
    "18C54": OS("macOS", "Mojave", "10.14.2", "18.2.0"),
    "18D42": OS("macOS", "Mojave", "10.14.3", "18.2.0"),
    "18D43": OS("macOS", "Mojave", "10.14.3", "18.2.0"),
    "18D109": OS("macOS", "Mojave", "10.14.3", "18.2.0"),
    "18E226": OS("macOS", "Mojave", "10.14.4", "18.5.0"),
    "18E227": OS("macOS", "Mojave", "10.14.4", "18.5.0"),
    "18F132": OS("macOS", "Mojave", "10.14.5", "18.6.0"),
    "18G84": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G87": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G95": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G103": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G1012": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G2022": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G3020": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G4032": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G5033": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G6020": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G6032": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G7016": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G8012": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G8022": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G9028": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G9216": OS("macOS", "Mojave", "10.14.6", "18.7.0"),
    "18G9323": OS("macOS", "Mojave", "10.14.6", "18.7.0"),

    # Catalina
    "19A583": OS("macOS", "Catalina", "10.15", "19.0.0"),
    "19A602": OS("macOS", "Catalina", "10.15", "19.0.0"),
    "19A603": OS("macOS", "Catalina", "10.15", "19.0.0"),
    "19B88": OS("macOS", "Catalina", "10.15.1", "19.0.0"),
    "19C57": OS("macOS", "Catalina", "10.15.2", "19.2.0"),
    "19C58": OS("macOS", "Catalina", "10.15.2", "19.2.0"),
    "19D76": OS("macOS", "Catalina", "10.15.3", "19.3.0"),
    "19E266": OS("macOS", "Catalina", "10.15.4", "19.4.0"),
    "19E287": OS("macOS", "Catalina", "10.15.4", "19.4.0"),
    "19F96": OS("macOS", "Catalina", "10.15.5", "19.5.0"),
    "19F101": OS("macOS", "Catalina", "10.15.5", "19.5.0"),
    "19G73": OS("macOS", "Catalina", "10.15.6", "19.6.0"),
    "19G2021": OS("macOS", "Catalina", "10.15.6", "19.6.0"),
    "19H2": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H4": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H15": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H114": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H512": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H524": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1030": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1217": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1323": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1417": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1419": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1519": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1615": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1713": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1715": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1824": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H1922": OS("macOS", "Catalina", "10.15.7", "19.6.0"),
    "19H2026": OS("macOS", "Catalina", "10.15.7", "19.6.0"),

    # Big Sur
    "20A2411": OS("macOS", "Big Sur", "11.0", "20.1.0"),
    "20B29": OS("macOS", "Big Sur", "11.0.1", "20.1.0"),
    "20B50": OS("macOS", "Big Sur", "11.0.1", "20.1.0"),
    "20C69": OS("macOS", "Big Sur", "11.1", "20.2.0"),
    "20D64": OS("macOS", "Big Sur", "11.2", "20.3.0"),
    "20D74": OS("macOS", "Big Sur", "11.2.1", "20.3.0"),
    "20D75": OS("macOS", "Big Sur", "11.2.1", "20.3.0"),
    "20D80": OS("macOS", "Big Sur", "11.2.2", "20.3.0"),
    "20D91": OS("macOS", "Big Sur", "11.2.3", "20.3.0"),
    "20E232": OS("macOS", "Big Sur", "11.3", "20.4.0"),
    "20E241": OS("macOS", "Big Sur", "11.3.1", "20.4.0"),
    "20F71": OS("macOS", "Big Sur", "11.4", "20.5.0"),
    "20G71": OS("macOS", "Big Sur", "11.5", "20.6.0"),
    "20G80": OS("macOS", "Big Sur", "11.5.1", "20.6.0"),
    "20G95": OS("macOS", "Big Sur", "11.5.2", "20.6.0"),
    "20G165": OS("macOS", "Big Sur", "11.6", "20.6.0"),
    "20G224": OS("macOS", "Big Sur", "11.6.1", "20.6.0"),
    "20G314": OS("macOS", "Big Sur", "11.6.2", "20.6.0"),
    "20G415": OS("macOS", "Big Sur", "11.6.3", "20.6.0"),
    "20G417": OS("macOS", "Big Sur", "11.6.4", "20.6.0"),
    "20G527": OS("macOS", "Big Sur", "11.6.5", "20.6.0"),
    "20G624": OS("macOS", "Big Sur", "11.6.6", "20.6.0"),
    "20G630": OS("macOS", "Big Sur", "11.6.7", "20.6.0"),
    "20G730": OS("macOS", "Big Sur", "11.6.8", "20.6.0"),
    "20G817": OS("macOS", "Big Sur", "11.7", "20.6.0"),
    "20G916": OS("macOS", "Big Sur", "11.7.1 RC3", "20.6.0"),
    "20G918": OS("macOS", "Big Sur", "11.7.1", "20.6.0"),
    "20G1020": OS("macOS", "Big Sur", "11.7.2", "20.6.0"),
    "20G1116": OS("macOS", "Big Sur", "11.7.3", "20.6.0"),
    "20G1120": OS("macOS", "Big Sur", "11.7.4", "20.6.0"),
    "20G1205": OS("macOS", "Big Sur", "11.7.5 RC", "20.6.0"),
    "20G1215": OS("macOS", "Big Sur", "11.7.5 RC3", "20.6.0"),
    "20G1220": OS("macOS", "Big Sur", "11.7.5 RC4", "20.6.0"),
    "20G1225": OS("macOS", "Big Sur", "11.7.5", "20.6.0"),
    "20G1329": OS("macOS", "Big Sur", "11.7.6 RC", "20.6.0"),
    "20G1331": OS("macOS", "Big Sur", "11.7.6", "20.6.0"),
    "20G1338": OS("macOS", "Big Sur", "11.7.7 RC3", "20.6.0"),
    "20G1342": OS("macOS", "Big Sur", "11.7.7 RC4", "20.6.0"),
    "20G1345": OS("macOS", "Big Sur", "11.7.7", "20.6.0"),  # RC5 has same versions
    "20G1407": OS("macOS", "Big Sur", "11.7.8 RC2", "20.6.0"),
    "20G1413": OS("macOS", "Big Sur", "11.7.9 RC3", "20.6.0"),
    "20G1351": OS("macOS", "Big Sur", "11.7.8", "20.6.0"),  # check version
    "20G1413": OS("macOS", "Big Sur", "11.7.9 RC3", "20.6.0"),
    "20G1416": OS("macOS", "Big Sur", "11.7.9 RC4", "20.6.0"),
    "20G1424": OS("macOS", "Big Sur", "11.7.9 RC5", "20.6.0"),
    "20G1426": OS("macOS", "Big Sur", "11.7.9", "20.6.0", "xnu-7195.141.49.702.12~1", "Thu Jul  6 22:12:47 PDT 2023"),
    "20G1427": OS("macOS", "Big Sur", "11.7.10", "20.6.0", "xnu-7195.141.49.702.12~1", "Thu Jul  6 22:12:47 PDT 2023"),

    # Monterey
    "21A344": OS("macOS", "Monterey", "12.0", "21.0.1"),
    "21A559": OS("macOS", "Monterey", "21.0.1", "21.1.0"),
    "21C52": OS("macOS", "Monterey", "12.1", "21.2.0"),
    "21D49": OS("macOS", "Monterey", "12.2", "21.3.0"),
    "21D62": OS("macOS", "Monterey", "12.2.1", "21.3.0"),
    "21E230": OS("macOS", "Monterey", "12.3", "21.4.0"),
    "21E258": OS("macOS", "Monterey", "12.3.1", "21.4.0"),
    "21F79": OS("macOS", "Monterey", "12.4", "21.5.0"),
    "21F2081": OS("macOS", "Monterey", "12.4", "21.5.0"),
    "21F2092": OS("macOS", "Monterey", "12.4", "21.5.0"),
    "21G72": OS("macOS", "Monterey", "12.5", "21.6.0"),
    "21G83": OS("macOS", "Monterey", "12.5.1", "21.6.0"),
    "21G115": OS("macOS", "Monterey", "12.6", "21.6.0"),
    "21G217": OS("macOS", "Monterey", "12.6.1", "21.6.0"),
    "21G320": OS("macOS", "Monterey", "12.6.2", "21.6.0"),
    "21G419": OS("macOS", "Monterey", "12.6.3", "21.6.0"),
    "21G506": OS("macOS", "Monterey", "12.6.4 RC", "21.6.0"),
    "21G516": OS("macOS", "Monterey", "12.6.4 RC3", "21.6.0"),
    "21G521": OS("macOS", "Monterey", "12.6.4 RC4", "21.6.0"),
    "21G526": OS("macOS", "Monterey", "12.6.4", "21.6.0"),  # also RC5
    "21G630": OS("macOS", "Monterey", "12.6.5 RC", "21.6.0"),
    "21G531": OS("macOS", "Monterey", "12.6.5", "21.6.0"),
    "21G633": OS("macOS", "Monterey", "12.6.6 RC2", "21.6.0"),
    "21G639": OS("macOS", "Monterey", "12.6.6 RC3", "21.6.0"),
    "21G644": OS("macOS", "Monterey", "12.6.6 RC4", "21.6.0"),
    "21G646": OS("macOS", "Monterey", "12.6.6", "21.6.0"),
    "21G708": OS("macOS", "Monterey", "12.6.7 RC2", "21.6.0"),
    "21G713": OS("macOS", "Monterey", "12.6.8 RC3", "21.6.0"),
    "21G651": OS("macOS", "Monterey", "12.6.7", "21.6.0"),
    "21G716": OS("macOS", "Monterey", "12.6.8 RC4", "21.6.0"),
    "21G724": OS("macOS", "Monterey", "12.6.8 RC5", "21.6.0"),
    "21G725": OS("macOS", "Monterey", "12.6.8", "21.6.0"), # also RC6
    "21G726": OS("macOS", "Monterey", "12.6.9", "21.6.0"),
    "21G808": OS("macOS", "Monterey", "12.7 RC", "21.6.0"),
    "21G813": OS("macOS", "Monterey", "12.7 RC2", "21.6.0"),
    "21G814": OS("macOS", "Monterey", "12.7 RC3", "21.6.0"),
    "21G816": OS("macOS", "Monterey", "12.7", "21.6.0"),
    "21G913": OS("macOS", "Monterey", "12.7.1 RC", "21.6.0"),
    "21G918": OS("macOS", "Monterey", "12.7.1 RC2", "21.6.0"),
    "21G920": OS("macOS", "Monterey", "12.7.1", "21.6.0"),
    "21G1925": OS("macOS", "Monterey", "12.7.2 RC", "21.6.0"),
    "21G1965": OS("macOS", "Monterey", "12.7.2 RC2", "21.6.0"),
    "21G1967": OS("macOS", "Monterey", "12.7.2 RC3", "21.6.0"),
    "21G1971": OS("macOS", "Monterey", "12.7.2 RC4", "21.6.0"),
    "21G1974": OS("macOS", "Monterey", "12.7.2", "21.6.0"), # also RC5
    "21H1006": OS("macOS", "Monterey", "12.7.3 RC", "21.6.0"),
    "21H1009": OS("macOS", "Monterey", "12.7.3 RC2", "21.6.0"),
    "21H1013": OS("macOS", "Monterey", "12.7.3 RC3", "21.6.0"),
    "21H1015": OS("macOS", "Monterey", "12.7.3", "21.6.0"), # also RC4
    "21H1105": OS("macOS", "Monterey", "12.7.4 RC", "21.6.0"),
    "21H1111": OS("macOS", "Monterey", "12.7.4 RC2", "21.6.0"),

    # Ventura
    "22A380": OS("macOS", "Ventura", "13.0", "22.1.0", "xnu-8792.41.9~2", "Sun Oct 9 20:15:52 PDT 2022"),
    "22A8380": OS("macOS", "Ventura", "13.0", "22.1.0", "xnu-8792.41.9~2", "Sun Oct 9 20:15:52 PDT 2022"),
    "22A400": OS("macOS", "Ventura", "13.0.1", "22.1.0", "xnu-8792.41.9~2", "Sun Oct 9 20:15:52 PDT 2022"),
    "22C65": OS("macOS", "Ventura", "13.1", "22.2.0", "xnu-8792.61.2~4", "Fri Nov 11 02:06:26 PST 2022"),
    "22D49": OS("macOS", "Ventura", "13.2", "22.3.0", "xnu-8792.81.2~2", "Thu Jan 5 20:53:49 PST 2023"),
    "22D68": OS("macOS", "Ventura", "13.2.1", "22.3.0", "xnu-8792.81.3~2", "Mon Jan 30 20:38:43 PST 2023"),
    "22E252": OS("macOS", "Ventura", "13.3", "22.4.0", "xnu-8796.101.5~3", "Mon Mar 6 20:59:28 PST 2023"),
    "22E261": OS("macOS", "Ventura", "13.3.1", "22.4.0", "xnu-8796.101.5~3", "Mon Mar 6 20:59:28 PST 2023"),
    "22E772610a": OS("macOS", "Ventura", "13.3.1 (a)", "22.4.0", "xnu-8796.101.5~3", "Mon Mar 6 20:59:28 PST 2023"),
    "22F66": OS("macOS", "Ventura", "13.4", "22.5.0", "xnu-8796.121.2~5", "Mon Apr 24 20:52:43 PDT 2023"),
    "22F82": OS("macOS", "Ventura", "13.4.1", "22.5.0", "xnu-8796.121.3~7", "Thu Jun 8 22:22:22 PDT 2023"),
    "22F770820b": OS("macOS", "Ventura", "13.4.1 (a)", "22.5.0", "xnu-8796.121.3~7", "Thu Jun 8 22:22:22 PDT 2023"),
    "22F770820d": OS("macOS", "Ventura", "13.4.1 (c)", "22.5.0", "xnu-8796.121.3~7", "Thu Jun 8 22:22:22 PDT 2023"),
    "22G74": OS("macOS", "Ventura", "13.5", "22.6.0", "xnu-8796.141.3~6", "Wed Jul 5 22:21:56 PDT 2023"),
    "22G90": OS("macOS", "Ventura", "13.5.1", "22.6.0", "xnu-8796.141.3~6", "Wed Jul 5 22:21:56 PDT 2023"),
    "22G91": OS("macOS", "Ventura", "13.5.2", "22.6.0", "xnu-8796.141.3~6", "Wed Jul 5 22:21:56 PDT 2023"),
    "22G120": OS("macOS", "Ventura", "13.6", "22.6.0", "xnu-8796.141.3.700.8~1", "Fri Sep 15 13:39:52 PDT 2023"),
    "22G313":  OS("macOS", "Ventura", "13.6.1", "22.6.0", "xnu-8796.141.3.701.17~4", "Wed Oct 4 21:25:26 PDT 2023"),
    "22G320":  OS("macOS", "Ventura", "13.6.2", "22.6.0", "xnu-8796.141.3.701.17~6", "Thu Nov 2 07:43:57 PDT 2023"),
    "22G436":  OS("macOS", "Ventura", "13.6.3", "22.6.0", "xnu-8796.141.3.702.9~2", "Tue Nov 7 21:48:06 PST 2023"),
    "22G513":  OS("macOS", "Ventura", "13.6.4", "22.6.0", "xnu-8796.141.3.703.2~2", "Sun Dec 17 22:18:09 PST 2023"),

    # Sonoma
    "23A5257q": OS("macOS", "Sonoma", "14.0 B1", "23.0.0"),
    "23A5276g": OS("macOS", "Sonoma", "14.0 B2", "23.0.0"),
    "23A5286g": OS("macOS", "Sonoma", "14.0 B3", "23.0.0"),
    "23A5286i": OS("macOS", "Sonoma", "14.0 B3", "23.0.0"),
    "23A5301g": OS("macOS", "Sonoma", "14.0 B4", "23.0.0"),
    "23A5301h": OS("macOS", "Sonoma", "14.0 B4", "23.0.0"),
    "23A5312d": OS("macOS", "Sonoma", "14.0 B5", "23.0.0"),
    "23A5328b": OS("macOS", "Sonoma", "14.0 B6", "23.0.0"),
    "23A5337a": OS("macOS", "Sonoma", "14.0 B7", "23.0.0"),
    "23A339":   OS("macOS", "Sonoma", "14.0 RC", "23.0.0"),
    "23A344":   OS("macOS", "Sonoma", "14.0 RC2", "23.0.0"),
    "23A344":   OS("macOS", "Sonoma", "14.0",     "23.0.0", "xnu-10002.1.13~1", "Fri Sep 15 14:41:34 PDT 2023"),
    "23B74":    OS("macOS", "Sonoma", "14.1",     "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:27:27 PDT 2023"),
    "23B81":    OS("macOS", "Sonoma", "14.1.1",   "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:26:29 PDT 2023"),
    "23B2082":  OS("macOS", "Sonoma", "14.1.1",   "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:26:29 PDT 2023"),
    "23B92":    OS("macOS", "Sonoma", "14.1.2",   "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:27:27 PDT 2023"),
    "23B2091":  OS("macOS", "Sonoma", "14.1.2",   "23.1.0", "xnu-10002.41.9~6", "Mon Oct 9 21:27:27 PDT 2023"),
    "23C64":    OS("macOS", "Sonoma", "14.2",     "23.2.0", "xnu-10002.61.3~2", "Wed Nov 15 21:54:10 PST 2023"),
    "23C71":    OS("macOS", "Sonoma", "14.2.1",   "23.2.0", "xnu-10002.61.3~2", "Wed Nov 15 21:54:10 PST 2023"),
    "23D56":    OS("macOS", "Sonoma", "14.3",     "23.3.0", "xnu-10002.81.5~7", "Wed Dec 20 21:30:27 PST 2023"),
    "23D60":    OS("macOS", "Sonoma", "14.3.1",   "23.3.0", "xnu-10002.81.5~7", "Wed Dec 20 21:28:58 PST 2023"),
}


def _read_sw_vers():
    info = {}

    p = os.popen("sw_vers")
    lines = p.readlines()
    p.close()

    for line in lines:
        bits = line.strip().split()
        info[bits[0][:-1]] = bits[1]

    return info


VERSION_INFO = _read_sw_vers()


def getMacOSRelease(darwin_version: str = None) -> (str, str):
    """(Deprecated) Return tuple of product name and version string.

    :param darwin_version: optional Darwin kernel version to get earliest release with that kernel
    :returns: product name, product version string"""

    if not darwin_version:
        return (VERSION_INFO["ProductName"], VERSION_INFO["ProductVersion"])

    # FIXME: look up Darwin version and return the ... earliest (?) ... version supported.
    return ("", "")


def get_macos_product_name() -> str:
    return VERSION_INFO["ProductName"]

def get_macos_version() -> str:
    return VERSION_INFO["ProductVersion"]

def get_macos_build() -> str:
    return VERSION_INFO["BuildVersion"]

def get_macos_darwin_version() -> str:
    return os.uname().release

def get_macos_full_name(build: str = None) -> str:
    if build is None:
        build = get_macos_build()

    vi = BUILDS.get(build)
    if vi is None:
        raise NameError(f"Unknown build '{build}'")

    return f"{vi.product} {vi.version} {vi.name} (darwin {vi.darwin}, build {build})"


if __name__ == "__main__":
    print(get_macos_full_name())
