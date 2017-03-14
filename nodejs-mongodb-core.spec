%{?scl:%scl_package nodejs-mongodb-core}
%{!?scl:%global pkg_name %{name}}

%global npm_name mongodb-core
%{?nodejs_find_provides_and_requires}

#tests are turned off due to missinf devDependencies
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-mongodb-core
Version:	2.1.8
Release:	1%{?dist}
Summary:	Core MongoDB driver functionality, no bells and whistles and meant for integration not end applications
Url:		https://github.com/christkv/mongodb-core
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ASL 2.0

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%description
Core MongoDB driver functionality, no bells and whistles and meant for integration not end applications

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js conf.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
node test/runner.js -t functional
%endif

%files
%{nodejs_sitelib}/mongodb-core

%doc README.md
%license LICENSE THIRD-PARTY-NOTICES

%changelog
* Thu Feb 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.8-1
- Update
- Add third party notices to licenses

* Sun Apr 03 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-1
- Initial build

