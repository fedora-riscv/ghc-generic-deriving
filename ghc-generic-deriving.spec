# generated by cabal-rpm-0.12.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name generic-deriving
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        1.12
Release:        2%{?dist}
Summary:        Generic programming library for generalised deriving

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-template-haskell-devel
%if %{with tests}
BuildRequires:  ghc-hspec-devel
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
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%package devel-doc
Summary:        Haskell %{pkg_name} library development documentation

BuildArch:      noarch

%description devel-doc
This package provides the Haskell %{pkg_name} library development
documentation.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install
grep -v "%{_docdir}/ghc/html/libraries/%{pkgver}" %{name}-devel.files > %{name}-devel-nodoc.files
grep "%{_docdir}/ghc/html/libraries/%{pkgver}" %{name}-devel.files > %{name}-devel-doc.files


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel-nodoc.files
%doc CHANGELOG.md README.md


%files devel-doc -f %{name}-devel-doc.files
%doc CHANGELOG.md README.md


%changelog
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
