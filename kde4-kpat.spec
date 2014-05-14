%define		_state		stable
%define		orgname		kpat
%define		qtver		4.8.0

Summary:	KDE solitaire patience game
Summary(pl.UTF-8):	Pasjanse dla KDE
Summary(pt_BR.UTF-8):	Versão do jogo 'Paciência' para o KDE
Name:		kde4-%{orgname}
Version:	4.13.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	1eac1197dedf57ac998905d042bf7cb3
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE solitaire patience games.

%description -l pl.UTF-8
Program dla KDE umożliwiający układanie kilku rodzajów pasjansów.

%description -l pt_BR.UTF-8
Versão do jogo 'Paciência' para o KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%attr(755,root,root) %{_libdir}/libkcardgame.so
%{_desktopdir}/kde4/kpat.desktop
%{_datadir}/apps/kpat
%{_datadir}/config.kcfg/kpat.kcfg
%{_datadir}/config/kcardtheme.knsrc
%{_datadir}/config/kpat.knsrc
%{_datadir}/mime/packages/kpatience.xml
%{_iconsdir}/*/*/apps/kpat.png
