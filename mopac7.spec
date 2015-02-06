Name:			mopac7
Version:		1.15
Release:		4

%define	major		1
%define	libname		%mklibname %{name}_ %major
%define develname	%mklibname %{name} -d
%define olddevelname	%mklibname %{name}_ 0 -d

Summary:	Semi-empirical quantum mechanics suite
License:	Public Domain
Group:		Sciences/Chemistry
URL:		http://www.uku.fi/~thassine/projects/ghemical
Source0:	http://www.uku.fi/~thassine/projects/download/current/%{name}-%{version}.tar.gz

BuildRequires:	f2c
BuildRequires:	libtool
BuildRequires:	gcc-gfortran

%description
MOPAC7 is a semi-empirical quantum-mechanics code written by James J. P.
Stewart and co-workers. The purpose of this project is to maintain MOPAC7 as
a stand-alone program as well as a library that provides the functionality
of MOPAC7 to other programs.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides: 	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}%{name}_0

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%{olddevelname}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
#rm -f configure
#libtoolize --copy --force; aclocal; autoconf
%configure2_5x
%make
										
%install
%makeinstall
install -m755 fortran/%{name} -D %{buildroot}%{_bindir}/%{name}
sed "s/\.\/src/\/usr\/bin/" run_mopac7 > %{buildroot}%{_bindir}/run_mopac7
chmod 755 %{buildroot}%{_bindir}/run_mopac7

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc tests
%{_bindir}/%{name}
%{_bindir}/run_mopac7

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.15-2mdv2011.0
+ Revision: 612930
- the mass rebuild of 2010.1 packages

* Fri Jan 08 2010 Emmanuel Andry <eandry@mandriva.org> 1.15-1mdv2010.1
+ Revision: 487766
- New version 1.15
- check major
- fix major
- obsolete wrong major lib package

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.14-2mdv2010.0
+ Revision: 440107
- rebuild

* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 1.14-1mdv2009.1
+ Revision: 328758
- Fix buildrequires
- Fix install
- Dropped outdated and already included patches
- Release 1.14

* Sun Jul 06 2008 Funda Wang <fwang@mandriva.org> 1.13-1mdv2009.0
+ Revision: 232072
- add ubuntu patches to make it build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Mar 06 2008 Guillaume Bedot <littletux@mandriva.org> 1.13-1mdv2008.1
+ Revision: 180322
- library policy

  + Oden Eriksson <oeriksson@mandriva.com>
    - added P0 to try and fix the build...

  + Austin Acton <austin@mandriva.org>
    - new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import mopac7


* Tue Aug 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.11-2mdv2007.0
- remove -lg2c from pkgconfig file

* Tue Aug 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.11-1mdv2007.0
- 1.11
- %%mkrel
- fix mixed-use-of-spaces-and-tabs

* Sun Dec 04 2005 Austin Acton <austin@mandriva.org> 1.10-1mdk
- New release 1.10

* Fri Aug 12 2005 Austin Acton <austin@mandrake.org> 1.00-1mdk
- initial package

