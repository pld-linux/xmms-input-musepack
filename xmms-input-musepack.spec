Summary:	This is an input plugin for XMMS which plays MP+ encoded audio files
Summary(pl):	Wtyczka wej�ciowa dla XMMS-a odtwarzaj�cy pliki MP+ (MPC)
Name:		xmms-input-musepack
Version:	1.2
%define	_RC RC1
Release:	0.%{_RC}.1
License:	LGPL
Group:		X11/Applications/Sound
Source0:	http://files.musepack.net/linux/plugins/xmms-musepack-%{version}-%{_RC}.tar.bz2
# Source0-md5:	db3d2988fc76e1976b9d4921d4bbc3cd
URL:		http://www.musepack.net/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	sed >= 4.0
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
This plugin for XMMS can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes MPC, MP+ or MPP.

%description -l pl
Ta wtyczka XMMS-a odtwarza pliki d�wi�kowe zakodowane koderem Musepack
autorstwa Andree Buschmanna. Te pliki maj� rozszerzenie MPC, MP+ lub
MPP.

%prep
%setup -q -n xmms-musepack-%{version}-%{_RC}

sed -i -e '/-O3 -fomit-frame-pointer/d' configure

%build
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
%attr(755,root,root) %{xmms_input_plugindir}/*.so
