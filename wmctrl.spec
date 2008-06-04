Summary:	wmctrl - a command line tool to interact with an EWMH/NetWM compatible X Window Managers
Summary(pl.UTF-8):	wmtrl - tekstowe narzędzie do interakcji z zarządcami okien kompatybilnymi z EWMH/NetWM
Name:		wmctrl
Version:	1.07
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Tomas Styblo <tripie@cpan.org>
Source0:	http://sweb.cz/tripie/utils/wmctrl/dist/%{name}-%{version}.tar.gz
# Source0-md5:	1fe3c7a2caa6071e071ba34f587e1555
URL:		http://sweb.cz/tripie/utils/wmctrl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It provides command line access to almost all the features defined in
the EWMH specification. Using it, it's possible to, for example,
obtain information about the window manager, get a detailed list of
desktops and managed windows, switch and resize desktops, change
number of desktops, make windows full-screen, always-above or sticky,
and activate, close, move, resize, maximize and minimize them.

The command line access makes it easy to automate these tasks and
execute them from any application that is able to run a command in
response to some event.

Please note that wmctrl only works with window managers which
implement this specification.

%description -l pl.UTF-8
wmctrl dostarcza narzędzie umożliwiające dostęp do większości
właściwości zdefiniowanych w specyfikacji EWMH. Używając go jest
możliwe (na przykład) uzyskanie informacji o zarządcy okien,
pobranie szczegółowej listy pulpitów i okien, przełączanie się i
zmienianie rozmiarów pulpitów, zmienianie nazw pulpitów, powiększanie
okien, ich aktywacja, zamykanie, przesuwanie i minimalizowanie.

Dostęp z poziomu wiersza poleceń pozwala na łatwą automatyzację tych
zadań i wykonywanie ich z poziomu dowolnej aplikacji, która potrafi
uruchamiać polecenia w wyniku jakichś zdarzeń.

Należy zauważyć, że wmctrl działa tylko w tych zarządcach okien, które
stosują się do specyfikacji.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/wmctrl
%{_mandir}/man1/wmctrl.1*
