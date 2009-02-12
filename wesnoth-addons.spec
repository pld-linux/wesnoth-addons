%define wesnothver 1.4
Summary:	Additional stuffs (maps, scenarios, eras, campaigns) for Wesnoth
Summary(hu.UTF-8):	Bővítések Wesnoth-hoz (térképek, küldetések, korok)
Name:		wesnoth-addons
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
# 0-49: multiplayers
# 50-99: campaigns
Source0:	http://files.wesnoth.org/addons/%{wesnothver}/Temples_Of_The_Nagas.tar.bz2
# Source0-md5:	642d90907ecfb5d9aa29625a68e6b3e8
Source50:	http://files.wesnoth.org/addons/%{wesnothver}/Flight_Freedom_1_3.tar.bz2
# Source50-md5:	cbf9d0a47784a04224a2b1225517d601
Source51:	http://files.wesnoth.org/addons/%{wesnothver}/Dead_Water.tar.bz2
# Source51-md5:	f50c5a1683a95cdb94680d649fc1e65d
Source52:	http://files.wesnoth.org/addons/%{wesnothver}/Elvish_Legacy.tar.bz2
# Source52-md5:	e3cabb85cd9399141336fe75cdf9d42b
Source53:	http://files.wesnoth.org/addons/%{wesnothver}/Bad_Moon_Rising.tar.bz2
# Source53-md5:	c9c01b5a4d795f8f718b156860a5bae0
Source54:	http://files.wesnoth.org/addons/%{wesnothver}/Forgotten_Kingdom.tar.bz2
# Source54-md5:	3b35f5651eb4bb4d28a1d83b03f632c3
Source55:	http://files.wesnoth.org/addons/%{wesnothver}/Raajal.tar.bz2
# Source55-md5:	2f0fe25ddc5adaf0af1a0c3722c55b72
Source56:	http://files.wesnoth.org/addons/%{wesnothver}/The_Three_Elves.tar.bz2
# Source56-md5:	9c083f06913e56e8de3fa4c0318639d9
Source57:	http://files.wesnoth.org/addons/%{wesnothver}/Trolls.tar.bz2
# Source57-md5:	0ec18cd1bb05e4e50b89bf737bc26584
URL:		http://www.wesnoth.org/addons/1.4/
Requires:	wesnoth >= %{wesnothver}
BuildArch:	noarch
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

%package camp-bad_moon_rising
Summary:	Officer Lorenzon leads a revolution against the brutal Prince
Summary(hu.UTF-8):	Lorenzon kapitány egy lázadást vezet a kegyetlen Herceg ellen
Group:		X11/Applications/Games

%description camp-bad_moon_rising
Officer Lorenzon leads a revolution against the brutal Prince.

%description camp-bad_moon_rising -l hu.UTF-8
Lorenzon kapitány egy lázadást vezet a kegyetlen Herceg ellen.

%package camp-forgotten_kingdom
Summary:	Help Orlog, a troll chieftan
Summary(hu.UTF-8):	Segíts Orlog-nak, egy troll főnöknek
Group:		X11/Applications/Games

%description camp-forgotten_kingdom
Help Orlog, a troll chieftan, lead his people to safety in the
underground and discover an ancient power long forgotten.

%description camp-forgotten_kingdom
Segíts Orlog-nak, a troll főnöknek az embereit biztonságba vezényelni
a föld alatt és felfedezni az ősí erőt, amelyet rég elfeledtek.

%package camp-raajal
Summary:	An Arch Mage with the power of resurrection seeks a new apprentice
Summary(hu.UTF-8):	Egy mágus a feltámasztás erejével egy új tanoncot keres
Group:		X11/Applications/Games

%description camp-raajal
An Arch Mage with the power of resurrection seeks a new apprentice.

%description camp-raajal -l hu.UTF-8
Egy mágus a feltámasztás erejével egy új tanoncot keres.

%package camp-the_three_elves
Summary:	Three elves have just begun their adventure in the northern swampland
Summary(hu.UTF-8):	Három tünde kalandjai az északi mocsarakban
Group:		X11/Applications/Games

%description camp-the_three_elves
Three elves have just begun their adventure in the northern swampland.
Will they become heroes or will they be responsible for another undead
expansion?

%description camp-the_three_elves -l hu.UTF-8
Három tünde kalandjai az északi mocsarakban. Hősökké válnak vagy ők
lesznek a felelősek az újabb élőhalott invázió miatt?

%package camp-trolls
Summary:	You are Eag, the leader of a troll tribe
Summary(hu.UTF-8):	Eag vagy, egy troll törzs vezetője
Group:		X11/Applications/Games

%description camp-trolls
You are Eag, the leader of a troll tribe, who lives in a peaceful cave
farming mushrooms for food. However a scout brings you bad news:
dwarves are attempting to mine gold and other valuable minerals in the
cave. They have attacked another tribe that is near you. Hearing the
news you lead your fighters to help.

%description camp-trolls -l hu.UTF-8
Eag vagy, egy troll törzs vezetője, akik egy békés barlagban élnek, és
gombát termesztenek ételnek. Azonban egy hírnök rossz híreket hoz:
törpök akarnak aranyat és egyéb értékes ásványokat bányászni a
barlangban. Egy közeli törzset már meg is támadtak. A híreket hallva a
harcosaidat harcba vezeted.

%prep
install -d wesnoth-addons
cd wesnoth-addons
%{__tar} xf %{SOURCE0}

%{__tar} xf %{SOURCE50}
%{__tar} xf %{SOURCE51}
%{__tar} xf %{SOURCE52}
%{__tar} xf %{SOURCE53}
%{__tar} xf %{SOURCE54}
%{__tar} xf %{SOURCE55}
%{__tar} xf %{SOURCE56}
%{__tar} xf %{SOURCE57}

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
%{__cp} -r Bad_Moon_Rising $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Forgotten_Kingdom $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Raajal $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r The_Three_Elves $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Trolls $RPM_BUILD_ROOT%{wesnothcamp}

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

%files camp-bad_moon_rising
%defattr(644,root,root,755)
%{wesnothcamp}/Bad_Moon_Rising

%files camp-forgotten_kingdom
%defattr(644,root,root,755)
%{wesnothcamp}/Forgotten_Kingdom

%files camp-raajal
%defattr(644,root,root,755)
%{wesnothcamp}/Raajal

%files camp-the_three_elves
%defattr(644,root,root,755)
%{wesnothcamp}/The_Three_Elves

%files camp-trolls
%defattr(644,root,root,755)
%{wesnothcamp}/Trolls
