# TODO:
# - subpackages
# - update desc and summary
%define 	eclipse_ver	3.3

%define		deps_ver	2.0.0
%define		deps_rev	20080517

%define		ver_major	0.7
%define		ver_minor	0
%define		rev		20080521

Summary:	subversive
Summary(pl.UTF-8):	subversive
Name:		eclipse-plugin-subversive
Version:	%{ver_major}.%{ver_minor}
Release:	0.%{rev}.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://download.eclipse.org/technology/subversive/%{ver_major}/builds/Subversive-incubation-%{version}.v%{rev}.zip
# Source0-md5:	1a0cfb22b2f58bccd43c09eecc97f259
Source1:	http://www.polarion.org/projects/subversive/download/eclipse/2.0/builds/Subversive-connectors-%{deps_ver}.v%{deps_rev}.zip
# Source1-md5:	c92e5f71b0ec268b6ada3a2f01ba51cd
Source2:	http://www.polarion.org/projects/subversive/download/integrations/builds/Subversive-integrations-%{deps_ver}.v%{deps_rev}.zip
# Source2-md5:	d6e0ce9a06d9f48b00d452820929be95
URL:		http://www.eclipse.org/subversive/
BuildRequires:	unzip
Requires:	eclipse >= %{eclipse_ver}
Requires:	subversion >= 1.1
Requires:	subversion < 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
Subversive.

% description -l pl.UTF-8
Subversive.

%prep
%setup -q -c -T
unzip -qo %{SOURCE0}
unzip -qo %{SOURCE1}
unzip -qo %{SOURCE2}
rm -f {features,plugins}/*.pack.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r {features,plugins} $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/plugins/*.jar
%{_eclipsedir}/features/*.jar
