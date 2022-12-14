#! /bin/bash

cd $(dirname $0)

ln -s $(pwd) mysql-server/storage/ci_example

cmake -S ./mysql-server -B build -DDOWNLOAD_BOOST=1 -DWITH_BOOST=boost
cmake --build build -t ci_example # use `-t` to build the storage engine alone

sudo cp build/plugin_output_directory/ha_ci_example.so $(echo "SHOW VARIABLES LIKE 'plugin_dir';" | mysql -uroot -proot -N | awk '{print $2}')
echo "INSTALL PLUGIN ci_example SONAME 'ha_ci_example.so'" | mysql -uroot -proot
