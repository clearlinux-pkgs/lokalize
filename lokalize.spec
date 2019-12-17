#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : lokalize
Version  : 19.12.0
Release  : 15
URL      : https://download.kde.org/stable/release-service/19.12.0/src/lokalize-19.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.0/src/lokalize-19.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.0/src/lokalize-19.12.0.tar.xz.sig
Summary  : Computer-Aided Translation System
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: lokalize-bin = %{version}-%{release}
Requires: lokalize-data = %{version}-%{release}
Requires: lokalize-license = %{version}-%{release}
Requires: lokalize-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : kross-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(hunspell)
BuildRequires : qtbase-dev mesa-dev

%description
# Lokalize
[**Lokalize**](https://www.kde.org/applications/development/lokalize) is a computer-aided translation system that focuses on productivity and quality assurance. It is targeted for software translation and also integrates external conversion tools for freelance office document translation.

%package bin
Summary: bin components for the lokalize package.
Group: Binaries
Requires: lokalize-data = %{version}-%{release}
Requires: lokalize-license = %{version}-%{release}

%description bin
bin components for the lokalize package.


%package data
Summary: data components for the lokalize package.
Group: Data

%description data
data components for the lokalize package.


%package doc
Summary: doc components for the lokalize package.
Group: Documentation

%description doc
doc components for the lokalize package.


%package license
Summary: license components for the lokalize package.
Group: Default

%description license
license components for the lokalize package.


%package locales
Summary: locales components for the lokalize package.
Group: Default

%description locales
locales components for the lokalize package.


%prep
%setup -q -n lokalize-19.12.0
cd %{_builddir}/lokalize-19.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576582069
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576582069
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lokalize
cp %{_builddir}/lokalize-19.12.0/COPYING %{buildroot}/usr/share/package-licenses/lokalize/8cf4afb0636055f7cacd1b6955e0e8ebec7888f5
cp %{_builddir}/lokalize-19.12.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/lokalize/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang lokalize

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lokalize

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.lokalize.desktop
/usr/share/config.kcfg/lokalize.kcfg
/usr/share/icons/hicolor/128x128/apps/lokalize.png
/usr/share/icons/hicolor/32x32/apps/lokalize.png
/usr/share/icons/hicolor/64x64/apps/lokalize.png
/usr/share/icons/hicolor/scalable/apps/lokalize.svgz
/usr/share/knotifications5/lokalize.notifyrc
/usr/share/kxmlgui5/lokalize/editorui.rc
/usr/share/kxmlgui5/lokalize/filesearchtabui.rc
/usr/share/kxmlgui5/lokalize/lokalizemainwindowui.rc
/usr/share/kxmlgui5/lokalize/projectmanagerui.rc
/usr/share/kxmlgui5/lokalize/scriptsui.rc
/usr/share/kxmlgui5/lokalize/translationmemoryrui.rc
/usr/share/lokalize/icons/hicolor/16x16/actions/approved.png
/usr/share/lokalize/icons/hicolor/16x16/actions/insert_arg.png
/usr/share/lokalize/icons/hicolor/16x16/actions/insert_tag.png
/usr/share/lokalize/icons/hicolor/16x16/actions/l10n/sr/approved.png
/usr/share/lokalize/icons/hicolor/16x16/actions/l10n/sr@ijekavian/approved.png
/usr/share/lokalize/icons/hicolor/16x16/actions/l10n/sr@ijekavianlatin/approved.png
/usr/share/lokalize/icons/hicolor/16x16/actions/l10n/sr@latin/approved.png
/usr/share/lokalize/icons/hicolor/16x16/actions/msgid2msgstr.png
/usr/share/lokalize/icons/hicolor/16x16/actions/nexterror.png
/usr/share/lokalize/icons/hicolor/16x16/actions/nextfuzzy.png
/usr/share/lokalize/icons/hicolor/16x16/actions/nextfuzzyuntrans.png
/usr/share/lokalize/icons/hicolor/16x16/actions/nextpo.png
/usr/share/lokalize/icons/hicolor/16x16/actions/nexttemplate.png
/usr/share/lokalize/icons/hicolor/16x16/actions/nextuntranslated.png
/usr/share/lokalize/icons/hicolor/16x16/actions/preverror.png
/usr/share/lokalize/icons/hicolor/16x16/actions/prevfuzzy.png
/usr/share/lokalize/icons/hicolor/16x16/actions/prevfuzzyuntrans.png
/usr/share/lokalize/icons/hicolor/16x16/actions/prevpo.png
/usr/share/lokalize/icons/hicolor/16x16/actions/prevtemplate.png
/usr/share/lokalize/icons/hicolor/16x16/actions/prevuntranslated.png
/usr/share/lokalize/icons/hicolor/16x16/actions/search2msgstr.png
/usr/share/lokalize/icons/hicolor/16x16/actions/transsearch.png
/usr/share/lokalize/icons/hicolor/22x22/actions/approved.png
/usr/share/lokalize/icons/hicolor/22x22/actions/catalogmanager.png
/usr/share/lokalize/icons/hicolor/22x22/actions/insert_arg.png
/usr/share/lokalize/icons/hicolor/22x22/actions/insert_tag.png
/usr/share/lokalize/icons/hicolor/22x22/actions/l10n/sr/approved.png
/usr/share/lokalize/icons/hicolor/22x22/actions/l10n/sr@ijekavian/approved.png
/usr/share/lokalize/icons/hicolor/22x22/actions/l10n/sr@ijekavianlatin/approved.png
/usr/share/lokalize/icons/hicolor/22x22/actions/l10n/sr@latin/approved.png
/usr/share/lokalize/icons/hicolor/22x22/actions/msgid2msgstr.png
/usr/share/lokalize/icons/hicolor/22x22/actions/nexterror.png
/usr/share/lokalize/icons/hicolor/22x22/actions/nextfuzzy.png
/usr/share/lokalize/icons/hicolor/22x22/actions/nextfuzzyuntrans.png
/usr/share/lokalize/icons/hicolor/22x22/actions/nextpo.png
/usr/share/lokalize/icons/hicolor/22x22/actions/nexttemplate.png
/usr/share/lokalize/icons/hicolor/22x22/actions/nextuntranslated.png
/usr/share/lokalize/icons/hicolor/22x22/actions/preverror.png
/usr/share/lokalize/icons/hicolor/22x22/actions/prevfuzzy.png
/usr/share/lokalize/icons/hicolor/22x22/actions/prevfuzzyuntrans.png
/usr/share/lokalize/icons/hicolor/22x22/actions/prevpo.png
/usr/share/lokalize/icons/hicolor/22x22/actions/prevtemplate.png
/usr/share/lokalize/icons/hicolor/22x22/actions/prevuntranslated.png
/usr/share/lokalize/icons/hicolor/22x22/actions/search2msgstr.png
/usr/share/lokalize/icons/hicolor/22x22/actions/transsearch.png
/usr/share/lokalize/icons/hicolor/32x32/actions/approved.png
/usr/share/lokalize/icons/hicolor/32x32/actions/catalogmanager.png
/usr/share/lokalize/icons/hicolor/32x32/actions/diff.png
/usr/share/lokalize/icons/hicolor/32x32/actions/insert_arg.png
/usr/share/lokalize/icons/hicolor/32x32/actions/insert_tag.png
/usr/share/lokalize/icons/hicolor/32x32/actions/l10n/sr/approved.png
/usr/share/lokalize/icons/hicolor/32x32/actions/l10n/sr@ijekavian/approved.png
/usr/share/lokalize/icons/hicolor/32x32/actions/l10n/sr@ijekavianlatin/approved.png
/usr/share/lokalize/icons/hicolor/32x32/actions/l10n/sr@latin/approved.png
/usr/share/lokalize/icons/hicolor/32x32/actions/msgid2msgstr.png
/usr/share/lokalize/icons/hicolor/32x32/actions/nexterror.png
/usr/share/lokalize/icons/hicolor/32x32/actions/nextfuzzy.png
/usr/share/lokalize/icons/hicolor/32x32/actions/nextfuzzyuntrans.png
/usr/share/lokalize/icons/hicolor/32x32/actions/nextpo.png
/usr/share/lokalize/icons/hicolor/32x32/actions/nexttemplate.png
/usr/share/lokalize/icons/hicolor/32x32/actions/nextuntranslated.png
/usr/share/lokalize/icons/hicolor/32x32/actions/preverror.png
/usr/share/lokalize/icons/hicolor/32x32/actions/prevfuzzy.png
/usr/share/lokalize/icons/hicolor/32x32/actions/prevfuzzyuntrans.png
/usr/share/lokalize/icons/hicolor/32x32/actions/prevpo.png
/usr/share/lokalize/icons/hicolor/32x32/actions/prevtemplate.png
/usr/share/lokalize/icons/hicolor/32x32/actions/prevuntranslated.png
/usr/share/lokalize/icons/hicolor/32x32/actions/search2msgstr.png
/usr/share/lokalize/icons/hicolor/32x32/actions/transsearch.png
/usr/share/lokalize/icons/hicolor/48x48/actions/approved.png
/usr/share/lokalize/icons/hicolor/48x48/actions/l10n/sr/approved.png
/usr/share/lokalize/icons/hicolor/48x48/actions/l10n/sr@ijekavian/approved.png
/usr/share/lokalize/icons/hicolor/48x48/actions/l10n/sr@ijekavianlatin/approved.png
/usr/share/lokalize/icons/hicolor/48x48/actions/l10n/sr@latin/approved.png
/usr/share/lokalize/icons/hicolor/scalable/actions/approved.svgz
/usr/share/lokalize/icons/hicolor/scalable/actions/l10n/sr/approved.svgz
/usr/share/lokalize/icons/hicolor/scalable/actions/l10n/sr@ijekavian/approved.svgz
/usr/share/lokalize/icons/hicolor/scalable/actions/l10n/sr@ijekavianlatin/approved.svgz
/usr/share/lokalize/icons/hicolor/scalable/actions/l10n/sr@latin/approved.svgz
/usr/share/lokalize/icons/locolor/16x16/actions/catalogmanager.png
/usr/share/lokalize/icons/locolor/16x16/actions/diff.png
/usr/share/lokalize/icons/locolor/16x16/actions/insert_arg.png
/usr/share/lokalize/icons/locolor/16x16/actions/insert_tag.png
/usr/share/lokalize/icons/locolor/16x16/actions/msgid2msgstr.png
/usr/share/lokalize/icons/locolor/16x16/actions/nexterror.png
/usr/share/lokalize/icons/locolor/16x16/actions/nextfuzzy.png
/usr/share/lokalize/icons/locolor/16x16/actions/nextfuzzyuntrans.png
/usr/share/lokalize/icons/locolor/16x16/actions/nextpo.png
/usr/share/lokalize/icons/locolor/16x16/actions/nexttemplate.png
/usr/share/lokalize/icons/locolor/16x16/actions/nextuntranslated.png
/usr/share/lokalize/icons/locolor/16x16/actions/preverror.png
/usr/share/lokalize/icons/locolor/16x16/actions/prevfuzzy.png
/usr/share/lokalize/icons/locolor/16x16/actions/prevfuzzyuntrans.png
/usr/share/lokalize/icons/locolor/16x16/actions/prevpo.png
/usr/share/lokalize/icons/locolor/16x16/actions/prevtemplate.png
/usr/share/lokalize/icons/locolor/16x16/actions/prevuntranslated.png
/usr/share/lokalize/icons/locolor/16x16/actions/search2msgstr.png
/usr/share/lokalize/icons/locolor/16x16/actions/transsearch.png
/usr/share/lokalize/icons/locolor/32x32/actions/catalogmanager.png
/usr/share/lokalize/icons/locolor/32x32/actions/diff.png
/usr/share/lokalize/icons/locolor/32x32/actions/insert_arg.png
/usr/share/lokalize/icons/locolor/32x32/actions/insert_tag.png
/usr/share/lokalize/icons/locolor/32x32/actions/msgid2msgstr.png
/usr/share/lokalize/icons/locolor/32x32/actions/nexterror.png
/usr/share/lokalize/icons/locolor/32x32/actions/nextfuzzy.png
/usr/share/lokalize/icons/locolor/32x32/actions/nextfuzzyuntrans.png
/usr/share/lokalize/icons/locolor/32x32/actions/nextpo.png
/usr/share/lokalize/icons/locolor/32x32/actions/nexttemplate.png
/usr/share/lokalize/icons/locolor/32x32/actions/nextuntranslated.png
/usr/share/lokalize/icons/locolor/32x32/actions/preverror.png
/usr/share/lokalize/icons/locolor/32x32/actions/prevfuzzy.png
/usr/share/lokalize/icons/locolor/32x32/actions/prevfuzzyuntrans.png
/usr/share/lokalize/icons/locolor/32x32/actions/prevpo.png
/usr/share/lokalize/icons/locolor/32x32/actions/prevtemplate.png
/usr/share/lokalize/icons/locolor/32x32/actions/prevuntranslated.png
/usr/share/lokalize/icons/locolor/32x32/actions/search2msgstr.png
/usr/share/lokalize/icons/locolor/32x32/actions/transsearch.png
/usr/share/lokalize/scripts/find-gui-text.sh
/usr/share/lokalize/scripts/msgmerge.py
/usr/share/lokalize/scripts/msgmerge.rc
/usr/share/lokalize/scripts/odf/xliff2odf-standalone.py
/usr/share/lokalize/scripts/odf/xliff2odf.py
/usr/share/lokalize/scripts/odf/xliff2odf.rc
/usr/share/lokalize/scripts/odf/xliffmerge.py
/usr/share/metainfo/org.kde.lokalize.appdata.xml
/usr/share/qlogging-categories5/lokalize.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/lokalize/index.cache.bz2
/usr/share/doc/HTML/ca/lokalize/index.docbook
/usr/share/doc/HTML/de/lokalize/index.cache.bz2
/usr/share/doc/HTML/de/lokalize/index.docbook
/usr/share/doc/HTML/en/lokalize/configure_shortcuts.png
/usr/share/doc/HTML/en/lokalize/configure_toolbar.png
/usr/share/doc/HTML/en/lokalize/default_editor_lokalize.png
/usr/share/doc/HTML/en/lokalize/glossary.png
/usr/share/doc/HTML/en/lokalize/index.cache.bz2
/usr/share/doc/HTML/en/lokalize/index.docbook
/usr/share/doc/HTML/en/lokalize/original-diff.png
/usr/share/doc/HTML/en/lokalize/project_overview.png
/usr/share/doc/HTML/en/lokalize/sync.png
/usr/share/doc/HTML/en/lokalize/tmview.png
/usr/share/doc/HTML/es/lokalize/index.cache.bz2
/usr/share/doc/HTML/es/lokalize/index.docbook
/usr/share/doc/HTML/et/lokalize/index.cache.bz2
/usr/share/doc/HTML/et/lokalize/index.docbook
/usr/share/doc/HTML/id/lokalize/index.cache.bz2
/usr/share/doc/HTML/id/lokalize/index.docbook
/usr/share/doc/HTML/it/lokalize/index.cache.bz2
/usr/share/doc/HTML/it/lokalize/index.docbook
/usr/share/doc/HTML/nl/lokalize/index.cache.bz2
/usr/share/doc/HTML/nl/lokalize/index.docbook
/usr/share/doc/HTML/pt/lokalize/index.cache.bz2
/usr/share/doc/HTML/pt/lokalize/index.docbook
/usr/share/doc/HTML/pt_BR/lokalize/index.cache.bz2
/usr/share/doc/HTML/pt_BR/lokalize/index.docbook
/usr/share/doc/HTML/sr/lokalize/glossary.png
/usr/share/doc/HTML/sr/lokalize/index.cache.bz2
/usr/share/doc/HTML/sr/lokalize/index.docbook
/usr/share/doc/HTML/sr/lokalize/original-diff.png
/usr/share/doc/HTML/sr/lokalize/sync.png
/usr/share/doc/HTML/sr/lokalize/tmview.png
/usr/share/doc/HTML/sv/lokalize/index.cache.bz2
/usr/share/doc/HTML/sv/lokalize/index.docbook
/usr/share/doc/HTML/uk/lokalize/configure_shortcuts.png
/usr/share/doc/HTML/uk/lokalize/configure_toolbar.png
/usr/share/doc/HTML/uk/lokalize/default_editor_lokalize.png
/usr/share/doc/HTML/uk/lokalize/glossary.png
/usr/share/doc/HTML/uk/lokalize/index.cache.bz2
/usr/share/doc/HTML/uk/lokalize/index.docbook
/usr/share/doc/HTML/uk/lokalize/original-diff.png
/usr/share/doc/HTML/uk/lokalize/project_overview.png
/usr/share/doc/HTML/uk/lokalize/sync.png
/usr/share/doc/HTML/uk/lokalize/tmview.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lokalize/8cf4afb0636055f7cacd1b6955e0e8ebec7888f5
/usr/share/package-licenses/lokalize/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f lokalize.lang
%defattr(-,root,root,-)

