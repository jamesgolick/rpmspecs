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
Requires(pre): shadow-utils

%description
Graphite's metric collector.

%pre
getent group graphite > /dev/null || groupadd -r graphite
getent passwd graphite > /dev/null || \
  useradd -r -g graphite -d /opt/graphite -s /sbin/nologin \
  -c "User for graphite/carbon/whisper." graphite
exit 0

%prep
%setup -q

%install
python setup.py install --root $RPM_BUILD_ROOT

%files
%defattr(-,graphite,graphite)
/opt/graphite/*
