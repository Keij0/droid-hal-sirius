# These and other macros are documented in dhd/droid-hal-device.inc

%define device z3c
%define vendor sony

%define vendor_pretty Sony
%define device_pretty Xperia Z3 Compact

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-z3c.spec
%define android_config \
#define QCOM_BSP 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc
