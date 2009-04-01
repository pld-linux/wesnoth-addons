%define wesnothver 1.6
Summary:	Additional stuffs (maps, scenarios, eras, campaigns) for Wesnoth
Summary(hu.UTF-8):	Kiegészítők Wesnoth-hoz (térképek, küldetések, korok)
Summary(pl.UTF-8):	Dodatki do Wesnoth (mapy, scenariusze, epoki, kampanie)
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
Source58:	http://files.wesnoth.org/addons/%{wesnothver}/Hallowed_Glade.tar.bz2
# Source58-md5:	1f7e93aac990a9464b468eaf1324f55b
Source59:	http://files.wesnoth.org/addons/%{wesnothver}/Attack_of_the_Undead.tar.bz2
# Source59-md5:	accb8cf6a0e40a8967e0e1b310db5fd4
Source60:	http://files.wesnoth.org/addons/%{wesnothver}/Children_of_Dragons.tar.bz2
# Source60-md5:	367f07f62957d1efa8f987376b784927
Source61:	http://files.wesnoth.org/addons/%{wesnothver}/Forgotten_Legacy.tar.bz2
# Source61-md5:	2701c604d16783cd1e9f8f5a220ba2cc
Source62:	http://files.wesnoth.org/addons/%{wesnothver}/Griffoon_Lads.tar.bz2
# Source62-md5:	59d5795e79b5aea75a7578e061c7ffc5
Source63:	http://files.wesnoth.org/addons/%{wesnothver}/Invasion_from_the_Unknown.tar.bz2
# Source63-md5:	7f33e944fc9132ddd4c1bb30483c65a3
Source64:	http://files.wesnoth.org/addons/%{wesnothver}/Story_of_Wose.tar.bz2
# Source64-md5:	e2f0d52d1ac2330b3055443aef9ba227
Source65:	http://files.wesnoth.org/addons/%{wesnothver}/Sceptre_of_Life.tar.bz2
# Source65-md5:	d3b2c5f5fe038089d09fe2d84d771b05
Source66:	http://files.wesnoth.org/addons/%{wesnothver}/Fiery_Menace.tar.bz2
# Source66-md5:	ebac0984a1315d395d7995d9267c211e
Source67:	http://files.wesnoth.org/addons/%{wesnothver}/Delfadors_Memoirs.tar.bz2
# Source67-md5:	9f2abced34056e14b3737012ec3e8f67
Source68:	http://files.wesnoth.org/addons/%{wesnothver}/The_Dark_Hordes.tar.bz2
# Source68-md5:	201bebc89509fc81b98adc44a4fe7424
Source69:	http://files.wesnoth.org/addons/%{wesnothver}/Broken_Valley.tar.bz2
# Source69-md5:	313287db6950e177c0c195845d08bd8a
URL:		http://www.wesnoth.org/addons/1.6/
Requires:	wesnoth >= %{wesnothver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define wesnothdir %{_datadir}/wesnoth/data
%define wesnothmulti %{wesnothdir}/multiplayer
%define wesnothcamp %{wesnothdir}/campaigns

%description
Additional stuffs (maps, scenarios, eras, campaigns) for Wesnoth.

%description -l hu.UTF-8
Bővítések Wesnoth-hoz (térképek, küldetések, korok).

%description -l pl.UTF-8
Dodatki do gry Wesnoth (mapy, scenariusze, epoki, kampanie).

%package mp-totn
Summary:	Temples of the Nagas - a team based MP survival game designed for four players
Summary(hu.UTF-8):	A Temples of the Nagas egy csapat alapú MP túlélő játék négy játékosra
Summary(pl.UTF-8):	Temples of the Nagas - drużynowa gra o przeżycie dla czterech graczy
Group:		X11/Applications/Games

%description mp-totn
Temples of the Nagas is a team based MP survival game designed for
four players.

%description mp-totn -l hu.UTF-8
A Temples of the Nagas egy csapat alapú MP túlélő játék négy
játékosra.

%description mp-totn -l pl.UTF-8
Temples of the Nagas (Świątynie Nagas) to drużynowa gra o przeżycie
zaprojektowana dla czterech graczy.

%package camp-flight_to_freedom
Summary:	Flight to Freedom chronicles the story of the drake hero Malakar
Summary(hu.UTF-8):	Flight to Freedom Malakar sárkány hős krónikáit meséli el
Summary(pl.UTF-8):	Flight to Freedom - kampania opisująca historię drake'a Malakara
Group:		X11/Applications/Games

%description camp-flight_to_freedom
Flight to Freedom chronicles the story of the drake hero Malakar. Lead
him and his Drake tribe to freedom from humanity's slavery!

%description camp-flight_to_freedom -l hu.UTF-8
Flight to Freedom Malakar sárkány hős krónikáit meséli el. Vezesd őt
és a sárkányai megalapítják a szabadságot az emberek rabszolgása után!

%description camp-flight_to_freedom -l pl.UTF-8
Flight to Freedom to campania opowiadadająca historię bohatera
drake'ów - Malakara. Poprowadź jego, oraz jego plemię ku wolności z
ludzkiej niewoli!

%package camp-dead_water
Summary:	Lead your merfolk on a mission to convince a powerful mermaid to help you repel an undead invasion
Summary(hu.UTF-8):	Vezesd a sellő népet egy élőhalott invázió ellen
Summary(pl.UTF-8):	Przekonaj potężną syrenę aby pomogła Twojemu morskiemu ludowi odeprzeć inwazję umarlaków
Group:		X11/Applications/Games

%description camp-dead_water
Lead your merfolk on a mission to convince a powerful mermaid to help
you repel an undead invasion.

%description camp-dead_water -l hu.UTF-8
Vezesd a sellő népet egy élőhalott invázió ellen.

%description camp-dead_water -l pl.UTF-8
Poprowadź Twój morski lud na misję. Przekonaj potężną syrenę, aby
pomogła Ci odeprzeć inwazję umarlaków.

%package camp-elvish_legacy
Summary:	You must defend your people from orcish raids
Summary(hu.UTF-8):	Meg kell védened az embereid az orkoktól
Summary(pl.UTF-8):	Obroń swój lud przed atakami orków
Group:		X11/Applications/Games

%description camp-elvish_legacy
You must defend your people from orcish raids.

%description camp-elvish_legacy -l hu.UTF-8
Meg kell védened az embereid az orkoktól.

%description camp-elvish_legacy -l pl.UTF-8
W tej kampani wcielisz się w rolę przywódcy elfów. Twoim zadaniem
będzie ochronić swój lud przed atakami orków.

%package camp-bad_moon_rising
Summary:	Officer Lorenzon leads a revolution against the brutal Prince
Summary(hu.UTF-8):	Lorenzon kapitány egy lázadást vezet a kegyetlen Herceg ellen
Summary(pl.UTF-8):	Oficer Lorenzon staje na czele rewolucji przeciwko złemu księciu
Group:		X11/Applications/Games

%description camp-bad_moon_rising
Officer Lorenzon leads a revolution against the brutal Prince.

%description camp-bad_moon_rising -l hu.UTF-8
Lorenzon kapitány egy lázadást vezet a kegyetlen Herceg ellen.

%description camp-bad_moon_rising -l pl.UTF-8
Jako oficer Lorenzon staniesz na czele rewolucji przeciwko złemu
księciu.

%package camp-forgotten_kingdom
Summary:	Help Orlog, a troll chieftan
Summary(hu.UTF-8):	Segíts Orlog-nak, egy troll főnöknek
Summary(pl.UTF-8):	Pomóż Orlogowi, hersztowi trolli
Group:		X11/Applications/Games

%description camp-forgotten_kingdom
Help Orlog, a troll chieftan, lead his people to safety in the
underground and discover an ancient power long forgotten.

%description camp-forgotten_kingdom -l hu.UTF-8
Segíts Orlog-nak, a troll főnöknek az embereit biztonságba vezényelni
a föld alatt és felfedezni az ősí erőt, amelyet rég elfeledtek.

%description camp-forgotten_kingdom -l pl.UTF-8
Pomóż Orologi, hersztowi trolli. Poprowadź jego ludzi bezpiecznie
przez podziemia i odkryj zapomniane antyczne moce.

%package camp-raajal
Summary:	An Arch Mage with the power of resurrection seeks a new apprentice
Summary(hu.UTF-8):	Egy mágus a feltámasztás erejével egy új tanoncot keres
Summary(pl.UTF-8):	Arcymag posiadający moc wskrzeszania zmarłych szuka praktykanta
Group:		X11/Applications/Games

%description camp-raajal
An Arch Mage with the power of resurrection seeks a new apprentice.

%description camp-raajal -l hu.UTF-8
Egy mágus a feltámasztás erejével egy új tanoncot keres.

%description camp-raajal -l pl.UTF-8
Arcymag posiadający moc wskrzeszania zmarłych szuka praktykanta.

%package camp-the_three_elves
Summary:	Three elves have just begun their adventure in the northern swampland
Summary(hu.UTF-8):	Három tünde kalandjai az északi mocsarakban
Summary(pl.UTF-8):	Trzej elfowie właśnie rozpoczęli swoją podróż przez północne bagna
Group:		X11/Applications/Games

%description camp-the_three_elves
Three elves have just begun their adventure in the northern swampland.
Will they become heroes or will they be responsible for another undead
expansion?

%description camp-the_three_elves -l hu.UTF-8
Három tünde kalandjai az északi mocsarakban. Hősökké válnak vagy ők
lesznek a felelősek az újabb élőhalott invázió miatt?

%description camp-the_three_elves -l pl.UTF-8
Trzej elfowie właśnie rozpoczęli swoją przygodę w północnych bagnach.
Czy staną się bohaterami, czy też będą odpowiedzialni za kolejną
inwazję umarlaków?

%package camp-trolls
Summary:	You are Eag, the leader of a troll tribe
Summary(hu.UTF-8):	Eag vagy, egy troll törzs vezetője
Summary(pl.UTF-8):	Wcielasz się w Eaga, przywódcę plemienia trolli
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

%description camp-trolls -l pl.UTF-8
W tej kampanii wcielasz się w Eaga, przywódcę pokojowego plemienia
trolli, które zamieszkuje jaskinię i zajmuje się uprawą grzybów.
Pewnego dnia zwiadowca przynosi Ci złe wieści: krasnoludy zamierzają
wydobywać złoto i inne cenne minerały w Twojej grocie. Zaatakowali już
inne plemię w Twojej okolicy. Musisz poprowadzić Twoje plemię do
walki.

%package camp-hallowed_glade
Summary:	Fight against the forces of darkness to recover a dangerous artifact
Summary(hu.UTF-8):	Harc a sötétség serege ellen egy veszélyes lelet újrateremtéséért
Summary(pl.UTF-8):	Walcz przeciwko siłom ciemności, aby odzyskać niebezpieczny artefakt
Group:		X11/Applications/Games

%description camp-hallowed_glade
Fight against the forces of darkness to recover a dangerous artifact.

%description camp-hallowed_glade -l hu.UTF-8
Harc a sötétség serege ellen egy veszélyes lelet újrateremtéséért.

%description camp-hallowed_glade -l pl.UTF-8
Walcz przeciwko siłom ciemności, aby odzyskać niebezpieczny artefakt.

%package camp-attack_of_the_undead
Summary:	Play as a mage to protect your city from the undead
Summary(hu.UTF-8):	Egy mágusként kell megvédened a városodat az élőholtak ellen
Summary(pl.UTF-8):	Jako mag ochroń swoje miasto przed umarlakami
Group:		X11/Applications/Games

%description camp-attack_of_the_undead
Play as a mage to protect your city from the undead.

%description camp-attack_of_the_undead -l hu.UTF-8
Egy mágusként kell megvédened a városodat az élőholtak ellen.

%description camp-attack_of_the_undead -l pl.UTF-8
Wciel się w rolę maga, którego zadaniem jest ochrona miasta przed
umarlakami.

%package camp-children_of_dragons
Summary:	Lead the Drakes as they search for a new homeland
Summary(hu.UTF-8):	Vezesd a sárkányokat új haza kereséséhez
Summary(pl.UTF-8):	Poprowadź Drake'ów w ich poszukiwaniach nowej ojczyzny
Group:		X11/Applications/Games

%description camp-children_of_dragons
Lead the Drakes as they search for a new homeland.

%description camp-children_of_dragons -l hu.UTF-8
Vezesd a sárkányokat új haza kereséséhez.

%description camp-children_of_dragons -l pl.UTF-8
Poprowadź Drake'ów w ich poszukiwaniach nowej ojczyzny.

%package camp-the_forgotten_legacy
Summary:	This is a campaign focusing on the saurian faction
Summary(hu.UTF-8):	Ez egy küldetés a gyík fajra összpontosítva
Summary(pl.UTF-8):	Kampania opisująca lud jaszczurów
Group:		X11/Applications/Games

%description camp-the_forgotten_legacy
This is a campaign focusing on the saurian faction.

%description camp-the_forgotten_legacy -l hu.UTF-8
Ez egy küldetés a gyík fajra összpontosítva.

%description camp-the_forgotten_legacy -l pl.UTF-8
Akcja tej kampanii skupia się na historii ludu jaszczurów.

%package camp-the_griffon_lads
Summary:	Follow the adventures of The Griffoon Lads in the Far North
Summary(hu.UTF-8):	Kövesd a Griffoon Fiúkat a Messzi Északon
Summary(pl.UTF-8):	Przeżyj przygody Młodzieńców Gryfów na Dalekiej Północy
Group:		X11/Applications/Games

%description camp-the_griffon_lads
Follow the adventures of The Griffoon Lads in the Far North.

%description camp-the_griffon_lads -l hu.UTF-8
Kövesd a Griffoon Fiúkat a Messzi Északon.

%description camp-the_griffon_lads -l pl.UTF-8
Przeżyj przygody Młodzieńców Gryfów na Dalekiej Północy.

%package camp-invasion_from_the_unknown
Summary:	Invasion from the Unknown
Summary(hu.UTF-8):	Invázió az ismeretlenből
Group:		X11/Applications/Games

%description camp-invasion_from_the_unknown
Long after the Fall, the last forest elves are forced to abandon their
safe valley, and find themselves resorting to the dark means of
necromancy in order to survive the perils and challenges of this new
harsh world. Later, as the shadow of Chaos covers the entire
continent, they prepare a counter-attack to the Empire, with one
unique goal in their minds: defeat the evil Emperor, whoever it is.
Lead these courageous living and non-living warriors to the victory,
and rediscover lost secrets of the history. (Expert level, 2 chapters
of 13 scenarios each one.)

%package camp-story_of_wose
Summary:	Story of Wose
Summary(hu.UTF-8):	Az erdő legendája
Group:		X11/Applications/Games

%description camp-story_of_wose
The trees are not always what they seem.

%description camp-story_of_wose -l hu.UTF-8
A fák nem mindig azok, aminek látszottak.

%package camp-sceptre_of_life
Summary:	Sceptre of Life
Summary(hu.UTF-8):	Az élet jogarja
Group:		X11/Applications/Games

%description camp-sceptre_of_life
A young doctor in a small, backwoods town is propelled into a
Northland skirmish. The small choices he makes have far-reaching
consequences as the Sceptre of Life is unveiled in a desparate, dying
land.

%package camp-fiery_menace
Summary:	Fiery Menace
Group:		X11/Applications/Games

%description camp-fiery_menace
Stop them! They are coming! Experience this adventure-style campaign
centering on Drakes and Humans.

%package camp-delfadors_memoirs
Summary:	Delfadors Memoirs
Summary(hu.UTF-8):	Delfador emlékiratai
Group:		X11/Applications/Games

%description camp-delfadors_memoirs
Wesnoth seems to be slipping inexorably into chaos, as marauding orcs
pour south across the Great River, and mysterious and deadly creatures
roam the night. Who is the shadowy Iliah-Malal? Can you defeat him
before he destroys all life in Wesnoth?

%package camp-the_dark_hordes
Summary:	The Dark Hordes
Summary(hu.UTF-8):	A Sötét Hordák
Group:		X11/Applications/Games

%description camp-the_dark_hordes
Lead fugitive dark sorcerer Gwiti Ha'atel to mastery of the undead
hordes. Nine playable scenarios so far.

%package camp-broken_valley
Summary:	Broken Valley
Group:		X11/Applications/Games

%description camp-broken_valley
A highly alpha campaign about the beginning of a great war on another
continent. The player takes part as the dwarvern character
Zyancordorza and his allies as they discover a deep plot by a dark
elven sorcerer. Future plans include a detailed history, cultures, and
legends for each of the areas and people mentioned, and some for the
ones never even hinted at.

%prep
%setup -q -c -a0 -a50 -a51 -a52 -a53 -a54 -a55 -a56 -a58 -a59 -a60 -a61 -a62 -a63 -a64 -a65 -a66 -a67 -a68 -a69
find -name COPYING.txt -exec rm {} \;

%install
rm -rf $RPM_BUILD_ROOT

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
# %%{__cp} -r Trolls $RPM_BUILD_ROOT%%{wesnothcamp}
%{__cp} -r Hallowed_Glade $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Attack_of_the_Undead $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Children_of_Dragons $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Forgotten_Legacy $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Griffoon_Lads $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Invasion_from_the_Unknown $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Story_of_Wose $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Sceptre_of_Life $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Fiery_Menace $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Delfadors_Memoirs $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r The_Dark_Hordes $RPM_BUILD_ROOT%{wesnothcamp}
%{__cp} -r Broken_Valley $RPM_BUILD_ROOT%{wesnothcamp}

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

# %files camp-trolls
# %defattr(644,root,root,755)
# %{wesnothcamp}/Trolls

%files camp-hallowed_glade
%defattr(644,root,root,755)
%{wesnothcamp}/Hallowed_Glade

%files camp-attack_of_the_undead
%defattr(644,root,root,755)
%{wesnothcamp}/Attack_of_the_Undead

%files camp-children_of_dragons
%defattr(644,root,root,755)
%{wesnothcamp}/Children_of_Dragons

%files camp-the_forgotten_legacy
%defattr(644,root,root,755)
%{wesnothcamp}/Forgotten_Legacy

%files camp-the_griffon_lads
%defattr(644,root,root,755)
%{wesnothcamp}/Griffoon_Lads

%files camp-invasion_from_the_unknown
%defattr(644,root,root,755)
%{wesnothcamp}/Invasion_from_the_Unknown

%files camp-story_of_wose
%defattr(644,root,root,755)
%{wesnothcamp}/Story_of_Wose

%files camp-sceptre_of_life
%defattr(644,root,root,755)
%{wesnothcamp}/Sceptre_of_Life

%files camp-fiery_menace
%defattr(644,root,root,755)
%{wesnothcamp}/Fiery_Menace

%files camp-delfadors_memoirs
%defattr(644,root,root,755)
%{wesnothcamp}/Delfadors_Memoirs

%files camp-the_dark_hordes
%defattr(644,root,root,755)
%{wesnothcamp}/The_Dark_Hordes

%files camp-broken_valley
%defattr(644,root,root,755)
%{wesnothcamp}/Broken_Valley
