%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit2
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - Regression testing framework for unit tests.
Summary(pl):	%{_pearname} - Zestaw testów regresyjnych.
Name:		php-pear-%{_pearname}
Version:	2.0.0
%define	_version	2.0.0beta1
Release:	0.beta1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{_version}.tgz
# Source0-md5:	1fd16ce40fd539abb6356e4656d10a3c
URL:		http://pear.php.net/package/PHPUnit2/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPUnit2 is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/.

This class has in PEAR status: %{_status}.

%description -l pl
PHPUnit2 jest zestawem testów regresyjnych u¿ywanych przez developerów,
którzy implementuj± jednostki testowe w PHP. Jest bazowane na JUnit,
który mo¿na znale¼æ pod adresem http://www.junit.org/.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{_version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Extensions/Logger,Framework,Runner,Tests/{Extensions,Framework,Runner},TextUI,Util}

install %{_pearname}-%{_version}/Extensions/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Extensions
install %{_pearname}-%{_version}/Extensions/Logger/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Extensions/Logger
install %{_pearname}-%{_version}/Framework/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Framework
install %{_pearname}-%{_version}/Runner/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Runner
install %{_pearname}-%{_version}/Tests/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests
install %{_pearname}-%{_version}/Tests/Extensions/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests/Extensions/
install %{_pearname}-%{_version}/Tests/Framework/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests/Framework
install %{_pearname}-%{_version}/Tests/Runner/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests/Runner
install %{_pearname}-%{_version}/TextUI/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/TextUI
install %{_pearname}-%{_version}/Util/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Util

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}
