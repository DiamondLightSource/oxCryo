TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

LIBRARY_IOC += oxCryo

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxx.h

# xxx.dbd will be installed into <top>/dbd
##DBD += xxx.dbd
##xxx_DBD += base.dbd

# The following are compiled and added to the support library
#xxx_SRCS += xxxCodeA.c
#xxx_SRCS += xxxCodeB.c

# We need to link against the EPICS Base libraries
##oxCryo_LIBS += $(EPICS_BASE_IOC_LIBS)

# ------------------------
# Build an IOC Application
# ------------------------

##PROD_IOC = oxCryo

# xxx.h will be created from xxx.dbd
#DBDINC += xxx.h

# xxx.dbd will be installed into <top>/dbd
DBD += oxCryo.dbd
DBD += oxCryoSupport.dbd

# oxCryo.dbd will be created from these files
oxCryo_DBD += base.dbd
oxCryo_DBD += calcSupport.dbd
oxCryo_DBD += stream.dbd
oxCryo_DBD += asyn.dbd

# oxCryoSupport.dbd will be created from these files
oxCryoSupport_DBD += alarmlookup.dbd

# The following are compiled and added to the support library
oxCryoSupport_SRCS += alarmlookup.c

# These two lines are needed for non-vxWorks builds, such as Linux
oxCryo_SRCS_DEFAULT += oxCryoMain.cpp
oxCryo_SRCS_vxWorks += -nil-

# Add locally compiled object code
#oxCryo_SRCS +=

# We need to link against the EPICS Base libraries
oxCryo_LIBS += $(EPICS_BASE_IOC_LIBS)

# This line says that this IOC Application depends on the
# xxx Support Module
#oxCryo_LIBS += xxx

# do debug build
# CXXFLAGS= -g -O0 -fPIC
USR_CFLAGS += -DUSE_TYPED_RSET

# Enable wonderful C++ 11 features
USR_CXXFLAGS_Linux += -std=c++11

include $(TOP)/configure/RULES
