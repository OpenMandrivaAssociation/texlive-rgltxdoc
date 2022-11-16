Name:		texlive-rgltxdoc
Version:	53858
Release:	1
Summary:	Common code for documentation of the author's packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rgltxdoc
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rgltxdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rgltxdoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rgltxdoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package combines several other packages and defines
additional macros and environments for documenting LaTeX code.
The package mainly serves the purpose of combining the
preferences used in the author's own package documentations.
However, others can use the package as well. Compatibility
between versions cannot be guaranteed, however.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/rgltxdoc
%{_texmfdistdir}/tex/latex/rgltxdoc
%doc %{_texmfdistdir}/doc/latex/rgltxdoc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
