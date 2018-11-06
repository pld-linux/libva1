Summary:	VAAPI (Video Acceleration API)
Summary(pl.UTF-8):	VAAPI (Video Acceleration API) - API akceleracji filmów
Name:		libva1
Version:	1.8.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://www.freedesktop.org/software/vaapi/releases/libva/libva-%{version}.tar.bz2
# Source0-md5:	2ce6901495b64f4cc26dd0fb53eb5b14
URL:		https://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
# wayland-client
BuildRequires:	wayland-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main motivation for VAAPI (Video Acceleration API) is to enable
hardware accelerated video decode/encode at various entry-points (VLD,
IDCT, Motion Compensation etc.) for the prevailing coding standards
today (MPEG-2, MPEG-4 ASP/H.263, MPEG-4 AVC/H.264, and VC-1/VMW3).

%description -l pl.UTF-8
Głównym celem API akceleracji filmów VAAPI (Video Acceleration API)
jest umożliwienie sprzętowej akceleracji dekodowania/kodowania filmów
na różnych etapach (VLD, IDCT, kompensacja ruchu itp.) dla obecnie
przeważających standardów kodowania (MPEG-2, MPEG-4 ASP/H.263, MPEG-4
AVC/H.264, VC-1/VMW3).

%package drm
Summary:	VAAPI - DRM interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu DRM
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdrm >= 2.4

%description drm
VAAPI - DRM interface library.

%description drm -l pl.UTF-8
VAAPI - biblioteka interfejsu DRM.

%package egl
Summary:	VAAPI - EGL interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu EGL
Group:		Libraries
Requires:	%{name}-x11 = %{version}-%{release}

%description egl
VAAPI - EGL interface library.

%description egl -l pl.UTF-8
VAAPI - biblioteka interfejsu EGL.

%package glx
Summary:	VAAPI - GLX interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu GLX
Group:		Libraries
Requires:	%{name}-x11 = %{version}-%{release}

%description glx
VAAPI - GLX interface library.

%description glx -l pl.UTF-8
VAAPI - biblioteka interfejsu GLX.

%package wayland
Summary:	VAAPI - Wayland interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu Wayland
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wayland >= 1.0.0

%description wayland
VAAPI - Wayland interface library.

%description wayland -l pl.UTF-8
VAAPI - biblioteka interfejsu Wayland.

%package x11
Summary:	VAAPI - X11 interface library
Summary(pl.UTF-8):	VAAPI - biblioteka interfejsu X11
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdrm >= 2.4

%description x11
VAAPI - X11 interface library.

%description x11 -l pl.UTF-8
VAAPI - biblioteka interfejsu X11.

%prep
%setup -q -n libva-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-drivers-path=%{_libdir}/%{name}/dri

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{%{name}/dri/*.la,libva*.la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	drm -p /sbin/ldconfig
%postun	drm -p /sbin/ldconfig

%post	egl -p /sbin/ldconfig
%postun	egl -p /sbin/ldconfig

%post	glx -p /sbin/ldconfig
%postun	glx -p /sbin/ldconfig

%post	wayland -p /sbin/ldconfig
%postun	wayland -p /sbin/ldconfig

%post	x11 -p /sbin/ldconfig
%postun	x11 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_libdir}/libva.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva.so.1
%attr(755,root,root) %{_libdir}/libva-tpi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-tpi.so.1
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dri
%attr(755,root,root) %{_libdir}/%{name}/dri/dummy_drv_video.so

%files drm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-drm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-drm.so.1

%files egl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-egl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-egl.so.1

%files glx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-glx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-glx.so.1

%files wayland
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-wayland.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-wayland.so.1

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-x11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libva-x11.so.1
