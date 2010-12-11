Summary: Carbon
Name: carbon
Version: 0.9.6
Source0: carbon-0.9.6.tar.gz
Release: fetlife1
License: GPL
Group: Monitoring
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
requires: python python-twisted

%description
Graphite's metric collector.

%prep
%setup -q

%install
python setup.py install --root $RPM_BUILD_ROOT

%files
/opt/graphite/*
