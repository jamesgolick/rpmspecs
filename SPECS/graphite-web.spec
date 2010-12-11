Summary: Graphite Web Interface
Name: graphite-web
Version: 0.9.6
Release: fetlife1
Source0: graphite-web-0.9.6.tar.gz
License: GPL
Group: Monitoring
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires(pre): shadow-utils
requires: python pycairo python-ldap python-django python-simplejson mod_python python-memcached python-sqlite2 rrdtool-python

%description
Graphite web interface.

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
