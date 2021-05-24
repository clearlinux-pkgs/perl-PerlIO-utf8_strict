#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PerlIO-utf8_strict
Version  : 0.008
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/PerlIO-utf8_strict-0.008.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/PerlIO-utf8_strict-0.008.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperlio-utf8-strict-perl/libperlio-utf8-strict-perl_0.007-2.debian.tar.xz
Summary  : 'Fast and correct UTF-8 IO'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PerlIO-utf8_strict-license = %{version}-%{release}
Requires: perl-PerlIO-utf8_strict-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
This archive contains the distribution PerlIO-utf8_strict,
version 0.008:
Fast and correct UTF-8 IO

%package dev
Summary: dev components for the perl-PerlIO-utf8_strict package.
Group: Development
Provides: perl-PerlIO-utf8_strict-devel = %{version}-%{release}
Requires: perl-PerlIO-utf8_strict = %{version}-%{release}

%description dev
dev components for the perl-PerlIO-utf8_strict package.


%package license
Summary: license components for the perl-PerlIO-utf8_strict package.
Group: Default

%description license
license components for the perl-PerlIO-utf8_strict package.


%package perl
Summary: perl components for the perl-PerlIO-utf8_strict package.
Group: Default
Requires: perl-PerlIO-utf8_strict = %{version}-%{release}

%description perl
perl components for the perl-PerlIO-utf8_strict package.


%prep
%setup -q -n PerlIO-utf8_strict-0.008
cd %{_builddir}
tar xf %{_sourcedir}/libperlio-utf8-strict-perl_0.007-2.debian.tar.xz
cd %{_builddir}/PerlIO-utf8_strict-0.008
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/PerlIO-utf8_strict-0.008/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PerlIO-utf8_strict
cp %{_builddir}/PerlIO-utf8_strict-0.008/LICENSE %{buildroot}/usr/share/package-licenses/perl-PerlIO-utf8_strict/fa89be48cbebd856e7cb66d4c21f0b6f4ea67aee
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PerlIO::utf8_strict.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PerlIO-utf8_strict/fa89be48cbebd856e7cb66d4c21f0b6f4ea67aee

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/PerlIO/utf8_strict.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/PerlIO/utf8_strict/utf8_strict.so
