from genSub import GenSub
from iocbuilder import AutoSubstitution, Device
from iocbuilder.modules.calc import Calc
from iocbuilder.modules.streamDevice import AutoProtocol


class OXCryoLib(Device):
    LibFileList = ["OXCryo"]
    DbdFileList = ["OXCryoSupport"]
    AutoInstantiate = True


class OXPH700(AutoSubstitution, AutoProtocol, Device):
    Dependencies = (GenSub, OXCryoLib, Calc)
    # Substitution attributes
    TemplateFile = "OXPH700.template"

    # AutoProtocol attributes
    ProtocolFiles = ["OXcommon.proto", "OXCS700.proto"]


class OXCS700(AutoSubstitution, AutoProtocol, Device):
    Dependencies = (GenSub, OXCryoLib, Calc)
    # Substitution attributes
    TemplateFile = "OXCS700.template"

    # AutoProtocol attributes
    ProtocolFiles = ["OXcommon.proto", "OXCS700.proto"]


class OXCB700(AutoSubstitution, AutoProtocol, Device):
    Dependencies = (GenSub, OXCryoLib, Calc)
    # Substitution attributes
    TemplateFile = "OXCB700.template"

    # AutoProtocol attributes
    ProtocolFiles = ["OXcommon.proto", "OXCB700.proto"]


class OXNH700(AutoSubstitution, AutoProtocol, Device):
    Dependencies = (GenSub, OXCryoLib, Calc)
    # Substitution attributes
    TemplateFile = "OXNH700.template"

    # AutoProtocol attributes
    ProtocolFiles = ["OXcommon.proto", "OXNH700.proto"]


class OXCB800(AutoSubstitution, AutoProtocol, Device):
    Dependencies = (GenSub, OXCryoLib, Calc)
    # Substitution attributes
    TemplateFile = "OXCB800.template"

    # AutoProtocol attributes
    ProtocolFiles = ["OXcommon.proto", "OXCB800.proto"]
