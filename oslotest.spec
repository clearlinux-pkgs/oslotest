#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : oslotest
Version  : 2.11.0
Release  : 41
URL      : http://tarballs.openstack.org/oslotest/oslotest-2.11.0.tar.gz
Source0  : http://tarballs.openstack.org/oslotest/oslotest-2.11.0.tar.gz
Source99 : http://tarballs.openstack.org/oslotest/oslotest-2.11.0.tar.gz.asc
Summary  : Oslo test framework
Group    : Development/Tools
License  : Apache-2.0
Requires: oslotest-bin
Requires: oslotest-python
Requires: debtcollector
Requires: fixtures
Requires: mock
Requires: mox3
Requires: os-client-config
Requires: python-mock
Requires: python-subunit
Requires: six
Requires: testrepository
Requires: testtools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======================================================
oslotest -- OpenStack Testing Framework and Utilities
=======================================================

%package bin
Summary: bin components for the oslotest package.
Group: Binaries

%description bin
bin components for the oslotest package.


%package python
Summary: python components for the oslotest package.
Group: Default

%description python
python components for the oslotest package.


%prep
%setup -q -n oslotest-2.11.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489273022
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489273022
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo_debug_helper
/usr/bin/oslo_run_cross_tests
/usr/bin/oslo_run_pre_release_tests

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
