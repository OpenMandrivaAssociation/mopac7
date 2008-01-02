%define	name	mopac7
%define	version	1.11
%define	release	%mkrel 2

%define	major	0
%define	libname	%mklibname %{name}_ %major

Name:		%{name}
Summary:	Semi-empirical quantum mechanics suite
Version:	%{version}
Release:	%{release}

Source0:	http://surfnet.dl.sourceforge.net/sourceforge/mopac7/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/mopac7/
License:	Public Domain
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	f2c

%description
MOPAC7 is a semi-empirical quantum-mechanics code written by James J. P.
Stewart and co-workers. The purpose of this project is to maintain MOPAC7 as
a stand-alone program as well as a library that provides the functionality
of MOPAC7 to other programs.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{libname}-devel
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%{name}-devel

%description -n	%{libname}-devel
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
perl -pi -e "s#-lg2c##g" libmopac7.pc.in

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall
install -m755 src/%{name} -D %{buildroot}%{_bindir}/%{name}
sed "s/\.\/src/\/usr\/bin/" run_mopac7 > %{buildroot}%{_bindir}/run_mopac7
chmod 755 %{buildroot}%{_bindir}/run_mopac7

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc tests
%{_bindir}/%{name}
%{_bindir}/run_mopac7

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

