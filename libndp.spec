# Used by NetworkManager, which in turn is used by steam
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 0
%define oldlibname %mklibname ndp 0
%define libname %mklibname ndp
%define devname %mklibname ndp -d

%define lib32name %mklib32name ndp
%define dev32name %mklib32name ndp -d

Summary:	Library for Neighbor Discovery Protocol
Name:		libndp
Version:	1.9
Release:	1
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://www.libndp.org/
Source0:	https://github.com/jpirko/libndp/archive/v%{version}.tar.gz
BuildRequires:	autoconf automake
%if %{with compat32}
BuildRequires:	libc6
%endif

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
%rename %{oldlibname}

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

%if 0
# lib32name == name
%package -n %{lib32name}
Summary:	32-Bit Library for Neighbor Discovery Protocol
Group:		System/Libraries

%description -n %{lib32name}
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.
%endif

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libndp.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n %{dev32name}
Summary:	32-Bit Libraries and header files for libndp development
Group:		Development/C
Requires:	%{lib32name} = %{EVRD}
Requires:	%{devname} = %{EVRD}

%description -n %{dev32name}
The libndp-devel package contains the header files and libraries
necessary for developing programs using libndp.

%if %{with compat32}
%files -n %{dev32name}
%{_prefix}/lib/libndp.so
%{_prefix}/lib/pkgconfig/libndp.pc
%endif

#----------------------------------------------------------------------------

%prep
%autosetup -p1
./autogen.sh
export CONFIGURE_TOP=`pwd`

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
