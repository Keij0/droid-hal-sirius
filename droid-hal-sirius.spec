# These and other macros are documented in dhd/droid-hal-device.inc

%define device sirius
%define vendor sony

%define vendor_pretty Sony
%define device_pretty Xperia Z2

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-sirius.spec
%define android_config \
#define QCOM_BSP 1\
%{nil}

# Remove /tmp from the makefstab entries
# moved from droid-hal-device.inc
%define makefstab_skip_entries /tmp

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

# Add users to inet group (fix internet access issue)
%define additional_post_scripts \
/usr/bin/groupadd-user inet || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
