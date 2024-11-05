Name:           ueberzug
Version:        18.3.0
Release:        1
Url:            https://github.com/ueber-devel/ueberzug/
Summary:        Ueberzug is a command line util to display images
License:        GPLv3
Group:          Development/Python
Source0:        https://github.com/ueber-devel/ueberzug/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3egg(setuptools)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(docopt)
BuildRequires:  python3dist(attrs)

%description
ueberzug is a command line util which allows to
display images in combination with X11.

#--------------------------------------------------------------
%prep
%autosetup -p1
# get ridd of env-script-interpreter
sed -i -e 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/g' %{pypi_name}/*.py
sed -i -e 's/^#!\/usr\/bin\/env bash/#!\/usr\/bin\/bash/g' %{pypi_name}/lib/*.sh

%build
%py_build

%install
%py_install

chmod +x %{buildroot}%{py_platsitedir}/ueberzug/__main__.py
chmod +x %{buildroot}%{py_platsitedir}/ueberzug/lib/lib.sh


%files
%doc *.md
%{_bindir}/*
%{py_platsitedir}/*
