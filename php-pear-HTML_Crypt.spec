%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Crypt
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Encrypts text which is later decoded using javascript on the client side
Summary(pl):	%{_pearname} - Szyfruje tekst, który jest po stronie klienta rozkodowany javascriptem
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-88
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_Crypt provides methods to encrypt text, which can be
later be decrypted using JavaScript on the client side. This is very
useful to prevent spam robots collecting email addresses from your
site, included is a method to add mailto links to the text being
generated.

%description -l pl
PEAR::HTML_Crypt dostarcza metody szyfrowania tekstu, który mo¿e byæ
potem rozszyfrowany przy u¿yciu JavaScriptu po stronie klienta. Jest
to u¿yteczne aby nie pozwoliæ robotom spamowym zbieraæ adresy mailowe
z twojej strony, w³±czaj±c w to dodawanie linków mailto do
generowanego tekstu.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
