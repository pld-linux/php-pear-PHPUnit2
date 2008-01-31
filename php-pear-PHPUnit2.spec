%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit2
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl.UTF-8):	%{_pearname} - zestaw testów regresyjnych
Name:		php-pear-%{_pearname}
Version:	2.3.6
Release:	4
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	95fe5e8dbb36462dd4d3f3daf8a4e8b3
URL:		http://pear.php.net/package/PHPUnit2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-common >= 3:5.0.2
Requires:	php-pear
Requires:	php-pear-Benchmark
Requires:	php-pear-Console_Getopt
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(Log.*)'

%description
PHPUnit2 is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at <http://www.junit.org/>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHPUnit2 jest zestawem testów regresyjnych używanych przez
programistów, którzy implementują jednostki testowe w PHP. Jest
bazowane na JUnit, który można znaleźć pod adresem
<http://www.junit.org/>.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install
install -d $RPM_BUILD_ROOT%{_bindir}
cp usr/bin/phpunit $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}
%attr(755,root,root) %{_bindir}/phpunit

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
