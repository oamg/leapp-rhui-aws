# Update name of package
Name:           leapp-rhui-aws
Version:        1.0.21
Release:        1%{?dist}
Summary:        Leapp in-place upgrade cloud specific package

# Provider variable is name of subdirectory that is cloud specific, please
# refer to LeApp documentation/code for what subdir you should use.
# Examples: aws, azure
%global provider    aws
%global leappfilespath  %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui

License:        LGPLv2+
URL:            http://redhat.com
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}

BuildArch:      noarch

# Update description
%description
Leapp in-place upgrade on AWS

%package sap-e4s
Summary: Yum repository and entitlement certificate configuration for Red Hat SAP Bundle
Group:   System Environment/Base
%description sap-e4s
Leapp in-place upgrade of SAP on AWS.

%if 0%{?rhel} == 7
%package sap-eus
Summary: Yum repository and entitlement certificate configuration for Red Hat SAP Bundle
Group:   System Environment/Base
%description sap-eus
Leapp in-place upgrade of SAP on AWS.
%endif

%if 0%{?rhel} == 8
%package ha
Summary: DNF repository and entitlement certificate configuration for Red Hat Enterprise Linux with HA
Group:   System Environment/Base
%description ha
Leapp configuration and support files for in-place upgrades of Red Hat Enterprise Linux with HA on AWS.
%endif

%if 0%{?rhel} == 9
%package ha
Summary: DNF repository and entitlement certificate configuration for Red Hat Enterprise Linux with HA
Group:   System Environment/Base
%description ha
Leapp configuration and support files for in-place upgrades of Red Hat Enterprise Linux with HA on AWS.
%endif

%prep
%setup -q -n %{name}-%{version}

%build

rm -rf $RPM_BUILD_ROOT

%if 0%{?rhel} == 7
%install

for provider in %{provider} %{provider}-sap-eus %{provider}-sap-e4s
do
  mkdir -p %{buildroot}%{leappfilespath}/$provider
done

mkdir -p %{buildroot}/usr/lib/python2.7/site-packages/dnf-plugins/

# Base RHEL
cp src/7to8/cdn.redhat.com-chain.crt            %{buildroot}%{leappfilespath}/%{provider}
cp src/7to8/leapp-%{provider}.repo              %{buildroot}%{leappfilespath}/%{provider}
cp src/7to8/content-rhel8.key                   %{buildroot}%{leappfilespath}/%{provider}
cp src/7to8/content-rhel8.crt                   %{buildroot}%{leappfilespath}/%{provider}
cp src/7to8/rhui-client-config-server-8.key     %{buildroot}%{leappfilespath}/%{provider}
cp src/7to8/rhui-client-config-server-8.crt     %{buildroot}%{leappfilespath}/%{provider}
cp src/7to8/rhel7-dnf-plugin/amazon-id.py       %{buildroot}%{leappfilespath}/%{provider}

# SAP Bundles
cp src/7to8/cdn.redhat.com-chain.crt                    %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/leapp-aws-sap.repo                          %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/content-rhel8-sap-bundle.crt                %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/content-rhel8-sap-bundle.key                %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/leapp-aws-sap-e4s.repo                      %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/content-rhel8-sap-bundle-e4s.crt            %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/content-rhel8-sap-bundle-e4s.key            %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/rhui-client-config-server-8-sap-bundle.key  %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/rhui-client-config-server-8-sap-bundle.crt  %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/7to8/rhel7-dnf-plugin/amazon-id.py               %{buildroot}%{leappfilespath}/%{provider}-sap-e4s

exit 0

%files
# List the directtories we have created so that uninstalling the package will clean them up
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/%{provider}

%{leappfilespath}/%{provider}/rhui-client-config-server-8.key
%{leappfilespath}/%{provider}/rhui-client-config-server-8.crt
%{leappfilespath}/%{provider}/content-rhel8.key
%{leappfilespath}/%{provider}/content-rhel8.crt
%{leappfilespath}/%{provider}/cdn.redhat.com-chain.crt
%{leappfilespath}/%{provider}/leapp-%{provider}.repo
%{leappfilespath}/%{provider}/amazon-id.py

%files sap-e4s
# List the directtories we have created so that uninstalling the package will clean them up
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/%{provider}-sap-e4s

%{leappfilespath}/%{provider}-sap-e4s/rhui-client-config-server-8-sap-bundle.key
%{leappfilespath}/%{provider}-sap-e4s/rhui-client-config-server-8-sap-bundle.crt
%{leappfilespath}/%{provider}-sap-e4s/content-rhel8-sap-bundle.crt
%{leappfilespath}/%{provider}-sap-e4s/content-rhel8-sap-bundle.key
%{leappfilespath}/%{provider}-sap-e4s/content-rhel8-sap-bundle-e4s.crt
%{leappfilespath}/%{provider}-sap-e4s/content-rhel8-sap-bundle-e4s.key
%{leappfilespath}/%{provider}-sap-e4s/cdn.redhat.com-chain.crt
%{leappfilespath}/%{provider}-sap-e4s/leapp-%{provider}-sap-e4s.repo
%{leappfilespath}/%{provider}-sap-e4s/leapp-%{provider}-sap.repo
%{leappfilespath}/%{provider}-sap-e4s/amazon-id.py
%endif

%if 0%{?rhel} == 8

for provider in %{provider} %{provider}-sap-e4s %{provider}-ha
do
  mkdir -p %{buildroot}%{leappfilespath}/$provider
done

# Base RHEL
cp src/8to9/cdn.redhat.com-chain.crt         %{buildroot}%{leappfilespath}/%{provider}
cp src/8to9/leapp-%{provider}.repo           %{buildroot}%{leappfilespath}/%{provider}
cp src/8to9/content-rhel9.key                %{buildroot}%{leappfilespath}/%{provider}
cp src/8to9/rhui-client-config-server-9.key  %{buildroot}%{leappfilespath}/%{provider}
cp src/8to9/content-rhel9.crt                %{buildroot}%{leappfilespath}/%{provider}
cp src/8to9/rhui-client-config-server-9.crt  %{buildroot}%{leappfilespath}/%{provider}

# sap-e4s keys and certs
cp src/8to9/leapp-%{provider}-sap-e4s.repo              %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/8to9/cdn.redhat.com-chain.crt                    %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/8to9/content-rhel9-sap-bundle-e4s.key            %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/8to9/content-rhel9-sap-bundle-e4s.crt            %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/8to9/rhui-client-config-server-9-sap-bundle.crt  %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/8to9/rhui-client-config-server-9-sap-bundle.key  %{buildroot}%{leappfilespath}/%{provider}-sap-e4s

# High Availability subpackage
mkdir -p %{buildroot}%{_sysconfdir}/leapp/actor_conf.d/
cp src/8to9/high_availability/amazon-id.py                       %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/8to9/high_availability/content-rhel9-ha.crt               %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/8to9/high_availability/content-rhel9-ha.key               %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/8to9/high_availability/redhat-rhui-client-config-ha.repo  %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/8to9/high_availability/redhat-rhui-ha.repo                %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/8to9/high_availability/rhui-client-config-server-9-ha.crt %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/8to9/high_availability/rhui-client-config-server-9-ha.key %{buildroot}%{leappfilespath}/%{provider}-ha

cp src/8to9/high_availability/leapp-rhui-config.yaml             %{buildroot}%{_sysconfdir}/leapp/actor_conf.d/

exit 0

%files
# List the directtories we have created so that uninstalling the package will clean them up
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/%{provider}

%{leappfilespath}/%{provider}/rhui-client-config-server-9.key
%{leappfilespath}/%{provider}/rhui-client-config-server-9.crt
%{leappfilespath}/%{provider}/content-rhel9.key
%{leappfilespath}/%{provider}/content-rhel9.crt
%{leappfilespath}/%{provider}/cdn.redhat.com-chain.crt
%{leappfilespath}/%{provider}/leapp-%{provider}.repo

%files sap-e4s
# List the directtories we have created so that uninstalling the package will clean them up
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/%{provider}-sap-e4s

%{leappfilespath}/%{provider}-sap-e4s/rhui-client-config-server-9-sap-bundle.crt
%{leappfilespath}/%{provider}-sap-e4s/rhui-client-config-server-9-sap-bundle.key
%{leappfilespath}/%{provider}-sap-e4s/content-rhel9-sap-bundle-e4s.crt
%{leappfilespath}/%{provider}-sap-e4s/content-rhel9-sap-bundle-e4s.key
%{leappfilespath}/%{provider}-sap-e4s/cdn.redhat.com-chain.crt
%{leappfilespath}/%{provider}-sap-e4s/leapp-%{provider}-sap-e4s.repo

%files ha
%dir %{_sysconfdir}/leapp/actor_conf.d/
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/%{provider}-ha

%{_sysconfdir}/leapp/actor_conf.d/leapp-rhui-config.yaml
%{leappfilespath}/%{provider}-ha/amazon-id.py
%{leappfilespath}/%{provider}-ha/content-rhel9-ha.crt
%{leappfilespath}/%{provider}-ha/content-rhel9-ha.key
%{leappfilespath}/%{provider}-ha/redhat-rhui-client-config-ha.repo
%{leappfilespath}/%{provider}-ha/redhat-rhui-ha.repo
%{leappfilespath}/%{provider}-ha/rhui-client-config-server-9-ha.crt
%{leappfilespath}/%{provider}-ha/rhui-client-config-server-9-ha.key

%endif


%if 0%{?rhel} == 9

for provider in %{provider} %{provider}-sap-e4s %{provider}-ha
do
  mkdir -p %{buildroot}%{leappfilespath}/$provider
done

# Base RHEL
cp src/9to10/leapp-aws.repo                    %{buildroot}%{leappfilespath}/%{provider}
cp src/9to10/cdn.redhat.com-chain.crt          %{buildroot}%{leappfilespath}/%{provider}
cp src/9to10/content-rhel10.key                %{buildroot}%{leappfilespath}/%{provider}
cp src/9to10/content-rhel10.crt                %{buildroot}%{leappfilespath}/%{provider}
cp src/9to10/rhui-client-config-server-10.key  %{buildroot}%{leappfilespath}/%{provider}
cp src/9to10/rhui-client-config-server-10.crt  %{buildroot}%{leappfilespath}/%{provider}

# sap-e4s
cp src/9to10/leapp-%{provider}-sap-e4s.repo               %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/9to10/cdn.redhat.com-chain.crt                     %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/9to10/content-rhel10-sap-bundle-e4s.key            %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/9to10/content-rhel10-sap-bundle-e4s.crt            %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/9to10/rhui-client-config-server-10-sap-bundle.crt  %{buildroot}%{leappfilespath}/%{provider}-sap-e4s
cp src/9to10/rhui-client-config-server-10-sap-bundle.key  %{buildroot}%{leappfilespath}/%{provider}-sap-e4s

# High Availability subpackage
mkdir -p %{buildroot}%{_sysconfdir}/leapp/actor_conf.d/
cp src/9to10/high_availability/amazon-id.py                       %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/9to10/high_availability/content-rhel10-ha.crt              %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/9to10/high_availability/content-rhel10-ha.key              %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/9to10/high_availability/redhat-rhui-client-config-ha.repo  %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/9to10/high_availability/redhat-rhui-ha.repo                %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/9to10/high_availability/rhui-client-config-server-10-ha.crt %{buildroot}%{leappfilespath}/%{provider}-ha
cp src/9to10/high_availability/rhui-client-config-server-10-ha.key %{buildroot}%{leappfilespath}/%{provider}-ha

cp src/9to10/high_availability/leapp-rhui-config.yaml             %{buildroot}%{_sysconfdir}/leapp/actor_conf.d/

exit 0

%files
# List the directtories we have created so that uninstalling the package will clean them up
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/aws

%{leappfilespath}/%{provider}/rhui-client-config-server-10.key
%{leappfilespath}/%{provider}/rhui-client-config-server-10.crt
%{leappfilespath}/%{provider}/content-rhel10.key
%{leappfilespath}/%{provider}/content-rhel10.crt
%{leappfilespath}/%{provider}/cdn.redhat.com-chain.crt
%{leappfilespath}/%{provider}/leapp-aws.repo

%files sap-e4s
# List the directtories we have created so that uninstalling the package will clean them up
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/%{provider}-sap-e4s

%{leappfilespath}/%{provider}-sap-e4s/rhui-client-config-server-10-sap-bundle.crt
%{leappfilespath}/%{provider}-sap-e4s/rhui-client-config-server-10-sap-bundle.key
%{leappfilespath}/%{provider}-sap-e4s/content-rhel10-sap-bundle-e4s.crt
%{leappfilespath}/%{provider}-sap-e4s/content-rhel10-sap-bundle-e4s.key
%{leappfilespath}/%{provider}-sap-e4s/cdn.redhat.com-chain.crt
%{leappfilespath}/%{provider}-sap-e4s/leapp-%{provider}-sap-e4s.repo

%files ha
%dir %{_sysconfdir}/leapp/actor_conf.d/
%dir %{_datadir}/leapp-repository
%dir %{_datadir}/leapp-repository/repositories
%dir %{_datadir}/leapp-repository/repositories/system_upgrade
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui
%dir %{_datadir}/leapp-repository/repositories/system_upgrade/common/files/rhui/%{provider}-ha

%{_sysconfdir}/leapp/actor_conf.d/leapp-rhui-config.yaml
%{leappfilespath}/%{provider}-ha/amazon-id.py
%{leappfilespath}/%{provider}-ha/content-rhel10-ha.crt
%{leappfilespath}/%{provider}-ha/content-rhel10-ha.key
%{leappfilespath}/%{provider}-ha/redhat-rhui-client-config-ha.repo
%{leappfilespath}/%{provider}-ha/redhat-rhui-ha.repo
%{leappfilespath}/%{provider}-ha/rhui-client-config-server-10-ha.crt
%{leappfilespath}/%{provider}-ha/rhui-client-config-server-10-ha.key

%endif


%changelog
* Mon Nov 23 2026 Karolina Kula <kkula@redhat.com> 1.0.21-1
- Handle obsolete certificates and map the Extensions repo

* Wed Sep 23 2026 Martin Minar <mminar@redhat.com> 1.0.20-1
- leapp(aws): add RHEL9 HA package (mhecko@redhat.com)
- Fix codeready-builder-for-rhel-10-rhui-rpms repo definition for AWS
  (mmatuska@redhat.com)

* Thu Jul 10 2026 Michal Hecko <mhecko@redhat.com> 1.0.19-1
- leapp(aws): add RHEL 9 HA package for 9>10 upgrades

* Thu Nov 27 2025 Martin Minar <mminar@redhat.com> 1.0.18-1
- leapp(aws-ha): update config file extension (mhecko@redhat.com)
- Add the High Availability repo definitions for leapp-rhui-aws-ha
  (bparry@redhat.com)

* Thu Nov 27 2025 Michal hecko <mhecko@redhat.com> 1.0.17-1
- leapp-rhui-aws-ha: add highavailability repo
- leapp-rhui-aws-ha: change config extension

* Wed Nov 26 2025 Martin Minar <mminar@redhat.com> 1.0.16-1
- leapp(aws): add RHEL9 package for RHEL SAP (mhecko@redhat.com)
- leapp(aws): add package for 9>10 upgrades of base RHEL systems
  (mhecko@redhat.com)

* Thu Jul 31 2025 Michal Hecko <mhecko@redhat.com> 1.0.15-1
- add RHEL9 package for 9>10 upgrades of base RHEL systems

* Wed Jul 16 2025 Martin Minar <mminar@redhat.com> 1.0.14-1
- leapp: make leapp-rhui-aws-ha a subpackage of leapp-rhui-aws
  (michal.sk.com@gmail.com)
- leapp-rhui-aws: add package for 8>9 AWS HA (mhecko@redhat.com)

* Tue Jul 15 2025 Michal Hecko <mhecko@redhat.com> 1.0.14-1
- leapp(aws): add subpackage for RHEL with High Availability

* Mon Jul 01 2024 Martin Minar <mminar@redhat.com> 1.0.13-1
- leapp(aws): fix inconsistent baseos/appstream repoids (mhecko@redhat.com)
- leapp-rhui-aws: accomodate for changes on RHEL SAP 8.10 (mhecko@redhat.com)

* Thu May 23 2024 Michal Hecko <mhecko@redhat.com> 1.0.12-1
- Add new keys, certs and non-e4s sap files

* Thu May 23 2024 Radek Bíba <radek@redhat.com> 1.0.11-1
- (hotfix) leapp-rhui*: remove dependencies on leapp (mhecko@redhat.com)

* Tue May 14 2024 Michal Hecko <mhecko@redhat.com> 1.0.10-1
- drop dependencies on leapp and leapp-upgrade-el{X}to{X+1}

* Tue Apr 30 2024 Martin Minar <mminar@redhat.com> 1.0.9-1
- Revert leapp RHUI package simplification for AWS
  (75834032+matejmatuska@users.noreply.github.com)
- leapp: add dependencies on leapp-upgrade for -sap packages
  (mhecko@redhat.com)
- simplify aws packages (mhecko@redhat.com)

* Fri Jan 26 2024 Michal Hecko <mhecko@redhat.com> 1.0.8-1
- add dependencies on leapp to the leapp-rhui-*-sap packages

* Thu Nov 10 2022 Martin Minar <mminar@redhat.com> 1.0.7-1
- leapp(aws): clean up AWS specfile so it is easier to follow
  (mhecko@redhat.com)
- leapp(aws): Add AWS SAP rhel9 content and extend specfile accordingly
  (mhecko@redhat.com)

* Tue Jul 12 2022 Michal Hecko <mhecko@redhat.com> 1.0.6-1
- Add SAP rhel9 content for AWS
- Refactor specfile to be more straightforward

* Tue May 10 2022 Martin Minar <mminar@redhat.com> 1.0.5-1
- new package built with tito

* Thu Feb 10 2022 Martin Minar <mminar@redhat.com> 1.0.4-1
- Refactoring to enable RHEL 8 to RHEL 9 upgrades (mreznik@redhat.com)

* Thu Feb 10 2022 Michal Reznik <mreznik@redhat.com> 1.0.3-1
- Refactoring to enable RHEL 8 to RHEL 9 upgrades (mreznik@redhat.com)
* Tue Oct 19 2021 Martin Minar <mminar@redhat.com> 1.0.2-1
- Fix "bare words are no longer supported" (mminar@redhat.com)
- SAP related refactoring (mreznik@redhat.com)
- Updated LeApp package to include Extras in SAP variant. (mminar@redhat.com)
- Typos fixes (mminar@redhat.com)
- Adding SAP Bundle variants. (mminar@redhat.com)
* Tue Aug 31 2021 Michal Reznik <mreznik@redhat.com> 1.0.1-2
- SAP related refactoring
* Tue Sep 22 2020 Martin Minar <mminar@redhat.com> 1.0.1-1
- new package built with tito
