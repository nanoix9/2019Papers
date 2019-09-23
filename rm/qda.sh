#!/bin/bash

bin_dir=$(dirname $0)

txt_dir=$bin_dir/devops-agile.log

for f in $(ls $txt_dir|grep -E '\d+-.*.txt$'); do
    path=$txt_dir/$f
    to_path=$(echo $path | sed -E 's/([0-9]+)[^\/]*\.txt$/\1.code.md/')
    echo "processing $path -> $to_path"
    [ -e $to_path ] && exit 1
    awk '{ if ($0 ~ /[^\w]+/) {print "> "$0} else {print }}' $path > $to_path
done