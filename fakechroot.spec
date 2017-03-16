#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fakechroot
Version  : 2.19
Release  : 2
URL      : https://github.com/dex4er/fakechroot/archive/2.19.tar.gz
Source0  : https://github.com/dex4er/fakechroot/archive/2.19.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: fakechroot-bin
Requires: fakechroot-lib
Requires: fakechroot-doc
Requires: util-linux
BuildRequires : util-linux

%description
![logo](http://fakechroot.alioth.debian.org/img/fakechroot_logo.png)
---
**Home** | [Download](https://github.com/fakechroot/fakechroot/wiki/Download) | [Documentation](https://github.com/fakechroot/fakechroot/blob/master/man/fakechroot.pod) | [ChangeLog](https://github.com/fakechroot/fakechroot/blob/master/NEWS.md) | [Development](https://github.com/fakechroot/fakechroot/wiki/Development) | [ToDo](https://github.com/fakechroot/fakechroot/wiki/Todo) | [Links](https://github.com/fakechroot/fakechroot/wiki/Links)

%package bin
Summary: bin components for the fakechroot package.
Group: Binaries

%description bin
bin components for the fakechroot package.


%package doc
Summary: doc components for the fakechroot package.
Group: Documentation

%description doc
doc components for the fakechroot package.


%package lib
Summary: lib components for the fakechroot package.
Group: Libraries

%description lib
lib components for the fakechroot package.


%prep
%setup -q -n fakechroot-2.19

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489626526
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1489626526
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chroot.fakechroot
/usr/bin/env.fakechroot
/usr/bin/fakechroot
/usr/bin/ldd.fakechroot

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/fakechroot/libfakechroot.so
