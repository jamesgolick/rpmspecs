Summary: redis
Name: redis
Version: 2.2.0.rc3
Release: fetlife1
Source0: redis-2.2.0.rc3.tar.gz
License: GPL
Group: DB
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
redis, it's cool shit.

%prep
%setup -q

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr
make PREFIX=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/redis-benchmark
/usr/bin/redis-check-aof
/usr/bin/redis-check-dump
/usr/bin/redis-cli
/usr/bin/redis-server
