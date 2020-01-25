%define		_class		HTML
%define		_subclass	Crypt
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Encrypts text which is later decoded using javascript on the client side
Summary(pl.UTF-8):	%{_pearname} - Szyfruje tekst, który jest po stronie klienta rozkodowany javascriptem
Name:		php-pear-%{_pearname}
Version:	1.3.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2560a624402e2e8847182ef309cdc670
URL:		http://pear.php.net/package/HTML_Crypt/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.0.2-88
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_Crypt provides methods to encrypt text, which can be
later be decrypted using JavaScript on the client side. This is very
useful to prevent spam robots collecting email addresses from your
site, included is a method to add mailto links to the text being
generated.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PEAR::HTML_Crypt dostarcza metody szyfrowania tekstu, który może być
potem rozszyfrowany przy użyciu JavaScriptu po stronie klienta. Jest
to użyteczne aby nie pozwolić robotom spamowym zbierać adresy mailowe
z twojej strony, włączając w to dodawanie linków mailto do
generowanego tekstu.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
