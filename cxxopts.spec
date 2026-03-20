Summary:	Lightweight C++ command line option parser
Name:		cxxopts
Version:	3.3.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/jarro2783/cxxopts/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	47dcaab8ea57feed39d79abad56a3ae9
URL:		https://github.com/jarro2783/cxxopts
BuildRequires:	cmake >= 3.5
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight C++ command line option parser.

%package devel
Summary:	Development files for cxxopts
Group:		Development/Libraries
BuildArch:	noarch

%description devel
This package contains the header files for developing applications
that use cxxopts.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
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
