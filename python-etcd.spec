%global srcname python-etcd

Name:           %{srcname}
Version:        0.4.3
Release:        1%{?dist}
Summary:        A python client library for etcd

License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}

# Using the github URL because the tarball file at pypi excludes
# the license file. But github tarball files are named awkwardly.
Source0:        https://github.com/jplana/%{srcname}/archive/%{version}.tar.gz

#VCS: git:https://github.com/jplana/python-etcd

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-dns
BuildRequires:  python-mock
BuildRequires:  python-nose
BuildRequires:  pyOpenSSL

BuildRequires:  python3-devel
BuildRequires:  python3-dns
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-pyOpenSSL

# Needed for tests
BuildRequires:  etcd

Patch1: python-etcd-0.4.3-auth-test-fail-workaround.patch

%description
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package -n python2-%{srcname}
Summary:        %summary
Requires:       etcd
Requires:       python-dns
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package -n python3-%{srcname}
Summary:        %summary
Requires:       etcd
Requires:       python3-dns
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%prep
%autosetup -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test

# This seems to require a newer python3-mock than what's currently available
# in F23, and even Rawhide.  If I let it download mock-1.3.0 from the Python
# Package Index (pypi) then tests pass.
#%%{__python3} setup.py test

%files -n python2-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/*

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
* Mon Feb 22 2016 Matthew Barnes <mbarnes@redhat.com> - 0.4.3-1
- Initial packaging.