# Geekbrains. Введение в Linux и облачные вычисления
## Урок 6. Обзор дополнительных возможностей AWS для работы с данными

## Практическое задание
1. Создать AMI на основе имеющегося у вас инстанса.
2. Создать новый инстанс на основе AMI, сделанного в предыдущем задании.
Проверить, присутствуют ли на новом инстансе программы,
установленные на исходном инстансе.
3. Добавить новый диск к используемому инстансу.
Проверить доступ к этому диску и создать на нем текстовый файл test.txt,
содержащий слово test.
Затем создать новый инстанс,
отсоединить диск от старого и подсоединить к новому.
Проверить наличие на диске файла test.txt
и просмотреть его в текстовом редакторе nano.

## Решение
1.  Create an AMI based on the existing instance:
is not scriptable.
2.  Create a new instance based on the AMI made previously:
is not scriptable.
3.  Add a new disk to the used instance.

    Builds file systems
    on a couple of volumes attached to used instance:

    ```
    $ lsblk | grep xvd
    
    xvda    202:0    0    8G  0 disk 
    └─xvda1 202:1    0    8G  0 part /
    xvdf    202:80   0    1G  0 disk 
    xvdg    202:96   0    1G  0 disk 
    
    $ sudo mkfs --type ext4 /dev/xvdf
    
    mke2fs 1.45.5 (07-Jan-2020)
    Creating filesystem with 262144 4k blocks and 65536 inodes
    Filesystem UUID: 3fb2cb35-ee8d-459d-881b-28b168bdb1df
    Superblock backups stored on blocks: 
	    32768, 98304, 163840, 229376

    Allocating group tables: done                            
    Writing inode tables: done                            
    Creating journal (8192 blocks): done
    Writing superblocks and filesystem accounting information: done

    $ sudo mkfs --type xfs /dev/xvdg
    
    meta-data=/dev/xvdg              isize=512    agcount=4, agsize=65536 blks
             =                       sectsz=512   attr=2, projid32bit=1
             =                       crc=1        finobt=1, sparse=1, rmapbt=0
             =                       reflink=1
    data     =                       bsize=4096   blocks=262144, imaxpct=25
             =                       sunit=0      swidth=0 blks
    naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
    log      =internal log           bsize=4096   blocks=2560, version=2
             =                       sectsz=512   sunit=0 blks, lazy-count=1
    realtime =none                   extsz=4096   blocks=0, rtextents=0

    $ sudo file --special-files /dev/xvd*
    
    /dev/xvda:  DOS/MBR boot sector
    /dev/xvda1: Linux rev 1.0 ext4 filesystem data, UUID=9451d968-8716-47ca-84d5-68b5c79f61e8, volume name "cloudimg-rootfs" (needs journal recovery) (extents) (64bit) (large files) (huge files)
    /dev/xvdf:  Linux rev 1.0 ext4 filesystem data, UUID=3fb2cb35-ee8d-459d-881b-28b168bdb1df (extents) (64bit) (large files) (huge files)
    /dev/xvdg:  SGI XFS filesystem data (blksz 4096, inosz 512, v2 dirs)
    ```
    
    Shares a couple of directories
    intended for file systems mounting:
    
    ```
    $ sudo mkdir /mnt/vol1 /mnt/vol2
    
    $ ls -l /mnt
    
    total 4
    drwxr-xr-x 3 root root 4096 Jul 27 12:18 vol1
    drwxr-xr-x 2 root root    6 Jul 27 12:18 vol2
    
    $ sudo chown root:users /mnt/vol?
    
    $ sudo chmod g+=w /mnt/vol?
    
    $ ls -l /mnt
    
    total 4
    drwxrwxr-x 3 root users 4096 Jul 27 12:18 vol1
    drwxrwxr-x 2 root users    6 Jul 27 12:18 vol2

    $ whoami
    
    ubuntu
    
    $ sudo usermod --append --groups users ubuntu

    $ groups ubuntu
    
    ubuntu : ubuntu adm dialout cdrom floppy sudo audio dip video plugdev users netdev lxd
    ```
    
    Mounts a couple of made file systems
    in prepared directories:
    
    ```
    $ sudo mount --source /dev/xvdf --target /mnt/vol1
    
    $ sudo mount --source /dev/xvdg --target /mnt/vol2
    
    $ lsblk | grep xvd
    
    xvda    202:0    0    8G  0 disk 
    └─xvda1 202:1    0    8G  0 part /
    xvdf    202:80   0    1G  0 disk /mnt/vol1
    xvdg    202:96   0    1G  0 disk /mnt/vol2
    
    $ df -hT | grep xvd
    
    /dev/xvdf      ext4      976M  2.6M  907M   1% /mnt/vol1
    /dev/xvdg      xfs      1014M   40M  975M   4% /mnt/vol2
    ```
    
    Writes information
    about the corresponding devices
    to each of both volumes:
    
    ```
    $ df -hT | grep xvdf > /mnt/vol1/log
    
    $ blkid | grep xvdf >> /mnt/vol1/log
    
    $ cat /mnt/vol1/log 
    
    /dev/xvdf      ext4      976M  2.6M  907M   1% /mnt/vol1
    /dev/xvdf: UUID="3fb2cb35-ee8d-459d-881b-28b168bdb1df" TYPE="ext4"
    
    $ df -hT | grep xvdg > /mnt/vol2/log
    
    $ blkid | grep xvdg >> /mnt/vol2/log
    
    $ cat /mnt/vol2/log 
    
    /dev/xvdg      xfs      1014M   40M  975M   4% /mnt/vol2
    /dev/xvdg: UUID="6470f9b5-4060-4dda-8600-2bf8708254b7" TYPE="xfs"
    ```
    
    Adds a couple of created volumes to fstab:
    
    ```
    $ sudo cp /etc/fstab /etc/fstab.orig
    
    $ sudo su -
    
    # cat /mnt/vol?/log >> /etc/fstab
    
    # logout
    
    $ sudo vim /etc/fstab
    
    $ cat /etc/fstab
    
    LABEL=cloudimg-rootfs / ext4 defaults,discard 0 0
    UUID=3fb2cb35-ee8d-459d-881b-28b168bdb1df /mnt/vol1 ext4  defaults,nofail 0 2
    UUID=6470f9b5-4060-4dda-8600-2bf8708254b7 /mnt/vol2 xfs  defaults,nofail 0 2
    ```

    Unmount created volumes
    and mount again using fstab:
    
    ```
    $ sudo umount /mnt/vol?
    
    $ lsblk | grep xvd

    xvda    202:0    0    8G  0 disk 
    └─xvda1 202:1    0    8G  0 part /
    xvdf    202:80   0    1G  0 disk 
    xvdg    202:96   0    1G  0 disk 
    
    $ sudo mount --all

    $ lsblk | grep xvd

    xvda    202:0    0    8G  0 disk 
    └─xvda1 202:1    0    8G  0 part /
    xvdf    202:80   0    1G  0 disk /mnt/vol1
    xvdg    202:96   0    1G  0 disk /mnt/vol2
    
    $ cat /mnt/vol?/log

    /dev/xvdf      ext4      976M  2.6M  907M   1% /mnt/vol1
    /dev/xvdf: UUID="3fb2cb35-ee8d-459d-881b-28b168bdb1df" TYPE="ext4"
    /dev/xvdg      xfs      1014M   40M  975M   4% /mnt/vol2
    /dev/xvdg: UUID="6470f9b5-4060-4dda-8600-2bf8708254b7" TYPE="xfs"
    ```    

