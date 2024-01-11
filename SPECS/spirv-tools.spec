%global sdkver 1.3.239.0

Name:           spirv-tools
Version:        2023.1
Release:        2%{?dist}
Summary:        API and commands for processing SPIR-V modules

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/SPIRV-Tools
Source0:        %url/archive/sdk-%{sdkver}.tar.gz#/SPIRV-Tools-sdk-%{sdkver}.tar.gz

Patch0:         0001-opt-fix-spirv-ABI-on-Linux-again.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
%if 0%{?rhel} == 7
BuildRequires:  python36-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  python3-rpm-macros
BuildRequires:  spirv-headers-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V..

%package        libs
Summary:        Library files for %{name}
Provides:       %{name}-libs%{?_isa} = %{version}

%description    libs
library files for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}

%prep
%autosetup -p1 -n SPIRV-Tools-sdk-%{sdkver}

%build
%__mkdir_p %_target_platform
pushd %_target_platform
%cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \
        -DSPIRV-Headers_SOURCE_DIR=%{_prefix} \
        -DPYTHON_EXECUTABLE=%{__python3} \
        -DSPIRV_TOOLS_BUILD_STATIC=OFF \
        -GNinja ..
%ninja_build
popd

%install
%ninja_install -C %_target_platform

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md CHANGES
%{_bindir}/spirv-as
%{_bindir}/spirv-cfg
%{_bindir}/spirv-dis
%{_bindir}/spirv-lesspipe.sh
%{_bindir}/spirv-link
%{_bindir}/spirv-lint
%{_bindir}/spirv-opt
%{_bindir}/spirv-reduce
%{_bindir}/spirv-val

%files libs
%{_libdir}/libSPIRV-Tools-diff.so
%{_libdir}/libSPIRV-Tools-link.so
%{_libdir}/libSPIRV-Tools-lint.so
%{_libdir}/libSPIRV-Tools-opt.so
%{_libdir}/libSPIRV-Tools-shared.so
%{_libdir}/libSPIRV-Tools-reduce.so
%{_libdir}/libSPIRV-Tools.so

%files devel
%{_includedir}/spirv-tools/
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{_libdir}/pkgconfig/SPIRV-Tools.pc

%changelog
* Wed Feb 15 2023 Dave Airlie <airlied@redhat.com> - 2023.1-2
- fix spirv-tools ABI break

* Mon Feb 13 2023 Dave Airlie <airlied@redhat.com> - 2023.1-1
- Update to 1.3.239.0 SDK version

* Wed Aug 24 2022 Dave Airlie <airlied@redhat.com> - 2022.2-2
- Update to 1.3.224.0 SDK version

* Mon Jun 20 2022 Dave Airlie <airlied@redhat.com> - 2022.2-1
- Update to 1.3.216.0 SDK version

* Mon Feb 21 2022 Dave Airlie <airlied@redhat.com> - 2022.1-1
- Update to 1.3.204.0 SDK version

* Thu Jan 28 2021 Dave Airlie <airlied@redhat.com> - 2020.5-3
- Update to 1.2.162.0 SDK version

* Wed Aug 05 2020 Dave Airlie <airlied@redhat.com> - 2020.5-1
- update to latest upstream

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 2019.5-1
- update to latest upstream

* Sat Dec 07 2019 Dave Airlie <airlied@redhat.com> - 2019.4-2
- rebuild for 8.2.0

* Tue Nov 12 2019 Dave Airlie <airlied@redhat.com> - 2019.4-1
- latest upstream snapshot

* Sun Aug 04 2019 Dave Airlie <airlied@redhat.com> - 2019.4-0.1
- Update to latest upstream for glslang
- drop spirv-stats as per upstream.

* Thu Mar 07 2019 Dave Airlie <airlied@redhat.com> - 2019.1-1
- Update to 2019.1 release

* Mon Jul 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.4-1
- Update to 2018.4 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.0-0.3.20180407.git26a698c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Dave Airlie <airlied@redhat.com> - 2018.3.0-0.2.20180407.git26a698c
- Move to python3 and drop the simplejson buildreq.

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.3.0-0.1.20180407.git26a698c
- Bump version to 2018.3.0 to match .pc files

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.4.20180407.git26a698c
- Bump provides to 2018.3.0

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.3.20180407.git26a698c
- Update for vulkan 1.1.73.0

* Wed Feb 14 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.2.20180205.git9e19fc0
- Add isa to the provides

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.1.20180205.git9e19fc0
- Fix version
- Fix pkgconfig file
- Add version provides to -libs package

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.5.20180205.git9e19fc0
- Update for vulkan 1.0.68.0
- Try building as shared object
- Split libs into -libs subpackage

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.4.20171023.git5834719
- Use ninja to build

* Mon Jan 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.3.20171023.git5834719
- Add python prefix to fix the stupid Bodhi tests

* Wed Jan 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.2.20171023.git5834719
- Split binaries into main package

* Thu Jul 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.1.20171023.git5834719
- First build

