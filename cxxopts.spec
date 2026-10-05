Summary:	Lightweight C++ command line option parser
Summary(pl.UTF-8):	Lekki parser opcji linii poleceń dla C++
Name:		cxxopts
Version:	3.3.1
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/jarro2783/cxxopts/releases
Source0:	https://github.com/jarro2783/cxxopts/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	47dcaab8ea57feed39d79abad56a3ae9
URL:		https://github.com/jarro2783/cxxopts
BuildRequires:	cmake >= 3.5
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	rpmbuild(macros) >= 1.605
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight C++ command line option parser.

%description -l pl.UTF-8
Lekki parser opcji linii poleceń dla C++.

%package devel
Summary:	Lightweight C++ command line option parser
Summary(pl.UTF-8):	Lekki parser opcji linii poleceń dla C++
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.8.1

%description devel
Lightweight C++ command line option parser.

This package contains the header files for developing applications
that use cxxopts.

%description devel -l pl.UTF-8
Lekki parser opcji linii poleceń dla C++.

Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących cxxopts.

%prep
%setup -q

%build
install -d build
cd build
# .pc file generation expects relative CMAKE_INSTALL_INCLUDEDIR
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{_includedir}/cxxopts.hpp
%{_datadir}/cmake/cxxopts
%{_npkgconfigdir}/cxxopts.pc
