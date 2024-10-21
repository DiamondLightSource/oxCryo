TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

LIBRARY_IOC += OXCryo

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxx.h

# xxxRecord.dbd will be installed into <top>/dbd
DBD += OXCryovdct.dbd
DBD += OXCryoSupport.dbd

OXCryovdct_DBD += base.dbd
OXCryovdct_DBD += stream.dbd
OXCryovdct_DBD += asyn.dbd
OXCryovdct_DBD += calcSupport.dbd
OXCryovdct_DBD += genSubRecord.dbd
OXCryovdct_DBD += alarmlookup.dbd

OXCryoSupport_DBD += alarmlookup.dbd

# The following are compiled and added to the support library
OXCryo_SRCS += alarmlookup.c

# We need to link against the EPICS Base libraries
#xxx_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
