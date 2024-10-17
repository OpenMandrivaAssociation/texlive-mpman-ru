Name:		texlive-mpman-ru
Version:	15878
Release:	2
Summary:	A Russian translation of the MetaPost manual
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/metapost/doc/russian/mpman-ru
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpman-ru.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpman-ru.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A translation of the user manual, as distributed with MetaPost
itself.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/Makefile
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/README
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/README.ru.koi8-r
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/bm-to-utf16be.awk
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/ctabbing.sty
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/extract-bm.awk
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/idx1.awk
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/idx2.awk
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/idx3.awk
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/manfig-ru.mp
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/mpman-optab-ru.tex
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/mpman-ru.pdf
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/mpman-ru.tex
%doc %{_texmfdistdir}/doc/metapost/mpman-ru/mpman.ist

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
