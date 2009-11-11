%define		_class		XML
%define		_subclass	RPC2
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.5
Release:	%mkrel 3
Summary:	XML-RPC client/server library
License:	LGPL
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_RPC2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post):	php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
XML_RPC2 is a pear package providing XML_RPC client and server services. 
XML-RPC is a simple remote procedure call protocol built using HTTP as 
transport and XML as encoding.

As a client library, XML_RPC2 is capable of creating a proxy class which 
exposes the methods exported by the server. As a server library, XML_RPC2 
is capable of exposing methods from a class or object instance, seamlessly 
exporting local methods as remotely callable procedures.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif
fi

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
