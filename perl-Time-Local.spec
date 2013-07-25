%define upstream_name    Time-Local
%define upstream_version 1.2300

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.2300
Release:	1

Summary:	Implements timelocal() and timegm()
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Time/Time-Local-1.2300.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides functions that are the inverse of built-in perl
functions 'localtime()' and 'gmtime()'. They accept a date as a six-element
array, and return the corresponding 'time(2)' value in seconds since the
system epoch (Midnight, January 1, 1970 GMT on Unix, for example). This
value can be positive or negative, though POSIX only requires support for
positive values, so dates before the system's epoch may not work on all
operating systems.

It is worth drawing particular attention to the expected ranges for the
values provided. The value for the day of the month is the actual day (ie
1..31), while the month is the number of months since January (0..11). This
is consistent with the values returned from 'localtime()' and 'gmtime()'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.200.0-2mdv2011.0
+ Revision: 657475
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.200.0-1
+ Revision: 638971
- update to new version 1.2000

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.190.100-1mdv2011.0
+ Revision: 395226
- import perl-Time-Local


* Sun Jul 12 2009 cpan2dist 1.1901-1mdv
- initial mdv release, generated with cpan2dist

