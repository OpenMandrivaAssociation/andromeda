Name:		andromeda
Summary:	Qt file manager
Version:	0.1
Release:	1
License:	LGPL
Group:		Graphical desktop/Other
URL:		https://gitorious.org/andromeda/andromeda/
Source0:	%{name}-%{version}.tar.xz
Patch0:		andromeda-0.1-mdv-linkage.patch
BuildRequires:	cmake
BuildRequires:	libqt4-devel

%description
Cross-platform file manager, written on Qt. Currently has support for local
filesystem (i.e. file:// protocol), simple web view and bookmarks plugins.

%prep
%setup -q
%patch0 -p1

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
%doc bugs.txt features.txt TODO.txt
%if %{mdvver} <= 201100
%{_datadir}/%{name}/translations/
%endif
