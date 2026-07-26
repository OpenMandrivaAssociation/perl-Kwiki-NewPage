%define upstream_name	 Kwiki-NewPage
Name:		perl-%{upstream_name}
Version:	0.12
Release:	6

Summary:	Kwiki New Page Plugin
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Kwiki-NewPage
Source0:	https://cpan.metacpan.org/authors/id/I/IN/INGY/Kwiki-NewPage-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
Adds a navigation link/button to create a new page without first adding a link
to that page.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 403381
- rebuild using %0.12 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.12-6mdv2009.0
+ Revision: 257467
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.12-5mdv2009.0
+ Revision: 245428
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.12-3mdv2008.1
+ Revision: 122824
- kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-3mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-2mdk
- better sources URL
- better buildrequires syntax

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdk 
- first mandriva release

