
Name:		kafka
Version:	2.12.0.11.0.1
Release:	1%{?dist}
Summary:	install kafka
Group:		Development/Software
License:	Linh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	x86_64
Packager:	$Id$
Requires:	java

%description
This RPM installs kafka

%pre
echo "pre"
echo "rhel=%{?rhel}"
echo "\$1=$1";
exit 0

%prep
exit 0

%build
exit 0

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/opt
mkdir -p %{buildroot}/var/lib/zookeeper
cd %{buildroot}/opt && tar xzvf %{_sourcedir}/kafka_2.12-0.11.0.1.tgz 
mv %{buildroot}/opt/kafka_2.12-0.11.0.1 %{buildroot}/opt/kafka

%if 0%{?rhel} >= 7
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system
install %{_sourcedir}/el7/kafka.service %{buildroot}%{_sysconfdir}/systemd/system/kafka.service
install %{_sourcedir}/el7/zookeeper.service %{buildroot}%{_sysconfdir}/systemd/system/zookeeper.service
%endif
exit 0

%clean
rm -rf %{buildroot}
exit 0

%post
exit 0

%verifyscript
exit 0

%preun
echo "preun"
echo "rhel=%{?rhel}"
echo "\$1=$1";
%if 0%{?rhel} >= 7
	if [ "$1" == "0" ]; then
		echo "Disabling zookeeper\n"
		systemctl disable zookeeper
		echo "Stopping zookeeper\n"
		systemctl stop zookeeper
		echo "Disabling kafka\n"
		systemctl disable kafka
		echo "Stopping kafka\n"
		systemctl stop kafka
	fi
%endif
exit 0

%postun
echo "postun"
echo "rhel=%{?rhel}"
echo "\$1=$1";
rm -rf /opt/kafka
rm -rf /var/lib/zookeeper
exit 0


%files
%attr(700,root,root) /opt/kafka
%attr(700,root,root) /var/lib/zookeeper
%if 0%{?rhel} == 7
%attr(644,root,root) %{_sysconfdir}/systemd/system/kafka.service
%attr(644,root,root) %{_sysconfdir}/systemd/system/zookeeper.service
%endif

%changelog
