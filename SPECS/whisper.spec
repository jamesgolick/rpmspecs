Summary: Whisper
Name: whisper
Version: 0.9.6
Release: fetlife1
Source0: whisper-0.9.6.tar.gz
License: GPL
Group: Monitoring
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
requires: python

%prep
%setup -q

%description
Whisper metrics database.

%install
python setup.py install --root $RPM_BUILD_ROOT

%files
/usr/bin/rrd2whisper.py
/usr/bin/rrd2whisper.pyc
/usr/bin/rrd2whisper.pyo
/usr/bin/whisper-create.py
/usr/bin/whisper-create.pyc
/usr/bin/whisper-create.pyo
/usr/bin/whisper-fetch.py
/usr/bin/whisper-fetch.pyc
/usr/bin/whisper-fetch.pyo
/usr/bin/whisper-info.py
/usr/bin/whisper-info.pyc
/usr/bin/whisper-info.pyo
/usr/bin/whisper-resize.py
/usr/bin/whisper-resize.pyc
/usr/bin/whisper-resize.pyo
/usr/bin/whisper-update.py
/usr/bin/whisper-update.pyc
/usr/bin/whisper-update.pyo
/usr/lib/python2.4/site-packages/whisper.py
/usr/lib/python2.4/site-packages/whisper.pyc
/usr/lib/python2.4/site-packages/whisper.pyo
