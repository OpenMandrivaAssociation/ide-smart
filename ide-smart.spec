%define name ide-smart
%define version 1.4
%define release  %mkrel 9

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-9mdv2011.0
+ Revision: 619601
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-8mdv2010.0
+ Revision: 429497
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4-7mdv2009.0
+ Revision: 247204
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2008.1
+ Revision: 126988
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import ide-smart


* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 1.4-5mdk
- rebuild

* Fri Feb 20 2004  Lenny Cartier <lenny@mandrakesoft.com> 1.4-4mdk
- rebuild

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.4-3mdk
- rebuild

* Tue Apr 16 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.4-2mdk
- fix typo in man page

* Mon Nov 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4
- url 

* Wed Aug 01 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.3-5mdk
- rebuild

* Fri Jan 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.3-4mdk
- rebuild

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-3mdk
- BM

* Fri Apr 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.3-2mdk
- fix group

* Fri Oct 1 1999 Thierry Vignaud <tvignaud@linux-mandrake.com>
- initial rpm

