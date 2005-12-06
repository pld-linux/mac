%define		_ver	3.99-u4-b4
Summary:	Monkey's Audio Codec, a lossless audio codec
Summary(pl):	Monkey's Audio Codec - bezstratny kodek d¼wiêku
Name:		mac
Version:	3.99.u4.b4
Release:	1
License:	Distributable with author's permission
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mac-port/%{name}-%{_ver}.tar.gz
# NoSource0-md5:	7eab2b9cc4bb696452d6c147976294b5
NoSource:	0
URL:		http://sourceforge.net/projects/mac-port/
BuildRequires:	libstdc++-devel
BuildRequires:	nasm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MAC: short for Monkey's Audio Codec, a lossless audio codec (almost
always with the .ape extension).

%description -l pl
MAC: skrót Monkey's Audio Codec, bezstratny kodek d¼wiêku (prawie
zawsze z rozszerzeniem .ape).

%package devel
Summary:	MAC header files
Summary(pl):	Pliki nag³ówkowe MAC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
MAC header files.

%description devel -l pl
Pliki nag³ówkowe MAC.

%package static
Summary:	Static MAC libraries
Summary(pl):	Biblioteki statyczne MAC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MAC libraries.

%description static -l pl
Biblioteki statyczne MAC.

%prep
%setup -q -n %{name}-%{_ver}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO src/{Credits.txt,History.txt,License.htm,Readme.htm}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
