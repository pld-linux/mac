%define		_ver	3.99-u4-b5
Summary:	Monkey's Audio Codec, a lossless audio codec
Summary(pl):	Monkey's Audio Codec - bezstratny kodek d¼wiêku
Name:		mac
Version:	3.99.u4.b5
Release:	1
License:	Distributable with author's permission
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mac-port/%{name}-%{_ver}.tar.gz
# NoSource0-md5:	75716b342e07deae58f56a2522362006
NoSource:	0
URL:		http://sourceforge.net/projects/mac-port/
BuildRequires:	libstdc++-devel
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm
%endif
BuildRequires:	sed >= 4.0
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

sed -i -e 's/-O3 //' configure

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
%attr(755,root,root) %{_bindir}/mac
%attr(755,root,root) %{_libdir}/libmac.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmac.so
%{_libdir}/libmac.la
%{_includedir}/mac

%files static
%defattr(644,root,root,755)
%{_libdir}/libmac.a
