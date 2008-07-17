%define		_class		XML
%define		_subclass	RPC2
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML-RPC client/server library
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	%mkrel 2
License:	LGPL
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_RPC2/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Requires(post):	php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	dos2unix
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
XML_RPC2 is a pear package providing XML_RPC client and server services. 
XML-RPC is a simple remote procedure call protocol built using HTTP as 
transport and XML as encoding.

As a client library, XML_RPC2 is capable of creating a proxy class which 
exposes the methods exported by the server. As a server library, XML_RPC2 
is capable of exposing methods from a class or object instance, seamlessly 
exporting local methods as remotely callable procedures.

%prep
%setup -qc

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/{Backend/{Php/Value,Xmlrpcext},Server/CallHandler,Util}

install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Backend/Php/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Backend/Php
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Backend/Php/Value/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Backend/Php/Value
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Backend/Xmlrpcext/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Backend/Xmlrpcext
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Server/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Server
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Server/CallHandler/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Server/CallHandler
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Util/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Util

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Backend
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Backend/Php
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Backend/Php/Value
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Backend/Xmlrpcext
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Server
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Server/CallHandler
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Util

%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Backend/Php/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Backend/Php/Value/*php
%{_datadir}/pear/%{_class}/%{_subclass}/Backend/Xmlrpcext/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Server/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Server/CallHandler/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Util/*.php
%{_datadir}/pear/packages/%{_pearname}.xml
