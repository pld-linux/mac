%define		_ver	3.99-u4-b2
Summary:	Monkey's Audio Codec, a lossless audio codec
Summary(pl):	Monkey's Audio Codec, bezstratny kodek d¼wiêku
Name:		mac
Version:	3.99.u4.b2
Release:	1
License:	Distributable with author's permission
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mac-port/%{name}-%{_ver}.tar.gz
# NoSource0-md5:	d4a9a357d9300f585848efab584d046f
Patch0:		%{name}-shared.patch
URL:		http://sourceforge.net/projects/mac-port/
BuildRequires:	libstdc++-devel
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
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
