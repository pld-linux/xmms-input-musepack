Summary:	This is an input plugin for XMMS which plays mp+ encoded audio files.
Summary(pl):	Plugin wej¶ciowy do XMMS odtwarzaj±cy pliki mp+ (mpc).
Name:		xmms-input-musepack
Version:	0.94
Release:	1
License:	LGPL
Group:		X11/Applications/Multimedia
Source:		http://telia.dl.sourceforge.net/sourceforge/mpegplus/xmms-musepack-%{version}.tar.bz2
URL:		http://sourceforge.net/project/mpegplus/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define     _prefix     /usr/X11R6

%description
This plugin for XMMS can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes mpc, mp+ or mpp.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n xmms-musepack-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xmms/Input/
install -s xmms-musepack-%{version}.so $RPM_BUILD_ROOT%{_libdir}/xmms/Input/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README_mpp-plugin_eng.txt
%attr(755,root,root) %{_libdir}/xmms/Input/* 
