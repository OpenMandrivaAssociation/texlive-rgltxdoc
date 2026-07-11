%global tl_name rgltxdoc
%global tl_revision 53858

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Common code for documentation of the authors packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rgltxdoc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rgltxdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rgltxdoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rgltxdoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package combines several other packages and defines additional
macros and environments for documenting LaTeX code. The package mainly
serves the purpose of combining the preferences used in the author's own
package documentations. However, others can use the package as well.
Compatibility between versions cannot be guaranteed, however.

