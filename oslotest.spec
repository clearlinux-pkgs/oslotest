#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslotest
Version  : 3.7.0
Release  : 48
URL      : http://tarballs.openstack.org/oslotest/oslotest-3.7.0.tar.gz
Source0  : http://tarballs.openstack.org/oslotest/oslotest-3.7.0.tar.gz
Source99 : http://tarballs.openstack.org/oslotest/oslotest-3.7.0.tar.gz.asc
Summary  : Oslo test framework
Group    : Development/Tools
License  : Apache-2.0
Requires: oslotest-bin
Requires: oslotest-python3
Requires: oslotest-license
Requires: oslotest-python
Requires: debtcollector
Requires: fixtures
Requires: mox3
Requires: os-client-config
Requires: python-mock
Requires: python-subunit
Requires: six
Requires: stestr
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the oslotest package.
Group: Binaries
Requires: oslotest-license = %{version}-%{release}

%description bin
bin components for the oslotest package.


%package license
Summary: license components for the oslotest package.
Group: Default

%description license
license components for the oslotest package.


%package python
Summary: python components for the oslotest package.
Group: Default
Requires: oslotest-python3 = %{version}-%{release}

%description python
python components for the oslotest package.


%package python3
Summary: python3 components for the oslotest package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslotest package.


%prep
%setup -q -n oslotest-3.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538578535
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/oslotest
cp LICENSE %{buildroot}/usr/share/doc/oslotest/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo_debug_helper
/usr/bin/oslo_run_cross_tests
/usr/bin/oslo_run_pre_release_tests

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/oslotest/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
