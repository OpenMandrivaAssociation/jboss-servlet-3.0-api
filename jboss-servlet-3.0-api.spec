%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-servlet-3.0-api
Version:          1.0.2
Release:          1.1%{?dist}
Summary:          Java Servlet 3.0 API

License:          CDDL
Url:              https://www.jboss.org
Source0:          https://github.com/jboss/jboss-servlet-api_spec/archive/jboss-servlet-api_3.0_spec-1.0.2.Final.tar.gz
Source1:          cddl.txt

BuildRequires:    jboss-parent
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin

BuildArch:        noarch

%description
The Java Servlet 3.0 API classes.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-servlet-api_spec-jboss-servlet-api_3.0_spec-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README cddl.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE README cddl.txt

%changelog
* Mon Sep 09 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.2-1
- Upstream release 1.0.2.Final
- Using xmvn
- Don't provide javax.servlet:servlet-api, RHBZ#911016

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-6
- Resolves #961462 - Remove unneeded maven-checkstyle-plugin and 
  maven-eclipse-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-3
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Added mapping to javax.servlet:servlet-api

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120312gitd4b6f2
- Packaging after license cleanup
- Spec cleanup

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging
