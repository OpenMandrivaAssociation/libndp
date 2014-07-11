%define major 0
%define libname %mklibname ndp %{major}
%define devname %mklibname ndp -d

Summary:	Library for Neighbor Discovery Protocol
Name:		libndp
Version:	1.3
Release:	2
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://www.libndp.org/
Source0:	http://www.libndp.org/files/%{name}-%{version}.tar.gz

%description
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

#----------------------------------------------------------------------------

%package -n ndptool
Summary:	Tool for sending and receiving ndp messages
Group:		Networking/Other

%description -n ndptool
Tool for sending and receiving NDP messages.

%files -n ndptool
%{_bindir}/ndptool
%{_mandir}/man8/ndptool.8*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for Neighbor Discovery Protocol
Group:		System/Libraries

%description -n %{libname}
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

%files -n %{libname}
%{_libdir}/libndp.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and header files for libndp development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	ndp-devel = %{EVRD}

%description -n %{devname}
The libndp-devel package contains the header files and libraries
necessary for developing programs using libndp.

%files -n %{devname}
%{_includedir}/ndp.h
%{_libdir}/libndp.so
%{_libdir}/pkgconfig/libndp.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

