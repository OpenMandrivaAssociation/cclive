Name:		cclive
Version:	0.7.9
Release:	2
Summary:	A tool for downloading media from YouTube and similar websites
License:	GPLv3
URL:		http://cclive.sourceforge.net/
Group:		Networking/WWW
Source0:	http://sourceforge.net/projects/cclive/files/0.7/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libquvi)
BuildRequires:	pcre-devel
BuildRequires:	curl-devel
BuildRequires:	boost-devel

%description
A tool for downloading media from YouTube and similar websites.
It has a low memory footprint compared to other existing tools.

Features:
- Retries interrupted downloads automatically
- Runs as a background process if preferred
- Use video ID, title, etc. in filenames
- Supports many (40+) websites, see quvi
- Configuration file support
- Bandwidth throttle

%prep
%setup -q

%build
%configure2_5x

%install
%makeinstall_std

%files
%doc README NEWS COPYING ChangeLog
%{_bindir}/%{name}
%{_mandir}/*/%{name}.*

