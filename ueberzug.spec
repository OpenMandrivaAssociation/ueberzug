Name:           python-%{pypi_name}
Version:        18.1.9
Release:        3
Url:            https://github.com/seebye/ueberzug
Summary:        Ueberzug is a command line util to display images
License:        GPLv3
Group:          Development/Python
Source0:        https://files.pythonhosted.org/packages/source/u/ueberzug/%{pypi_name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python3egg(pillow)
BuildRequires:  python3egg(docopt)
BuildRequires:  python3egg(attrs)


%description
ueberzug is a command line util which allows to
display images in combination with X11.

#--------------------------------------------------------------
%package -n python3-%{pypi_name}
Summary:        Ueberzug is a command line util to display images
Group:          Development/Python
%rename         python-%{pypi_name}

%description -n python3-%{pypi_name}
ueberzug is a command line util which allows to
display images in combination with X11.

%files -n python3-%{pypi_name}
%doc *.md
%{_bindir}/*
%{py3_platsitedir}/*

#--------------------------------------------------------------
%prep
%setup -qn %{pypi_name}-%{version}
# get ridd of env-script-interpreter
sed -i -e 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/g' %{pypi_name}/*.py
sed -i -e 's/^#!\/usr\/bin\/env bash/#!\/usr\/bin\/bash/g' %{pypi_name}/lib/*.sh

%build
%py3_build

%install
%py3_install

chmod +x %{buildroot}%{py3_platsitedir}/ueberzug/__main__.py
chmod +x %{buildroot}%{py3_platsitedir}/ueberzug/lib/lib.sh
