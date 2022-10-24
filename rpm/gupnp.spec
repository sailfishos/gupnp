Name:          gupnp
Version:       1.3.0
Release:       1%{?dist}
Summary:       A framework for creating UPnP devices & control points

License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       %{name}-%{version}.tar.xz
Patch0:        0001-Completely-disable-doc-generation-because-we-dont-ha.patch
BuildRequires: pkgconfig
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gssdp-1.2)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(connman)

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

%package devel
Summary: Development package for gupnp
Requires: %{name} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dcontext_manager=connman -Dexamples=false
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libgupnp-*.so.*
%{_libdir}/girepository-1.0/GUPnP-*.typelib

%files devel
%{_bindir}/gupnp-binding-tool-*
%{_libdir}/pkgconfig/gupnp-*.pc
%{_libdir}/libgupnp-*.so
%{_includedir}/gupnp-*
%{_datadir}/gir-1.0/GUPnP-*.gir
%{_datadir}/vala/vapi/gupnp-*.deps
%{_datadir}/vala/vapi/gupnp-*.vapi
