# revision 29762
# category Package
# catalog-ctan /support/arara
# catalog-date 2013-02-06 08:25:13 +0100
# catalog-license bsd
# catalog-version 3.0
Name:		texlive-arara
Version:	3.0
Release:	6
Summary:	Automation of LaTeX compilation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/arara
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arara.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arara.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arara.source.tar.xz
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
%{_texmfdistdir}/scripts/arara/arara.jar
%{_texmfdistdir}/scripts/arara/arara.sh
%{_texmfdistdir}/scripts/arara/rules/biber.yaml
%{_texmfdistdir}/scripts/arara/rules/bibtex.yaml
%{_texmfdistdir}/scripts/arara/rules/clean.yaml
%{_texmfdistdir}/scripts/arara/rules/dvips.yaml
%{_texmfdistdir}/scripts/arara/rules/frontespizio.yaml
%{_texmfdistdir}/scripts/arara/rules/latex.yaml
%{_texmfdistdir}/scripts/arara/rules/lmkclean.yaml
%{_texmfdistdir}/scripts/arara/rules/lualatex.yaml
%{_texmfdistdir}/scripts/arara/rules/lualatexmk.yaml
%{_texmfdistdir}/scripts/arara/rules/luatex.yaml
%{_texmfdistdir}/scripts/arara/rules/make.yaml
%{_texmfdistdir}/scripts/arara/rules/makeglossaries.yaml
%{_texmfdistdir}/scripts/arara/rules/makeindex.yaml
%{_texmfdistdir}/scripts/arara/rules/nomencl.yaml
%{_texmfdistdir}/scripts/arara/rules/pdflatex.yaml
%{_texmfdistdir}/scripts/arara/rules/pdflatexmk.yaml
%{_texmfdistdir}/scripts/arara/rules/pdftex.yaml
%{_texmfdistdir}/scripts/arara/rules/ps2pdf.yaml
%{_texmfdistdir}/scripts/arara/rules/sketch.yaml
%{_texmfdistdir}/scripts/arara/rules/songidx.yaml
%{_texmfdistdir}/scripts/arara/rules/tex.yaml
%{_texmfdistdir}/scripts/arara/rules/xelatex.yaml
%{_texmfdistdir}/scripts/arara/rules/xelatexmk.yaml
%{_texmfdistdir}/scripts/arara/rules/xetex.yaml
%doc %{_texmfdistdir}/doc/support/arara/README
%doc %{_texmfdistdir}/doc/support/arara/arara-usermanual.pdf
%doc %{_texmfdistdir}/doc/support/arara/arara-usermanual.tex
%doc %{_texmfdistdir}/doc/support/arara/arara.sty
%doc %{_texmfdistdir}/doc/support/arara/figures/arara.png
%doc %{_texmfdistdir}/doc/support/arara/figures/inlage/inlage-addcommand.png
%doc %{_texmfdistdir}/doc/support/arara/figures/inlage/inlage-addcompiler.png
%doc %{_texmfdistdir}/doc/support/arara/figures/inlage/inlage-araramenu.png
%doc %{_texmfdistdir}/doc/support/arara/figures/inlage/inlage-editcommands.png
%doc %{_texmfdistdir}/doc/support/arara/figures/inlage/inlage-listarara.png
%doc %{_texmfdistdir}/doc/support/arara/figures/inlage/inlage-newprofile.png
%doc %{_texmfdistdir}/doc/support/arara/figures/inlage/inlage-settings.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-finish.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-langsel.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-license.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-packs.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-path.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-pathwarning.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-progress.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/install-welcome.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/uninstall-finish.png
%doc %{_texmfdistdir}/doc/support/arara/figures/installer/uninstall-welcome.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texniccenter/texniccenter-config.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texniccenter/texniccenter-newprofile.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texniccenter/texniccenter-profiles.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texshop/texshop-arara.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texworks/texworks-add.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texworks/texworks-arara.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texworks/texworks-prefs.png
%doc %{_texmfdistdir}/doc/support/arara/figures/texworks/texworks-profile.png
%doc %{_texmfdistdir}/doc/support/arara/figures/winedt/winedt-ararabutton.png
%doc %{_texmfdistdir}/doc/support/arara/figures/winedt/winedt-menu.png
%doc %{_texmfdistdir}/doc/support/arara/figures/winedt/winedt-optionsinterface.png
%doc %{_texmfdistdir}/doc/support/arara/references.bib
#- source
%doc %{_texmfdistdir}/source/support/arara/pom.xml
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/Arara.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/exception/AraraException.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraCommand.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraConfiguration.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraDirective.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraFilePattern.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraLanguage.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraRuleArgument.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraRuleConfig.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/model/AraraTask.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/AraraConstants.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/AraraLocalization.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/AraraLogging.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/AraraMethods.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/AraraResolver.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/AraraUtils.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/CommandLineAnalyzer.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/CommandTrigger.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/ConfigurationLoader.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/DirectiveExtractor.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/DirectiveParser.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/LanguageController.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/TaskDeployer.java
%doc %{_texmfdistdir}/source/support/arara/src/main/java/com/github/arara/utils/TeeOutputStream.java
%doc %{_texmfdistdir}/source/support/arara/src/main/resources/com/github/arara/conf/logback.xml
%doc %{_texmfdistdir}/source/support/arara/src/main/resources/com/github/arara/localization/dummy
%doc %{_texmfdistdir}/source/support/arara/src/test/java/com/github/arara/AraraTest.java

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/arara/arara.sh arara
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
