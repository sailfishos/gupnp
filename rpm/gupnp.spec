Name:          gupnp
Version:       0.20.10
Release:       1%{?dist}
Summary:       A framework for creating UPnP devices & control points

Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       http://download.gnome.org/sources/%{name}/0.20/%{name}-%{version}.tar.xz

BuildRequires: gssdp-devel >= 0.14.0
BuildRequires: gnome-common
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: libuuid-devel
BuildRequires: pkgconfig(connman)
Requires: dbus

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

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
%{_bindir}/gupnp-binding-tool

%files devel
%{_libdir}/pkgconfig/gupnp-1.0.pc
%{_libdir}/libgupnp-1.0.so
%{_includedir}/gupnp-1.0
