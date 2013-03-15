%define		_class		XML
%define		_subclass	RPC2
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	3
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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean


fi

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2012.0
+ Revision: 742308
- fix major breakage by careless packager

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1
+ Revision: 741271
- 1.1.1

* Sat Apr 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.8-1
+ Revision: 652038
- update to new version 1.0.8

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 602112
- new version

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.5-3mdv2010.1
+ Revision: 464960
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2010.0
+ Revision: 441762
- rebuild

* Sun Sep 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 284744
- update to new version 1.0.5

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2009.0
+ Revision: 237167
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 10 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 61016
- new version

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2008.0
+ Revision: 15757
- 1.0.1


* Wed Feb 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2007.0
+ Revision: 117277
- Import php-pear-XML_RPC2

