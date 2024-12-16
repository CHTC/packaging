%define         _disable_ld_no_undefined 0
%define         srcname                  pmix

%define         major                    2

%define         libname                  openpmix-lib
%define         develname                openpmix-dev


Summary:        A highly configurable open-source workload manager
Name:           openpmix
Version:        5.0.2
Release:        1%{?dist}
License:        MIT
Group:          System/Cluster

Url:            https://pmix.org/

Source0:        https://github.com/openpmix/openpmix/releases/download/v%{version}/pmix-%{version}.tar.bz2


BuildRequires:  pkg-config
BuildRequires:  autoconf
BuildRequires:  perl
BuildRequires:  man2html
BuildRequires:  hwloc
BuildRequires:  flex
BuildRequires:  pkgconfig(libevent)
BuildRequires:  libev-devel
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pkgconfig(zlib)

# 32 bits support dropped since 4.2.* version (that will
#propagate soon to OpenMPI...)
ExcludeArch: 	%{ix86}
ExcludeArch:    %{arm32}

%description
The Process Management Interface (PMI) has been used for quite some
time as a means of exchanging wireup information needed for
interprocess communication. Two versions (PMI-1 and PMI-2) have been
released as part of the MPICH effort. While PMI-2 demonstrates better
scaling properties than its PMI-1 predecessor, attaining rapid launch
and wireup of the roughly 1M processes executing across 100k nodes
expected for exascale operations remains challenging.

PMI Exascale (PMIx) represents an attempt to resolve these questions
by providing an extended version of the PMI standard specifically
designed to support clusters up to and including exascale sizes. The
overall objective of the project is not to branch the existing
pseudo-standard definitions - in fact, PMIx fully supports both of the
existing PMI-1 and PMI-2 APIs - but rather to (a) augment and extend
those APIs to eliminate some current restrictions that impact
scalability, and (b) provide a reference implementation of the
PMI-server that demonstrates the desired level of scalability.

%package -n %{libname}
Summary:        Shared libraries for OpenPMIx
Group:          Development/Other
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
%{summary}.



%package -n %{develname}
Summary:        Development files for OpenPMIx
Group:          Development/Other
Requires:       %{libname} = %{version}-%{release}
Provides:       lib%{name}-devel  = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
%{summary}.






%prep

%setup -q -n %{srcname}-%{version}

%build
%configure --with-devel-headers

%make_build

%install
%make_install

find %{buildroot}%{_libdir} -name '*.la' -delete



%files
%doc AUTHORS README.md VERSION LICENSE
%config(noreplace)%{_sysconfdir}/pmix-mca-params.conf
%{_bindir}/*
%{_datadir}/pmix
%{_datadir}/doc/pmix
%{_mandir}/man1/*.1.*
%{_mandir}/man5/*.5.*


%files -n %{libname}
%{_libdir}/libpmix.so.%{major}{,.*}
#these guys are modules, not devel files
%{_libdir}/pmix/*.so
%{_mandir}/man3/*.3.*



%files -n %{develname}
%{_includedir}/pmi*.h
%{_includedir}/pmix
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


