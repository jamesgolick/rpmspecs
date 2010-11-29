Summary: Ganglia
Name: ganglia
Version: 3.1.7
Release: fetlife1
Source0: ganglia-3.1.7.tar.gz
License: GPL
Group: Monitoring
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libconfuse-devel pcre-devel rrdtool-devel
requires: libconfuse pcre rrdtool

%description
Make some relevant package description here

%package core
Summary: ganglia core
Group: monitoring
%description core
The core of the ganglia monitoring system. Includes gmond, gmetric, gstat, and necessary libs.

%package gmetad
Summary: ganglia gmetad
Group: monitoring
requires: ganglia-core
%description gmetad
ganglia gmetad.

%package web
Summary: ganglia web interface
Group: monitoring
%description web
ganglia web interface

%prep
%setup -q

%build
./configure --sysconfdir=/etc/ganglia --with-gmetad
make

%install
%makeinstall
mkdir -p $RPM_BUILD_ROOT/etc/ganglia
mv $RPM_BUILD_ROOT/etc/gmetad.conf $RPM_BUILD_ROOT/etc/ganglia/gmetad.conf
install -d $RPM_BUILD_ROOT/usr/share/man/man1/
install -C -m 0644 mans/gmetric.1 $RPM_BUILD_ROOT/usr/share/man/man1/gmetric.1
install -C -m 0644 mans/gmond.1 $RPM_BUILD_ROOT/usr/share/man/man1/gmond.1
install -C -m 0644 mans/gstat.1 $RPM_BUILD_ROOT/usr/share/man/man1/gstat.1
install -C -m 0644 mans/gmetad.1 $RPM_BUILD_ROOT/usr/share/man/man1/gmetad.1
install -d -m 0755 $RPM_BUILD_ROOT/etc/init.d/
install -C -m 0755 examples/gmond-init $RPM_BUILD_ROOT/etc/init.d/gmond
install -C -m 0755 examples/gmetad-init $RPM_BUILD_ROOT/etc/init.d/gmetad
install -C -m 0755 examples/gmond.conf $RPM_BUILD_ROOT/etc/ganglia/gmond.conf
install -d -m 0755 $RPM_BUILD_ROOT/var/www/ganglia
install -C -m 0755 web/cluster_legend.html					  $RPM_BUILD_ROOT/var/www/ganglia/cluster_legend.html
install -C -m 0755 web/host_view.php                                              $RPM_BUILD_ROOT/var/www/ganglia/host_view.php
install -C -m 0755 web/get_context.php                                            $RPM_BUILD_ROOT/var/www/ganglia/get_context.php
install -C -m 0755 web/cluster_view.php                                           $RPM_BUILD_ROOT/var/www/ganglia/cluster_view.php
install -C -m 0755 web/footer.php                                                 $RPM_BUILD_ROOT/var/www/ganglia/footer.php
install -C -m 0755 web/Makefile.am                                                $RPM_BUILD_ROOT/var/www/ganglia/Makefile.am
install -C -m 0755 web/node_legend.html                                           $RPM_BUILD_ROOT/var/www/ganglia/node_legend.html
install -C -m 0755 web/eval_config.php                                            $RPM_BUILD_ROOT/var/www/ganglia/eval_config.php
install -C -m 0755 web/COPYING                                                    $RPM_BUILD_ROOT/var/www/ganglia/COPYING
install -C -m 0755 web/meta_view.php                                              $RPM_BUILD_ROOT/var/www/ganglia/meta_view.php
install -C -m 0755 web/version.php.in                                             $RPM_BUILD_ROOT/var/www/ganglia/version.php.in
install -C -m 0755 web/functions.php                                              $RPM_BUILD_ROOT/var/www/ganglia/functions.php
install -C -m 0755 web/graph.php                                                  $RPM_BUILD_ROOT/var/www/ganglia/graph.php
install -C -m 0755 web/conf.php                                                   $RPM_BUILD_ROOT/var/www/ganglia/conf.php
install -C -m 0755 web/pie.php                                                    $RPM_BUILD_ROOT/var/www/ganglia/pie.php
install -C -m 0755 web/AUTHORS                                                    $RPM_BUILD_ROOT/var/www/ganglia/AUTHORS
install -d -m 0755                                                                $RPM_BUILD_ROOT/var/www/ganglia/graph.d/
install -C -m 0755 web/graph.d/mem_report.php                                     $RPM_BUILD_ROOT/var/www/ganglia/graph.d/mem_report.php
install -C -m 0755 web/graph.d/sample_report.php                                  $RPM_BUILD_ROOT/var/www/ganglia/graph.d/sample_report.php
install -C -m 0755 web/graph.d/packet_report.php                                  $RPM_BUILD_ROOT/var/www/ganglia/graph.d/packet_report.php
install -C -m 0755 web/graph.d/metric.php                                         $RPM_BUILD_ROOT/var/www/ganglia/graph.d/metric.php
install -C -m 0755 web/graph.d/network_report.php                                 $RPM_BUILD_ROOT/var/www/ganglia/graph.d/network_report.php
install -C -m 0755 web/graph.d/load_report.php                                    $RPM_BUILD_ROOT/var/www/ganglia/graph.d/load_report.php
install -C -m 0755 web/graph.d/cpu_report.php                                     $RPM_BUILD_ROOT/var/www/ganglia/graph.d/cpu_report.php
install -C -m 0755 web/grid_tree.php                                              $RPM_BUILD_ROOT/var/www/ganglia/grid_tree.php
install -C -m 0755 web/conf.php.in                                                $RPM_BUILD_ROOT/var/www/ganglia/conf.php.in
install -C -m 0755 web/Makefile.in                                                $RPM_BUILD_ROOT/var/www/ganglia/Makefile.in
install -C -m 0755 web/class.TemplatePower.inc.php                                $RPM_BUILD_ROOT/var/www/ganglia/class.TemplatePower.inc.php
install -C -m 0755 web/header.php                                                 $RPM_BUILD_ROOT/var/www/ganglia/header.php
install -C -m 0755 web/index.php                                                  $RPM_BUILD_ROOT/var/www/ganglia/index.php
install -C -m 0755 web/version.php                                                $RPM_BUILD_ROOT/var/www/ganglia/version.php
install -C -m 0755 web/physical_view.php                                          $RPM_BUILD_ROOT/var/www/ganglia/physical_view.php
install -C -m 0755 web/ganglia.php                                                $RPM_BUILD_ROOT/var/www/ganglia/ganglia.php
install -C -m 0755 web/get_ganglia.php                                            $RPM_BUILD_ROOT/var/www/ganglia/get_ganglia.php
install -C -m 0755 web/auth.php                                                   $RPM_BUILD_ROOT/var/www/ganglia/auth.php
install -C -m 0755 web/private_clusters                                           $RPM_BUILD_ROOT/var/www/ganglia/private_clusters
install -C -m 0755 web/Makefile                                                   $RPM_BUILD_ROOT/var/www/ganglia/Makefile
install -d -m 0755                                                                $RPM_BUILD_ROOT/var/www/ganglia/templates/
install -d -m 0755                                                                $RPM_BUILD_ROOT/var/www/ganglia/templates/default/
install -C -m 0755 web/templates/default/grid_tree.tpl                            $RPM_BUILD_ROOT/var/www/ganglia/templates/default/grid_tree.tpl
install -C -m 0755 web/templates/default/meta_view.tpl                            $RPM_BUILD_ROOT/var/www/ganglia/templates/default/meta_view.tpl
install -C -m 0755 web/templates/default/footer.tpl                               $RPM_BUILD_ROOT/var/www/ganglia/templates/default/footer.tpl
install -C -m 0755 web/templates/default/show_node.tpl                            $RPM_BUILD_ROOT/var/www/ganglia/templates/default/show_node.tpl
install -d -m 0755                                                                $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/
install -C -m 0755 web/templates/default/images/node_75-100.jpg                   $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/node_75-100.jpg
install -C -m 0755 web/templates/default/images/grid_overloaded.jpg               $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/grid_overloaded.jpg
install -C -m 0755 web/templates/default/images/node_overloaded.jpg               $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/node_overloaded.jpg
install -C -m 0755 web/templates/default/images/node_25-49.jpg                    $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/node_25-49.jpg
install -C -m 0755 web/templates/default/images/cluster_overloaded.jpg            $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/cluster_overloaded.jpg
install -C -m 0755 web/templates/default/images/cluster_25-49.jpg                 $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/cluster_25-49.jpg
install -C -m 0755 web/templates/default/images/cluster_50-74.jpg                 $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/cluster_50-74.jpg
install -C -m 0755 web/templates/default/images/grid_private.jpg                  $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/grid_private.jpg
install -C -m 0755 web/templates/default/images/logo.jpg                          $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/logo.jpg
install -C -m 0755 web/templates/default/images/grid_0-24.jpg                     $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/grid_0-24.jpg
install -C -m 0755 web/templates/default/images/grid_25-49.jpg                    $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/grid_25-49.jpg
install -C -m 0755 web/templates/default/images/node_50-74.jpg                    $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/node_50-74.jpg
install -C -m 0755 web/templates/default/images/grid_75-100.jpg                   $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/grid_75-100.jpg
install -C -m 0755 web/templates/default/images/node_0-24.jpg                     $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/node_0-24.jpg
install -C -m 0755 web/templates/default/images/grid_50-74.jpg                    $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/grid_50-74.jpg
install -C -m 0755 web/templates/default/images/cluster_0-24.jpg                  $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/cluster_0-24.jpg
install -C -m 0755 web/templates/default/images/node_dead.jpg                     $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/node_dead.jpg
install -C -m 0755 web/templates/default/images/cluster_private.jpg               $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/cluster_private.jpg
install -C -m 0755 web/templates/default/images/cluster_75-100.jpg                $RPM_BUILD_ROOT/var/www/ganglia/templates/default/images/cluster_75-100.jpg
install -C -m 0755 web/templates/default/cluster_view.tpl                         $RPM_BUILD_ROOT/var/www/ganglia/templates/default/cluster_view.tpl
install -C -m 0755 web/templates/default/cluster_extra.tpl                        $RPM_BUILD_ROOT/var/www/ganglia/templates/default/cluster_extra.tpl
install -C -m 0755 web/templates/default/host_view.tpl                            $RPM_BUILD_ROOT/var/www/ganglia/templates/default/host_view.tpl
install -C -m 0755 web/templates/default/node_extra.tpl                           $RPM_BUILD_ROOT/var/www/ganglia/templates/default/node_extra.tpl
install -C -m 0755 web/templates/default/header-nobanner.tpl                      $RPM_BUILD_ROOT/var/www/ganglia/templates/default/header-nobanner.tpl
install -C -m 0755 web/templates/default/physical_view.tpl                        $RPM_BUILD_ROOT/var/www/ganglia/templates/default/physical_view.tpl
install -C -m 0755 web/templates/default/host_extra.tpl                           $RPM_BUILD_ROOT/var/www/ganglia/templates/default/host_extra.tpl
install -C -m 0755 web/templates/default/header.tpl                               $RPM_BUILD_ROOT/var/www/ganglia/templates/default/header.tpl
install -C -m 0755 web/styles.css                                                 $RPM_BUILD_ROOT/var/www/ganglia/styles.css
install -C -m 0755 web/show_node.php                                              $RPM_BUILD_ROOT/var/www/ganglia/show_node.php

%clean
rm -rf $RPM_BUILD_ROOT

%files core
%doc /usr/share/man/man1/gmetric.1.gz
%doc /usr/share/man/man1/gstat.1.gz
%doc /usr/share/man/man1/gmond.1.gz
/usr/bin/ganglia-config
/usr/bin/gmetric
/usr/bin/gstat
/usr/sbin/gmond
/etc/init.d/gmond
/etc/ganglia/gmond.conf
/usr/include/ganglia_gexec.h
/usr/include/ganglia.h
/usr/include/gm_metric.h
/usr/include/gm_mmn.h
/usr/include/gm_msg.h
/usr/include/gm_protocol.h
/usr/include/gm_value.h
/usr/lib64/ganglia/modcpu.so
/usr/lib64/ganglia/moddisk.so
/usr/lib64/ganglia/modload.so
/usr/lib64/ganglia/modmem.so
/usr/lib64/ganglia/modmulticpu.so
/usr/lib64/ganglia/modnet.so
/usr/lib64/ganglia/modproc.so
/usr/lib64/ganglia/modsys.so
/usr/lib64/libganglia-3.1.7.so.0
/usr/lib64/libganglia-3.1.7.so.0.0.0
/usr/lib64/libganglia.a
/usr/lib64/libganglia.la
/usr/lib64/libganglia.so

%files gmetad
%doc /usr/share/man/man1/gmetad.1.gz
%config /etc/ganglia/gmetad.conf
/usr/sbin/gmetad
/etc/init.d/gmetad

%files web
/var/www/ganglia/cluster_legend.html
/var/www/ganglia/host_view.php
/var/www/ganglia/get_context.php
/var/www/ganglia/cluster_view.php
/var/www/ganglia/footer.php
/var/www/ganglia/Makefile.am
/var/www/ganglia/node_legend.html
/var/www/ganglia/eval_config.php
/var/www/ganglia/COPYING
/var/www/ganglia/meta_view.php
/var/www/ganglia/version.php.in
/var/www/ganglia/functions.php
/var/www/ganglia/graph.php
/var/www/ganglia/conf.php
/var/www/ganglia/pie.php
/var/www/ganglia/AUTHORS
/var/www/ganglia/graph.d/
/var/www/ganglia/graph.d/mem_report.php
/var/www/ganglia/graph.d/sample_report.php
/var/www/ganglia/graph.d/packet_report.php
/var/www/ganglia/graph.d/metric.php
/var/www/ganglia/graph.d/network_report.php
/var/www/ganglia/graph.d/load_report.php
/var/www/ganglia/graph.d/cpu_report.php
/var/www/ganglia/grid_tree.php
/var/www/ganglia/conf.php.in
/var/www/ganglia/Makefile.in
/var/www/ganglia/class.TemplatePower.inc.php
/var/www/ganglia/header.php
/var/www/ganglia/index.php
/var/www/ganglia/version.php
/var/www/ganglia/physical_view.php
/var/www/ganglia/ganglia.php
/var/www/ganglia/get_ganglia.php
/var/www/ganglia/auth.php
/var/www/ganglia/private_clusters
/var/www/ganglia/Makefile
/var/www/ganglia/templates/
/var/www/ganglia/templates/default/
/var/www/ganglia/templates/default/grid_tree.tpl
/var/www/ganglia/templates/default/meta_view.tpl
/var/www/ganglia/templates/default/footer.tpl
/var/www/ganglia/templates/default/show_node.tpl
/var/www/ganglia/templates/default/images/
/var/www/ganglia/templates/default/images/node_75-100.jpg
/var/www/ganglia/templates/default/images/grid_overloaded.jpg
/var/www/ganglia/templates/default/images/node_overloaded.jpg
/var/www/ganglia/templates/default/images/node_25-49.jpg
/var/www/ganglia/templates/default/images/cluster_overloaded.jpg
/var/www/ganglia/templates/default/images/cluster_25-49.jpg
/var/www/ganglia/templates/default/images/cluster_50-74.jpg
/var/www/ganglia/templates/default/images/grid_private.jpg
/var/www/ganglia/templates/default/images/logo.jpg
/var/www/ganglia/templates/default/images/grid_0-24.jpg
/var/www/ganglia/templates/default/images/grid_25-49.jpg
/var/www/ganglia/templates/default/images/node_50-74.jpg
/var/www/ganglia/templates/default/images/grid_75-100.jpg
/var/www/ganglia/templates/default/images/node_0-24.jpg
/var/www/ganglia/templates/default/images/grid_50-74.jpg
/var/www/ganglia/templates/default/images/cluster_0-24.jpg
/var/www/ganglia/templates/default/images/node_dead.jpg
/var/www/ganglia/templates/default/images/cluster_private.jpg
/var/www/ganglia/templates/default/images/cluster_75-100.jpg
/var/www/ganglia/templates/default/cluster_view.tpl
/var/www/ganglia/templates/default/cluster_extra.tpl
/var/www/ganglia/templates/default/host_view.tpl
/var/www/ganglia/templates/default/node_extra.tpl
/var/www/ganglia/templates/default/header-nobanner.tpl
/var/www/ganglia/templates/default/physical_view.tpl
/var/www/ganglia/templates/default/host_extra.tpl
/var/www/ganglia/templates/default/header.tpl
/var/www/ganglia/styles.css
/var/www/ganglia/show_node.php
