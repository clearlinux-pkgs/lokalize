#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : lokalize
Version  : 23.04.2
Release  : 55
URL      : https://download.kde.org/stable/release-service/23.04.2/src/lokalize-23.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.2/src/lokalize-23.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.2/src/lokalize-23.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 GPL-3.0 LGPL-2.1
Requires: lokalize-bin = %{version}-%{release}
Requires: lokalize-data = %{version}-%{release}
Requires: lokalize-license = %{version}-%{release}
Requires: lokalize-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(hunspell)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n lokalize-23.04.2
cd %{_builddir}/lokalize-23.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686502699
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1686502699
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lokalize
cp %{_builddir}/lokalize-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/lokalize/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/lokalize-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/lokalize/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc || :
cp %{_builddir}/lokalize-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/lokalize/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/lokalize-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/lokalize/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/lokalize-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/lokalize/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/lokalize-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/lokalize/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/lokalize-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/lokalize/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/lokalize-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/lokalize/7d9831e05094ce723947d729c2a46a09d6e90275 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang lokalize
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/lokalize
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
/usr/share/doc/HTML/fr/lokalize/index.cache.bz2
/usr/share/doc/HTML/fr/lokalize/index.docbook
/usr/share/doc/HTML/hu/lokalize/index.cache.bz2
/usr/share/doc/HTML/hu/lokalize/index.docbook
/usr/share/doc/HTML/id/lokalize/index.cache.bz2
/usr/share/doc/HTML/id/lokalize/index.docbook
/usr/share/doc/HTML/it/lokalize/configure_shortcuts.png
/usr/share/doc/HTML/it/lokalize/configure_toolbar.png
/usr/share/doc/HTML/it/lokalize/default_editor_lokalize.png
/usr/share/doc/HTML/it/lokalize/glossary.png
/usr/share/doc/HTML/it/lokalize/index.cache.bz2
/usr/share/doc/HTML/it/lokalize/index.docbook
/usr/share/doc/HTML/it/lokalize/original-diff.png
/usr/share/doc/HTML/it/lokalize/project_overview.png
/usr/share/doc/HTML/it/lokalize/sync.png
/usr/share/doc/HTML/it/lokalize/tmview.png
/usr/share/doc/HTML/nl/lokalize/index.cache.bz2
/usr/share/doc/HTML/nl/lokalize/index.docbook
/usr/share/doc/HTML/pt/lokalize/index.cache.bz2
/usr/share/doc/HTML/pt/lokalize/index.docbook
/usr/share/doc/HTML/pt_BR/lokalize/index.cache.bz2
/usr/share/doc/HTML/pt_BR/lokalize/index.docbook
/usr/share/doc/HTML/ru/lokalize/index.cache.bz2
/usr/share/doc/HTML/ru/lokalize/index.docbook
/usr/share/doc/HTML/sr/lokalize/glossary.png
/usr/share/doc/HTML/sr/lokalize/index.cache.bz2
/usr/share/doc/HTML/sr/lokalize/index.docbook
/usr/share/doc/HTML/sr/lokalize/original-diff.png
/usr/share/doc/HTML/sr/lokalize/sync.png
/usr/share/doc/HTML/sr/lokalize/tmview.png
/usr/share/doc/HTML/sr@latin/lokalize/index.cache.bz2
/usr/share/doc/HTML/sr@latin/lokalize/index.docbook
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
/usr/share/package-licenses/lokalize/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/lokalize/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/lokalize/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/lokalize/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/lokalize/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/lokalize/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc

%files locales -f lokalize.lang
%defattr(-,root,root,-)

