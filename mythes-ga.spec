Name: mythes-ga
Summary: Irish thesaurus
%define upstreamid 20071001
Version: 0.%{upstreamid}
Release: 11%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/thes_ga_IE_v2.zip
Group: Applications/Text
URL: http://borel.slu.edu/lsg/index-en.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: unzip
License: GFDL
BuildArch: noarch
Requires: mythes

%description
Irish thesaurus.

%prep
%setup -q -c

%build
for i in README_th_ga_IE_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ga_IE_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_ga_IE_v2.txt
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20071001-11
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 04 2010 Caolan McNamara <caolanm@redhat.com> - 0.20071001-6
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20071001-4
- tidy spec

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Caolan McNamara <caolanm@redhat.com> - 0.20071001-2
- fix typos

* Thu Dec 11 2008 Caolan McNamara <caolanm@redhat.com> - 0.20071001-1
- initial version
