%define		_class		Console
%define		_subclass	CommandLine
%define		_status		stable
%define		_pearname	Console_CommandLine
Summary:	%{_pearname} - A full featured command line options and arguments parser
Summary(pl.UTF-8):	%{_pearname} - Bogaty w funkcjonalność analizator parametrów linii poleceń
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	2
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	64685af6b4cb7668d76dfea9fa848bc6
URL:		http://pear.php.net/package/Console_CommandLine/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Console_CommandLine-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Console_CommandLine is a full featured package for managing
command-line options and arguments highly inspired from python
optparse module, it allows the developer to easily build complex
command line interfaces.

Main features:
 - handles sub commands (ie. $ myscript.php -q subcommand -f file),
 - can be completely built from an xml definition file,
 - generate --help and --version options automatically,
 - can be completely customized,
 - builtin support for i18n,
 - and much more...

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Console_CommandLine to udostępniający wiele moliwości pakiet do
zarządzania parametrami linii poleceń, wzorowany na pythonowym module
optparse. Pozwala programiście na łatwe budowanie złożonych
interfejsów linii poleceń (CLI).

Podstawowe cechy:
 - obsługa podpoleceń (np. $ myscript.php -q polecenie -f plik),
 - możliwość generowania z pliku XML,
 - automatyczne generowanie opcji --help oraz --version,
 - możliwość dostosowania do własnych potrzeb,
 - wbudowane wsparcie dla i18n,
 - i wiele innych...

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
%doc install.log docs/Console_CommandLine/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Console/CommandLine
%{php_pear_dir}/Console/CommandLine.php
%{php_pear_dir}/data/%{_pearname}
