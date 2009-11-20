Summary:	VAAPI (Video Acceleration API)
Name:		libva
# see configure.ac
Version:	0.31
Release:	1
License:	BSD
Group:		Libraries
# git clone git://anongit.freedesktop.org/git/libva
Source0:	%{name}-20091120.tar.bz2
# Source0-md5:	4ed2e4e6f1293f1405a847f17a42c9fa
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main motivation for VAAPI (Video Acceleration API) is to enable
hardware accelerated video decode/encode at various entry-points (VLD,
IDCT, Motion Compensation etc.) for the prevailing coding standards
today (MPEG-2, MPEG-4 ASP/H.263, MPEG-4 AVC/H.264, and VC-1/VMW3).

%package devel
Summary:	Header files and develpment documentation for libva
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and documentation for libva.

%package static
Summary:	Static libva library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libva library.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure \
	--enable-static \
	--enable-i965-driver \
	--with-drivers-path=%{_libdir}/%{name}/dri

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vainfo
%attr(755,root,root) %{_libdir}/libva*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libva*.so.1
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dri
%attr(755,root,root) %{_libdir}/%{name}/dri/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva*.so
%{_includedir}/va
%{_libdir}/libva*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libva*.a
