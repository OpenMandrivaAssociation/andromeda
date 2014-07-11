Name:		andromeda
Summary:	Qt file manager
Version:	0.2.1
Release:	8
License:	LGPL
Group:		Graphical desktop/Other
URL:		https://gitorious.org/andromeda/andromeda/
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt3Support)

%description
Cross-platform file manager, written on Qt. Currently has support for local
filesystem (i.e. file:// protocol), simple web view and bookmarks plugins.

%prep
%setup -q
find . -type f -name '*.h' -o -name '*.cpp' -exec chmod 644 {} \;

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF
%make

%install
pushd build
%makeinstall_std
popd

%if %{mdvver} >= 201200
%find_lang %{name} --with-qt --all-name
%define langfile %{name}.lang
%endif

%files %{?langfile:-f %{langfile}}
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc TODO.txt
%if %{mdvver} <= 201100
%{_datadir}/%{name}/translations/
%endif
