%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit2
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl):	%{_pearname} - zestaw testów regresyjnych
Name:		php-pear-%{_pearname}
Version:	2.0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	17755636fb94908eac364f643b4479ab
URL:		http://pear.php.net/package/PHPUnit2/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPUnit2 is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/ .

In PEAR status of this package is: %{_status}.

%description -l pl
PHPUnit2 jest zestawem testów regresyjnych u¿ywanych przez
programistów, którzy implementuj± jednostki testowe w PHP. Jest
bazowane na JUnit, który mo¿na znale¼æ pod adresem
http://www.junit.org/ .

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Extensions,Framework,Runner,Tests/{Extensions,Framework,Runner},TextUI,Util}

install %{_pearname}-%{version}/Extensions/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Extensions
install %{_pearname}-%{version}/Framework/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Framework
install %{_pearname}-%{version}/Runner/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Runner
install %{_pearname}-%{version}/Tests/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests
install %{_pearname}-%{version}/Tests/Extensions/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests/Extensions/
install %{_pearname}-%{version}/Tests/Framework/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests/Framework
install %{_pearname}-%{version}/Tests/Runner/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tests/Runner
install %{_pearname}-%{version}/TextUI/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/TextUI
install %{_pearname}-%{version}/Util/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Util

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}
