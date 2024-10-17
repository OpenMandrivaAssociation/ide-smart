Summary:	A system utility for monitoring a SMART capable hard-disk
Name:		ide-smart
Version:	1.4
Release:	11
License:	GPLv2+
Group:		Monitoring
Url:		https://lightside.eresmas.com/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		ide-smart-1.4-typofix.patch.bz2
Patch1:		ide-smart-1.4-no-strip.patch

%description
The ide-smart program enable to monitor a SMART capable hard-disk.
The SMART protocol define several items. When one of these items is under
a certain level, this means that the disk is about to break.

%files
%{_sbindir}/*
%{_mandir}/man8/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make clean
make CFLAGS="%{optflags}"

%install
perl -pi -e "s!/man/!/share/man/!g" Makefile
%makeinstall INSTALL_PREFIX=%{buildroot}%{_prefix}


