Summary:	wmctrl - a command line tool to interact with an EWMH/NetWM compatible X Window Managers
Summary(pl):	wmtrl - tekstowe narzêdzie do interakcji z zarz±dcami okien kompatybilnymi z EWMH/NetWM
Name:		wmctrl
Version:	1.07
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Tomas Styblo <tripie@cpan.org>
Source0:	http://sweb.cz/tripie/utils/wmctrl/dist/%{name}-%{version}.tar.gz
# Source0-md5:	1fe3c7a2caa6071e071ba34f587e1555
URL:		http://sweb.cz/tripie/utils/wmctrl/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig
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

%description -l pl
wmctrl dostarcza narzêdzie umo¿liwiaj±ce dostêp do wiêkszo¶ci
w³a¶ciwo¶ci zdefiniowanych w specyfikacji EWMH. U¿ywaj±c go jest
mo¿liwe (na przyk³ad) uzyskanie informacji o zarz±dcy okien,
pobranie szczegó³owej listy pulpitów i okien, prze³±czanie siê i
zmienianie rozmiarów pulpitów, zmienianie nazw pulpitów, powiêkszanie
okien, ich aktywacja, zamykanie, przesuwanie i minimalizowanie.

Dostêp z poziomu wiersza poleceñ pozwala na ³atw± automatyzacjê tych
zadañ i wykonywanie ich z poziomu dowolnej aplikacji, która potrafi
uruchamiaæ polecenia w wyniku jakich¶ zdarzeñ.

Nale¿y zauwa¿yæ, ¿e wmctrl dzia³a tylko w tych zarz±dcach okien, które
stosuj± siê do specyfikacji.

%prep
%setup -q

%build
rm -f missing aclocal.m4
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
