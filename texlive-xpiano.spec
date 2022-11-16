Name:		texlive-xpiano
Version:	61719
Release:	1
Summary:	An extension of the piano package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xpiano
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpiano.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpiano.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpiano.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros for typesetting virtual keyboards
limited to two octaves for showing notes represented by a
colored circle. Optionally, the number used for pitch analysis
can be shown. It is an extension of piano.sty by Emile
Daneault, written in expl3 in answer to a couple of questions
on TeX.StackExchange:
https://tex.stackexchange.com/questions/162184/
https://tex.stackexchange.com/questions/246276/. It features
extended syntax and several options, like setting the color,
adding numbers for pitch analysis, one or two octaves, and
others.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xpiano
%{_texmfdistdir}/tex/latex/xpiano
%doc %{_texmfdistdir}/doc/latex/xpiano

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
