

HUGO_VERSION:=0.81.0


install-debian install-ubuntu: 
	@echo Requesting sudo to install and  download Hugo v$(HUGO_VERSION)
	sudo wget https://github.com/gohugoio/hugo/releases/download/v$(HUGO_VERSION)/hugo_$(HUGO_VERSION)_Linux-64bit.deb
	@echo Installing ...
	sudo dpkg -i hugo_$(HUGO_VERSION)_Linux-64bit.deb
	@echo Removing .deb file
	rm -Rf *.deb*
	@echo Installed:
	hugo version	



build:
	hugo


serve:
	hugo server
