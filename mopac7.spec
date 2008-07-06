%define	name	mopac7
%define	version	1.13
%define	release	%mkrel 1

%define	major	0
%define	libname	%mklibname %{name}_ %major
%define develname %mklibname %{name} -d
%define olddevelname %mklibname %{name}_ %major -d

Name:		%{name}
Summary:	Semi-empirical quantum mechanics suite
Version:	%{version}
Release:	%{release}

Source0:	http://www.uku.fi/~thassine/projects/download/current/%{name}-%{version}.tar.gz
Patch0:		mopac7-no_bundled_libtool.diff
Patch1:		01_undefined_symbol_in_so.patch
Patch2:		03_fix_FORTRAN_source.patch
URL:		http://sourceforge.net/projects/mopac7/
License:	Public Domain
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	f2c
BuildRequires:	libtool

%description
MOPAC7 is a semi-empirical quantum-mechanics code written by James J. P.
Stewart and co-workers. The purpose of this project is to maintain MOPAC7 as
a stand-alone program as well as a library that provides the functionality
of MOPAC7 to other programs.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides: 	%{name} = %{version}-%{release}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%{name}-devel
Obsoletes:	%{olddevelname}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
rm -f configure
libtoolize --copy --force; aclocal; autoconf
%configure2_5x
%make -j1
										
%install
rm -rf %{buildroot}
%makeinstall
install -m755 src/%{name} -D %{buildroot}%{_bindir}/%{name}
sed "s/\.\/src/\/usr\/bin/" run_mopac7 > %{buildroot}%{_bindir}/run_mopac7
chmod 755 %{buildroot}%{_bindir}/run_mopac7

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc tests
%{_bindir}/%{name}
%{_bindir}/run_mopac7

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
