Name:           ueberzug
Version:        18.3.2
Release:        2
Url:            https://github.com/ueber-devel/ueberzug/
Summary:        Ueberzug is a command line util to display images
License:        GPLv3
Group:          Development/Python
Source0:        https://github.com/ueber-devel/ueberzug/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python%{pyver}dist(pillow)
BuildRequires:  python%{pyver}dist(docopt)
BuildRequires:  python%{pyver}dist(attrs)
BuildRequires:  python%{pyver}dist(meson-python)

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
