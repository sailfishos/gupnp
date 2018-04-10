Name:          gupnp
Version:       1.0.1
Release:       1%{?dist}
Summary:       A framework for creating UPnP devices & control points

Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       http://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.xz

BuildRequires: gssdp-devel >= 0.14.5
BuildRequires: gobject-introspection-devel >= 1.36
BuildRequires: vala-devel
BuildRequires: vala-tools
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: libuuid-devel
BuildRequires: pkgconfig(connman)
Requires: dbus

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible.
Test for JB#40554
Touch 1

%package devel
Summary: Development package for gupnp
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gssdp-devel
Requires: libsoup-devel
Requires: libxml2-devel
Requires: libuuid-devel
Requires: pkgconfig

%description devel
Files for development with %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%autogen --disable-static --with-context-manager=connman
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-1.0.so.*
%{_libdir}/girepository-1.0/GUPnP-1.0.typelib

%files devel
%{_bindir}/gupnp-binding-tool
%{_libdir}/pkgconfig/gupnp-1.0.pc
%{_libdir}/libgupnp-1.0.so
%{_includedir}/gupnp-1.0
%{_datadir}/gir-1.0/GUPnP-1.0.gir
%{_datadir}/vala/vapi/gupnp-1.0.deps
%{_datadir}/vala/vapi/gupnp-1.0.vapi
