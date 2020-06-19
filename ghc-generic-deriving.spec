# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name generic-deriving
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        1.13.1
Release:        1%{?dist}
Summary:        Generic programming library for generalised deriving

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-prof
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
%endif
# End cabal-rpm deps

%description
This package provides functionality for generalising the deriving mechanism in
Haskell to arbitrary classes. It was first described in the paper:

* /A generic deriving mechanism for Haskell/. Jose Pedro Magalhaes, Atze
Dijkstra, Johan Jeuring, and Andres Loeh. Haskell'10.

The current implementation integrates with the new GHC Generics. See
<http://www.haskell.org/haskellwiki/GHC.Generics> for more information.
Template Haskell code is provided for supporting older GHCs.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%cabal_test


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 1.13.1-1
- update to 1.13.1

* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 1.12.4-4
- enable tests

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 1.12.4-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.12.4-1
- update to 1.12.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.12.2-4
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.2-1
- update to 1.12.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.12-1
- update to 1.12

* Sat Aug 26 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.11.2-3
- Minor fixes to devel-doc subpackage.

* Sat Aug 26 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.11.2-2
- Split documentation into separate subpackage.
- Update to latest spec template.

* Sat Jul 22 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.11.2-1
- spec file generated by cabal-rpm-0.11
