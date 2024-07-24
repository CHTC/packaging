Name:           duo_unix
Version:        2.0.3
Release:        1%{?dist}
Summary:        Login utility and PAM module for Duo Security two-factor authentication
License:        GPLv2
URL:            https://www.duosecurity.com/docs/duounix
Source0:        https://dl.duosecurity.com/duo_unix-%{version}.tar.gz

BuildRequires:  pam-devel
BuildRequires:  openssl-devel
Requires:       pam

%description
Duo Unix provides two-factor authentication support for SSH and other
applications via a PAM module or a stand-alone login utility.

%prep
%setup -q

%build
# By default, login_duo is installed setuid root with system-wide config files
# Using nobody as the privsep user to match the default openssh package
# More config options here: https://github.com/duosecurity/duo_unix
%configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir}/duo \
    --sbindir=%{_bindir} \
    --datarootdir=%{_datadir} \
    --mandir=%{_mandir} \
    --with-pam=%{_libdir}/security \
    --with-privsep-user=nobody


make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS
%doc CHANGES
%doc CONTRIBUTING.md
%doc README.md
%doc sbom.spdx
%{_docdir}/%{name}/duo_unix_support/README.md

%{_bindir}/login_duo
%{_bindir}/duo_unix_support.sh

%{_libdir}/pkgconfig/libduo.pc
%{_libdir}/security/pam_duo.la
%{_libdir}/security/pam_duo.so

%config(noreplace) %{_sysconfdir}/duo/login_duo.conf
%config(noreplace) %{_sysconfdir}/duo/pam_duo.conf

%{_includedir}/common_ini_test.h
%{_includedir}/duo.h
%{_includedir}/duo_private.h
%{_includedir}/shell.h
%{_includedir}/unity.h
%{_includedir}/util.h

%{_datadir}/LICENSES/Apache-2.0.txt
%{_datadir}/LICENSES/BSD-2-Clause.txt
%{_datadir}/LICENSES/BSD-3-Clause.txt
%{_datadir}/LICENSES/BSD-4-Clause.txt
%{_datadir}/LICENSES/FSFAP.txt
%{_datadir}/LICENSES/FSFULLR.txt
%{_datadir}/LICENSES/GPL-1.0-only.txt
%{_datadir}/LICENSES/GPL-2.0-with-classpath-exception.txt
%{_datadir}/LICENSES/LicenseRef-URLEnc-MIT.txt
%{_datadir}/LICENSES/MIT.txt
%{_datadir}/LICENSES/SSH-short.txt

%{_mandir}/man3/duo.3.gz
%{_mandir}/man8/login_duo.8.gz
%{_mandir}/man8/pam_duo.8.gz

%changelog
* Fri Jul 05 2024 Bocheng Zou <bocheng.zou@outlook.com> - 2.0.3-1
- Initial package