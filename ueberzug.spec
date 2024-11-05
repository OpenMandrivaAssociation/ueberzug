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
BuildRequires:  python3dist(meson-python)

%description
ueberzug is a command line util which allows to
display images in combination with X11.

#--------------------------------------------------------------
%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%doc *.md
%{_bindir}/*
%{py_platsitedir}/*
