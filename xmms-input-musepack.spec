Summary:	This is an input plugin for XMMS which plays MP+ encoded audio files
Summary(pl):	Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±cy pliki MP+ (MPC)
Name:		xmms-input-musepack
Version:	1.00
Release:	1
License:	LGPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/mpegplus/xmms-musepack-%{version}.tar.gz
# Source0-md5:	086faea9707911b90dde6291176e9a08
Patch0:		%{name}-Makefile.patch
URL:		http://sourceforge.net/projects/mpegplus/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
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
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}

install xmms-musepack-%{version}.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README_mpc-plugin_english.txt
%doc %lang(de) README_mpc-plugin_german.txt
%doc %lang(es) README_mpc-plugin_spanish.txt
%doc %lang(fi) README_mpc-plugin_finnish.txt
%doc %lang(ko) README_mpc-plugin_korean.txt
%attr(755,root,root) %{xmms_input_plugindir}/*
