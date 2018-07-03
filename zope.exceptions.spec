#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.exceptions
Version  : 4.2.0
Release  : 15
URL      : http://pypi.debian.net/zope.exceptions/zope.exceptions-4.2.0.tar.gz
Source0  : http://pypi.debian.net/zope.exceptions/zope.exceptions-4.2.0.tar.gz
Summary  : Zope Exceptions
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.exceptions-python3
Requires: zope.exceptions-license
Requires: zope.exceptions-python
Requires: Sphinx
Requires: setuptools
Requires: zope.interface
Requires: zope.testrunner
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.interface

%description
zope.exceptions
        =================

%package license
Summary: license components for the zope.exceptions package.
Group: Default

%description license
license components for the zope.exceptions package.


%package python
Summary: python components for the zope.exceptions package.
Group: Default
Requires: zope.exceptions-python3

%description python
python components for the zope.exceptions package.


%package python3
Summary: python3 components for the zope.exceptions package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.exceptions package.


%prep
%setup -q -n zope.exceptions-4.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530331732
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/zope.exceptions
cp LICENSE.txt %{buildroot}/usr/share/doc/zope.exceptions/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/zope.exceptions/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
