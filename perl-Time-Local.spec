%define upstream_name    Time-Local
%define upstream_version 1.2000

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Implements timelocal() and timegm()
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


