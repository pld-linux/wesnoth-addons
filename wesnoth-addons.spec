Summary:	Additional stuffs (maps, scenarios, eras, campaigns) for Wesnoth
Summary(hu.UTF-8):	Bővítések Wesnoth-hoz (térképek, küldetések, korok)
Name:		wesnoth-addons
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
# 0-49: multiplayers
# 50-99: campaigns
Source0:	http://files.wesnoth.org/addons/1.4/Temples_Of_The_Nagas.tar.bz2
# Source0-md5:	642d90907ecfb5d9aa29625a68e6b3e8
Source50:	http://files.wesnoth.org/addons/1.4/Flight_Freedom_1_3.tar.bz2
# Source50-md5:	cbf9d0a47784a04224a2b1225517d601
Source51:	http://files.wesnoth.org/addons/1.4/Dead_Water.tar.bz2
# Source51-md5:	f50c5a1683a95cdb94680d649fc1e65d
Source52:	http://files.wesnoth.org/addons/1.4/Elvish_Legacy.tar.bz2
# Source52-md5:	e3cabb85cd9399141336fe75cdf9d42b
URL:		http://www.wesnoth.org/addons/1.4/
Requires:	wesnoth >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define wesnothdir %{_datadir}/wesnoth/data
%define wesnothmulti %{wesnothdir}/multiplayer
%define wesnothcamp %{wesnothdir}/campaigns

%description
Additional stuffs (maps, scenarios, eras,campaigns) for Wesnoth.

%description -l hu.UTF-8
Bővítések Wesnoth-hoz (térképek, küldetések, korok).

%package mp-totn
Summary:	Temples of the Nagas is a team based MP survival game designed for four players
Summary(hu.UTF-8):	A Temples of the Nagas egy csapat alapú MP túlélő játék négy játékosra
Group:		X11/Applications/Games

%description mp-totn
Temples of the Nagas is a team based MP survival game designed for
four players.

%description mp-totn -l hu.UTF-8
A Temples of the Nagas egy csapat alapú MP túlélő játék négy
játékosra.

%package camp-flight_to_freedom
Summary:	Flight to Freedom chronicles the story of the drake hero Malakar
Summary(hu.UTF-8):	Flight to Freedom Malakar sárkány hős krónikáit meséli el
Group:		X11/Applications/Games

%description camp-flight_to_freedom
Flight to Freedom chronicles the story of the drake hero Malakar. Lead
him and his Drake tribe to freedom from humanity's slavery!

%description camp-flight_to_freedom -l hu.UTF-8
Flight to Freedom Malakar sárkány hős krónikáit meséli el. Vezesd őt
és a sárkányai megalapítják a szabadságot az emberek rabszolgása után!

%package camp-dead_water
Summary:	Lead your merfolk on a mission to convince a powerful mermaid to help you repel an undead invasion
Summary(hu.UTF-8):	Vezesd a sellő népet egy élőhalott invázió ellen
Group:		X11/Applications/Games

%description camp-dead_water
Lead your merfolk on a mission to convince a powerful mermaid to help
you repel an undead invasion.

%description camp-dead_water -l hu.UTF-8
Vezesd a sellő népet egy élőhalott invázió ellen.

%package camp-elvish_legacy
Summary:	You must defend your people from orcish raids
Summary(hu.UTF-8):	Meg kell védened az embereid az orkoktól
Group:		X11/Applications/Games

%description camp-elvish_legacy
You must defend your people from orcish raids.

%description camp-elvish_legacy -l hu.UTF-8
Meg kell védened az embereid az orkoktól.


%prep
install -d wesnoth-addons
cd wesnoth-addons
%{__tar} xf %{SOURCE0}

%{__tar} xf %{SOURCE50}
%{__tar} xf %{SOURCE51}
%{__tar} xf %{SOURCE52}

find -name COPYING.txt -exec rm {} \;

%build

%install
rm -rf $RPM_BUILD_ROOT
cd wesnoth-addons
install -d $RPM_BUILD_ROOT/%{wesnothmulti}
install -d $RPM_BUILD_ROOT/%{wesnothcamp}

%{__cp} -r Temples_Of_The_Nagas $RPM_BUILD_ROOT%{wesnothmulti}

%{__cp} -r Flight_Freedom_1_3 $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Dead_Water $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Elvish_Legacy $RPM_BUILD_ROOT%{wesnothcamp}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{wesnothdir}

%files mp-totn
%defattr(644,root,root,755)
%{wesnothmulti}/Temples_Of_The_Nagas

%files camp-flight_to_freedom
%defattr(644,root,root,755)
%{wesnothcamp}/Flight_Freedom_1_3

%files camp-dead_water
%defattr(644,root,root,755)
%{wesnothcamp}/Dead_Water

%files camp-elvish_legacy
%defattr(644,root,root,755)
%{wesnothcamp}/Elvish_Legacy
