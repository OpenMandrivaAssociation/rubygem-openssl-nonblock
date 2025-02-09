# Generated from openssl-nonblock-0.2.1.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	openssl-nonblock

Summary:	Non-blocking support for Ruby OpenSSL
Name:		rubygem-%{rbname}

Version:	0.2.1
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://rev.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	openssl-devel

%description
Non-blocking support for Ruby OpenSSL

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/openssl
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/openssl/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so


%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.1-2
+ Revision: 774513
- drop build dependency on rake as it's now provided by ruby's standard library
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.1-1
+ Revision: 767170
- BR:openssl-devel
- imported package rubygem-openssl-nonblock

