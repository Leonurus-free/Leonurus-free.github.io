# ubuntu查看序列号

~~~
sudo lshw -class disk
~~~

~~~
 *-disk                    
       description: SCSI Disk
       product: MR9364-8i
       vendor: AVAGO
       physical id: 2.0.0
       bus info: scsi@0:2.0.0
       logical name: /dev/sda
       version: 4.68
       serial: 00748d35173140fc2df033ef0ab00506
       size: 3725GiB (3999GB)
       capabilities: gpt-1.00 partitioned partitioned:gpt
       configuration: ansiversion=5 guid=cb126a62-7b99-42f8-ae81-f783e2e4cc90 logicalsectorsize=512 sectorsize=512

~~~

