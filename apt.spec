%define version 0.9.7.7.1
Summary: APT - Another packaging tool
Name: apt
Version: %{version}
Release: el6.1
Source0: apt-%{version}.tar.gz
License: GPL
Group: System Environment/Libraries
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ncurses,curl,zlib,db4
BuildRequires: ncurses-devel,curl-devel,zlib-devel,db4-devel
%description
Debian package management tool
%prep
%setup -q
%build
mkdir -p build
echo "running autoconf"
autoconf -f
echo "running configure"
( cd build && ../configure --prefix=/usr --prefix=/etc --bindir=/bin --libdir=/lib )
echo "buid and install"
( cd build && make )
%install
( cd build && make DESTDIR=$RPM_BUILD_ROOT install )
%clean
rm -Rf build
%files
%defattr(-,root,root)
/bin/apt-cache
/bin/apt-cdrom
/bin/apt-config
/bin/apt-get
/bin/apt-key
/bin/apt-mark
/lib/libapt-inst.so
/lib/libapt-pkg.so
/lib/libapt-pkg.so.4.12
/lib/libapt-pkg.so.4.12.0
/usr/lib/apt/methods/bzip2
/usr/lib/apt/methods/cdrom
/usr/lib/apt/methods/copy
/usr/lib/apt/methods/file
/usr/lib/apt/methods/ftp
/usr/lib/apt/methods/gpgv
/usr/lib/apt/methods/gzip
/usr/lib/apt/methods/http
/usr/lib/apt/methods/https
/usr/lib/apt/methods/lzma
/usr/lib/apt/methods/mirror
/usr/lib/apt/methods/rred
/usr/lib/apt/methods/rsh
/usr/lib/apt/methods/ssh
/usr/lib/apt/methods/xz
/usr/lib/dpkg/methods/apt/desc.apt
/usr/lib/dpkg/methods/apt/install
/usr/lib/dpkg/methods/apt/names
/usr/lib/dpkg/methods/apt/setup
/usr/lib/dpkg/methods/apt/update
/usr/share/locale/ar/LC_MESSAGES/apt.mo
/usr/share/locale/ar/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ast/LC_MESSAGES/apt.mo
/usr/share/locale/ast/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/bg/LC_MESSAGES/apt.mo
/usr/share/locale/bg/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/bs/LC_MESSAGES/apt.mo
/usr/share/locale/bs/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ca/LC_MESSAGES/apt.mo
/usr/share/locale/ca/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/cs/LC_MESSAGES/apt.mo
/usr/share/locale/cs/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/cy/LC_MESSAGES/apt.mo
/usr/share/locale/cy/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/da/LC_MESSAGES/apt.mo
/usr/share/locale/da/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/de/LC_MESSAGES/apt.mo
/usr/share/locale/de/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/dz/LC_MESSAGES/apt.mo
/usr/share/locale/dz/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/el/LC_MESSAGES/apt.mo
/usr/share/locale/el/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/es/LC_MESSAGES/apt.mo
/usr/share/locale/es/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/eu/LC_MESSAGES/apt.mo
/usr/share/locale/eu/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/fi/LC_MESSAGES/apt.mo
/usr/share/locale/fi/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/fr/LC_MESSAGES/apt.mo
/usr/share/locale/fr/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/gl/LC_MESSAGES/apt.mo
/usr/share/locale/gl/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/hu/LC_MESSAGES/apt.mo
/usr/share/locale/hu/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/it/LC_MESSAGES/apt.mo
/usr/share/locale/it/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ja/LC_MESSAGES/apt.mo
/usr/share/locale/ja/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/km/LC_MESSAGES/apt.mo
/usr/share/locale/km/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ko/LC_MESSAGES/apt.mo
/usr/share/locale/ko/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ku/LC_MESSAGES/apt.mo
/usr/share/locale/ku/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/lt/LC_MESSAGES/apt.mo
/usr/share/locale/lt/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/mr/LC_MESSAGES/apt.mo
/usr/share/locale/mr/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/nb/LC_MESSAGES/apt.mo
/usr/share/locale/nb/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ne/LC_MESSAGES/apt.mo
/usr/share/locale/ne/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/nl/LC_MESSAGES/apt.mo
/usr/share/locale/nl/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/nn/LC_MESSAGES/apt.mo
/usr/share/locale/nn/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/pl/LC_MESSAGES/apt.mo
/usr/share/locale/pl/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/pt/LC_MESSAGES/apt.mo
/usr/share/locale/pt/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/pt_BR/LC_MESSAGES/apt.mo
/usr/share/locale/pt_BR/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ro/LC_MESSAGES/apt.mo
/usr/share/locale/ro/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ru/LC_MESSAGES/apt.mo
/usr/share/locale/ru/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/sk/LC_MESSAGES/apt.mo
/usr/share/locale/sk/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/sl/LC_MESSAGES/apt.mo
/usr/share/locale/sl/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/sv/LC_MESSAGES/apt.mo
/usr/share/locale/sv/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/th/LC_MESSAGES/apt.mo
/usr/share/locale/th/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/tl/LC_MESSAGES/apt.mo
/usr/share/locale/tl/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/uk/LC_MESSAGES/apt.mo
/usr/share/locale/uk/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/vi/LC_MESSAGES/apt.mo
/usr/share/locale/vi/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/zh_CN/LC_MESSAGES/apt.mo
/usr/share/locale/zh_CN/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/zh_TW/LC_MESSAGES/apt.mo
/usr/share/locale/zh_TW/LC_MESSAGES/libapt-pkg4.12.mo
/usr/share/locale/ar/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ar/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ast/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ast/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/bg/LC_MESSAGES/apt-utils.mo
/usr/share/locale/bg/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/bs/LC_MESSAGES/apt-utils.mo
/usr/share/locale/bs/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ca/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ca/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/cs/LC_MESSAGES/apt-utils.mo
/usr/share/locale/cs/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/cy/LC_MESSAGES/apt-utils.mo
/usr/share/locale/cy/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/da/LC_MESSAGES/apt-utils.mo
/usr/share/locale/da/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/de/LC_MESSAGES/apt-utils.mo
/usr/share/locale/de/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/dz/LC_MESSAGES/apt-utils.mo
/usr/share/locale/dz/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/el/LC_MESSAGES/apt-utils.mo
/usr/share/locale/el/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/es/LC_MESSAGES/apt-utils.mo
/usr/share/locale/es/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/eu/LC_MESSAGES/apt-utils.mo
/usr/share/locale/eu/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/fi/LC_MESSAGES/apt-utils.mo
/usr/share/locale/fi/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/fr/LC_MESSAGES/apt-utils.mo
/usr/share/locale/fr/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/gl/LC_MESSAGES/apt-utils.mo
/usr/share/locale/gl/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/hu/LC_MESSAGES/apt-utils.mo
/usr/share/locale/hu/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/it/LC_MESSAGES/apt-utils.mo
/usr/share/locale/it/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ja/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ja/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/km/LC_MESSAGES/apt-utils.mo
/usr/share/locale/km/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ko/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ko/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ku/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ku/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/lt/LC_MESSAGES/apt-utils.mo
/usr/share/locale/lt/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/mr/LC_MESSAGES/apt-utils.mo
/usr/share/locale/mr/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/nb/LC_MESSAGES/apt-utils.mo
/usr/share/locale/nb/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ne/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ne/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/nl/LC_MESSAGES/apt-utils.mo
/usr/share/locale/nl/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/nn/LC_MESSAGES/apt-utils.mo
/usr/share/locale/nn/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/pl/LC_MESSAGES/apt-utils.mo
/usr/share/locale/pl/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/pt/LC_MESSAGES/apt-utils.mo
/usr/share/locale/pt/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/pt_BR/LC_MESSAGES/apt-utils.mo
/usr/share/locale/pt_BR/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ro/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ro/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/ru/LC_MESSAGES/apt-utils.mo
/usr/share/locale/ru/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/sk/LC_MESSAGES/apt-utils.mo
/usr/share/locale/sk/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/sl/LC_MESSAGES/apt-utils.mo
/usr/share/locale/sl/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/sv/LC_MESSAGES/apt-utils.mo
/usr/share/locale/sv/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/th/LC_MESSAGES/apt-utils.mo
/usr/share/locale/th/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/tl/LC_MESSAGES/apt-utils.mo
/usr/share/locale/tl/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/uk/LC_MESSAGES/apt-utils.mo
/usr/share/locale/uk/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/vi/LC_MESSAGES/apt-utils.mo
/usr/share/locale/vi/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/zh_CN/LC_MESSAGES/apt-utils.mo
/usr/share/locale/zh_CN/LC_MESSAGES/libapt-inst1.5.mo
/usr/share/locale/zh_TW/LC_MESSAGES/apt-utils.mo
/usr/share/locale/zh_TW/LC_MESSAGES/libapt-inst1.5.mo
%config(noreplace) /etc/apt/apt.conf.d
%config(noreplace) /etc/apt/trusted.gpg.d
%config(noreplace) /etc/apt/preferences.d
%config(noreplace) /etc/apt/sources.list.d
