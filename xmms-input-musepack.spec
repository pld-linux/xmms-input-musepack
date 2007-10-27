Summary:	This is an input plugin for XMMS which plays MP+ encoded audio files
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzający pliki MP+ (MPC)
Name:		xmms-input-musepack
Version:	1.2.1
Release:	3
License:	BSD
Group:		X11/Applications/Sound
Source0:	http://files.musepack.net/linux/plugins/xmms-musepack-%{version}.tar.bz2
# Source0-md5:	d9d5ee7720d39f466ea71f4a7a285e83
URL:		http://www.musepack.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib-devel >= 1:1.2.10
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libmpcdec-devel >= 1.2.6
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	sed >= 4.0
BuildRequires:	taglib-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
This plugin for XMMS can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes MPC, MP+ or MPP.

%description -l pl.UTF-8
Ta wtyczka XMMS-a odtwarza pliki dźwiękowe zakodowane koderem Musepack
autorstwa Andree Buschmanna. Te pliki mają rozszerzenie MPC, MP+ lub
MPP.

%prep
%setup -q -n xmms-musepack-%{version}

sed -i -e '/-O3 -fomit-frame-pointer/d' configure.ac
chmod +x configure

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{xmms_input_plugindir}/*.so
