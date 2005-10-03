%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit2
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl):	%{_pearname} - zestaw testów regresyjnych
Name:		php-pear-%{_pearname}
Version:	2.2.1
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1ca5f73abbb65c5cce8458aa7af74e78
URL:		http://pear.php.net/package/PHPUnit2/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:5.0.2
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-Benchmark
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(Log.*)'

%description
PHPUnit2 is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at <http://www.junit.org/>.

In PEAR status of this package is: %{_status}.

%description -l pl
PHPUnit2 jest zestawem testów regresyjnych u¿ywanych przez
programistów, którzy implementuj± jednostki testowe w PHP. Jest
bazowane na JUnit, który mo¿na znale¼æ pod adresem
<http://www.junit.org/>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}
