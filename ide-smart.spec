%define name ide-smart
%define version 1.4
%define release  %mkrel 5

Summary: A system utility for monitoring a SMART capable hard-disk
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Patch0: ide-smart-1.4-typofix.patch.bz2
License: GPL
Url: http://lightside.eresmas.com/
Group: Monitoring
Buildroot: %{_tmppath}/%{name}-buildroot

%description
The ide-smart program enable to monitor a SMART capable hard-disk.
The SMART protocol define several items. When one of these items is under
a certain level, this means that the disk is about to break.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p1

%build
make clean
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
perl -pi -e "s!/man/!/share/man/!g" Makefile
%makeinstall INSTALL_PREFIX=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_sbindir}/*
%{_mandir}/man8/*

