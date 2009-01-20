%define 	modulename pam_usb
Summary:	A PAM module that provides hardware authentication using USB Flash Drives
Name:		pam-%{modulename}
Version:	0.4.2
Release:	1
License:	LGPL
Group:		Base
Source0:	http://dl.sourceforge.net/pamusb/%{modulename}-%{version}.tar.gz
# Source0-md5:	2320b752dd0b030dfbb0a3935e7dc899
URL:		http://pamusb.org/
BuildRequires:	hal-devel
Requires:	hal
Requires:	pmount
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A PAM module that provides hardware authentication using USB Flash Drives.

%prep
%setup -q -n %{modulename}-%{version}

%build
CFLAGS="%{rpmcflags} -DPUSB_CONF_FILE=\"/etc/security/pamusb.conf\"" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{_docdir}/pamusb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/CONFIGURATION doc/FAQ doc/QUICKSTART doc/UPGRADING
%attr(755,root,root) /%{_lib}/security/pam_usb.so
%attr(755,root,root) %{_bindir}/pamusb-*
%config(noreplace) %verify(not md5 mtime size) /etc/pamusb.conf
%{_mandir}/man1/pamusb-*
