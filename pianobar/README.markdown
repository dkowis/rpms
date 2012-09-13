# RPM Building instructions:

## Prereqs
$ yum groupinstall "Development Tools"
$ yum install rpmdevtools
$ rpmdev-setuptree

## Install the rpmfusion repo!


## Build RPM
1. update pianobar.spec with new version and source tarball name
2. Fetch source from the site!
3. create source tarball and place in ~/rpmbuild/SOURCES/ 
4. cd ~/rpmbuild/SPECS/
5. $ rpmbuild -ba pianobar.spec

Two rpm files are generated and placed into:
~/rpmbuild/RPMS/{arch}
~/rpmbuild/SRPMS/

To install
yum localinstall <teh rpm>
