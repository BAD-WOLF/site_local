sudo softwareupdate -ia && xcode-select --install && sudo pip install --upgrade pip && brew install python3 && brew install curl

echo -n "

[1] PHP 7.3 (Next stable) - 10.10 and later
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.3

[2] PHP 7.2 (Current stable) - 10.10 and later
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.2

[3] PHP 7.1 (Old stable) - 10.10 and later
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.1

[4] PHP 7.0 (Old stable) - 10.10 and later
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.0

[5] PHP 5.6 (Old stable) - 10.8 and later
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.6

[6] PHP 5.5 (End of life) - All OS X versions
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.5

[7] PHP 5.4 (End of life) - All OS X versions
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.4

[8] PHP 5.3 (End of life) - All OS X versions
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.3

->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<
It will ask you for your password. We install the packager in /usr/local/packer and PHP into /usr/local/php5 and for this, we need your password. We don't do anything bad with it.


>> "
read number

command="curl -o curl_mac_os_x.sh -s https://php-osx.liip.ch/install.sh && bash -s"

case "$number" in
	"1")
		eval "$command 7.3 curl_mac_os_x.sh";
	;;
	"2")
		eval "$command 7.2 curl_mac_os_x.sh";
	;;
	"3")
		eval "$command 7.1 curl_mac_os_x.sh";
	;;
	"4")
		eval "$command 7.0 curl_mac_os_x.sh";
	;;
	"5")
		curl -s https://php-osx.liip.ch/install.sh | bash -s 5.6;
	;;
	"6")
		curl -s https://php-osx.liip.ch/install.sh | bash -s 5.5;
	;;
	"7")
		curl -s https://php-osx.liip.ch/install.sh | bash -s 5.4;
	;;
	"8")
		curl -s https://php-osx.liip.ch/install.sh | bash -s 5.4;
esac

