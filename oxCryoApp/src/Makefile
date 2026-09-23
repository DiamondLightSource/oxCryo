TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

LIBRARY_IOC += oxCryo

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxx.h

# no longer using VDCT
# DBD += oxCryovdct.dbd

DBD += oxCryoSupport.dbd

# no longer using VDCT
# oxCryovdct_DBD += base.dbd
# oxCryovdct_DBD += calcSupport.dbd
# oxCryovdct_DBD += stream.dbd
# oxCryovdct_DBD += asyn.dbd
# oxCryovdct_DBD += alarmlookup.dbd

oxCryoSupport_DBD += alarmlookup.dbd

# The following are compiled and added to the support library
oxCryo_SRCS += alarmlookup.c

# We need to link against the EPICS Base libraries
#xxx_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES