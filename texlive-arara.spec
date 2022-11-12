Name:		texlive-arara
Version:	63760
Release:	1
Summary:	Automation of LaTeX compilation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/arara
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arara.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arara.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arara.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-arara.bin = %{EVRD}

%description
Arara is comparable with other well-known compilation tools
like latexmk and rubber. The key difference is that that arara
determines its actions from metadata in the source code, rather
than relying on indirect resources, such as log file analysis.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/arara
%{_texmfdistdir}/scripts/arara
%doc %{_texmfdistdir}/doc/support/arara
%doc %{_texmfdistdir}/doc/man/man1/*
#- source
%doc %{_texmfdistdir}/source/support/arara

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/arara/arara.sh arara
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
