Summary:	This is an input plugin for XMMS which plays MP+ encoded audio files
Summary(pl):	Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±cy pliki MP+ (MPC)
Name:		xmms-input-musepack
Version:	1.1
Release:	1
License:	LGPL
Group:		X11/Applications/Sound
Source0:	http://www.saunalahti.fi/grimmel/musepack.net/linux/plugins/xmms-musepack-%{version}.tar.bz2
# Source0-md5:	8aed0b02562ee3913b5fd058d2c14ccf
URL:		http://sourceforge.net/projects/mpegplus/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRequires:	libmusepack-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin for XMMS can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes MPC, MP+ or MPP.

%description -l pl
Ta wtyczka XMMS-a odtwarza pliki d¼wiêkowe zakodowane koderem Musepack
autorstwa Andree Buschmanna. Te pliki maj± rozszerzenie MPC, MP+ lub
MPP.

%prep
%setup -q -n xmms-musepack-%{version}

%build

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_input_plugindir}/*
