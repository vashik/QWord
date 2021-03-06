Name: qword
Version: 2.0
Release: 1
Summary: Application for learning foreign words
Group: Education/Languages
License: GPL
Source0: qword-2.0.tar.gz
Source1: qword.desktop
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

#########################################################################################  
# SuSE, openSUSE  
#########################################################################################  
%if 0%{?suse_version}  
#BuildRequires:  update-desktop-files  
BuildRequires:  desktop-file-utils  
BuildRequires:  libqt4-devel  
%endif  
 #########################################################################################  
# Fedora, RHEL or CentOS  
#########################################################################################  
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}  
BuildRequires:  qt4-devel  
BuildRequires:  desktop-file-utils  
%endif  

%description
This package basically does nothing, but it potentially could
do something useful.


%prep
%setup -q -n %{name}-%{version}

%build
qmake
make %{?jobs:-j%jobs}

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/{bin,lib,share}
mkdir -p $RPM_BUILD_ROOT/usr/local/share/QWord
mkdir -p $RPM_BUILD_ROOT/usr/local/share/man/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install QWord $RPM_BUILD_ROOT/usr/local/bin
install images/test1.svg $RPM_BUILD_ROOT/usr/local/share/QWord

%if 0%{?suse_version}
#  %suse_update_desktop_file -c qword QWord "Learning foreign words" QWord "" Education
 %suse_update_desktop_file -i qword Education
#  desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ --add-category Education --add-category Languages qword.desktop
%elseif 0%{?fedora_version}
  desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ --add-category Education --add-category Languages qword.desktop
%endif

%files
%defattr(-,root,root)
/usr/local/bin/QWord
/usr/local/share/QWord/test1.svg
/usr/share/applications/qword.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri May 15 2009 Ivan Selchenkov
- Tray mode added
- Some interface and error correction
* Tue May 12 2009 Ivan Selchenkov
- Initial build


