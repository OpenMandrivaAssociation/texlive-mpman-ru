%global tl_name mpman-ru
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.004
Release:	%{tl_revision}.1
Summary:	A Russian translation of the MetaPost manual
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/metapost/doc/russian/mpman-ru
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpman-ru.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpman-ru.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A translation of the user manual, as distributed with MetaPost itself.

