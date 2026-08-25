TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

LIBRARY_IOC += oxCryo

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxx.h

# xxxRecord.dbd will be installed into <top>/dbd
# DBD += oxCryovdct.dbd
DBD += oxCryo.dbd

oxCryo_DBD += base.dbd
oxCryo_DBD += stream.dbd
oxCryo_DBD += asyn.dbd
oxCryo_DBD += calcSupport.dbd
oxCryo_DBD += alarmlookup.dbd

# The following are compiled and added to the support library
oxCryo_SRCS += alarmlookup.c

# We need to link against the EPICS Base libraries
#xxx_LIBS += $(EPICS_BASE_IOC_LIBS)

# do debug build
# CXXFLAGS= -g -O0 -fPIC
USR_CFLAGS += -DUSE_TYPED_RSET

# Enable wonderful C++ 11 features
USR_CXXFLAGS_Linux += -std=c++11

include $(TOP)/configure/RULES
