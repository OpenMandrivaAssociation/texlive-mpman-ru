# revision 15878
# category Package
# catalog-ctan /info/metapost/doc/russian/mpman-ru
# catalog-date 2008-08-22 17:15:44 +0200
# catalog-license other-free
# catalog-version 1.004
Name:		texlive-mpman-ru
Version:	1.004
Release:	8
Summary:	A Russian translation of the MetaPost manual
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/metapost/doc/russian/mpman-ru
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpman-ru.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpman-ru.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.004-2
+ Revision: 754117
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.004-1
+ Revision: 719071
- texlive-mpman-ru
- texlive-mpman-ru
- texlive-mpman-ru
- texlive-mpman-ru

