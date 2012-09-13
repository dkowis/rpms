%define version 2012.09.07

Name: pianobar
Version: %{version}
Release: 1%{?dist}
Summary: "pianobar" is a free/open-source, console-based replacement for pandora's flash player.

Group: Applications/Multimedia
License: AS-IS
URL: http://6xq.net/projects/pianobar/
Source0: http://6xq.net/projects/pianobar/pianobar-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: make, libao-devel, gnutls-devel, libgcrypt-devel, json-c-devel,  faad2-libs, libmad-devel
Requires: libao, faad2-libs, gnutls, libgcrypt, json-c, libmad

%description
Pianobar is a free/open-source, console-based client for the personalized online radio Pandora
 * play and manage (create, add more music, delete, rename, ...) stations
 * rate songs and explain why they have been selected
 * upcoming songs/song history
 * customize keybindings and text output
 * remote control and eventcmd interface (send tracks to last.fm, for example)
 * proxy support for listeners outside the USA

%build
gmake
gmake VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
gmake install PREFIX=usr DESTDIR=$RPM_BUILD_ROOT

%check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
