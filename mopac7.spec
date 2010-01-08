Name:			mopac7
Version:		1.15
Release:		%mkrel 1

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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall
install -m755 fortran/%{name} -D %{buildroot}%{_bindir}/%{name}
sed "s/\.\/src/\/usr\/bin/" run_mopac7 > %{buildroot}%{_bindir}/run_mopac7
chmod 755 %{buildroot}%{_bindir}/run_mopac7

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
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
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
