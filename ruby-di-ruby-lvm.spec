#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	di-ruby-lvm
Summary:	This is a fork of the ruby-lvm gem found at git://rubyforge.org/ruby-lvm.git
Name:		ruby-%{pkgname}
Version:	0.1.3
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	1a95892a53a34080d56abce8b5714e52
URL:		http://ruby-lvm.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-hoe < 4
BuildRequires:	ruby-hoe >= 3.0
BuildRequires:	ruby-rdoc < 4
BuildRequires:	ruby-rdoc >= 3.10
%endif
Requires:	ruby-di-ruby-lvm-attrib < 0.1
Requires:	ruby-di-ruby-lvm-attrib >= 0.0.3
Requires:	ruby-open4 >= 0.9.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a fork of the ruby-lvm gem found at
git://rubyforge.org/ruby-lvm.git.

The primary difference from upstream is that it depends on
di-ruby-lvm-attributes instead of ruby-lvm-attributes. This adds
support for lvm version 2.02.66(2). This is a wrapper for the LVM2
administration utility, lvm. Its primary function it to convert
physical volumes, logical volumes and volume groups into easy to use
ruby objects. It also provides a simple wrapper for typical
create/delete/etc operations. Due to a lack of LVM2 api this is a best
effort attempt at ruby integration but subject to complete replacement
in the future.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt History.txt Todo.txt
%{ruby_vendorlibdir}/lvm.rb
%{ruby_vendorlibdir}/lvm
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
%{_examplesdir}/%{name}-%{version}
