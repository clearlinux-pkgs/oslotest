#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslotest
Version  : 2.8.0
Release  : 31
URL      : http://tarballs.openstack.org/oslotest/oslotest-2.8.0.tar.gz
Source0  : http://tarballs.openstack.org/oslotest/oslotest-2.8.0.tar.gz
Summary  : Oslo test framework
Group    : Development/Tools
License  : Apache-2.0
Requires: oslotest-bin
Requires: oslotest-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : netaddr-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pycodestyle-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

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
Requires: fixtures-python
Requires: mox3-python
Requires: six-python
Requires: testrepository-python
Requires: testscenarios
Requires: testtools-python

%description python
python components for the oslotest package.


%prep
%setup -q -n oslotest-2.8.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

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
