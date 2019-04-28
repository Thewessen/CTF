#!/bin/bash

file="password.x.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a"
dir="passwd"
i=1
extract=true

while $extract; do
  extract=false
  while [ -n "$(file $dir$i/$file | grep -o "Zip archive data")" ]; do
    extract=true
    i=$(expr $i + 1)
    echo "Creating new dir $dir$i..."
    mkdir $dir$i
    file=$(unzip $dir$(expr $i - 1)/$file | tail -1)
    file=${file:13}
    echo "New file is: $file"
    mv $file $dir$i
  done

  while [ -n "$(file $dir$i/$file | grep -o "XZ compressed data")" ]; do
    extract=true
    mv "$dir$i/$file" "$dir$i/$file.xz"
    file=$file.xz
    i=$(expr $i + 1)
    echo "Creating new dir $dir$i..."
    mkdir $dir$i
    cp $dir$(expr $i - 1)/$file $dir$i/
    unxz $dir$i/$file
    file=$(ls $dir$i/)
    echo "New file is: $file"
  done

  while [ -n "$(file $dir$i/$file | grep -o "bzip2 compressed data")" ]; do
    extract=true
    mv "$dir$i/$file" "$dir$i/$file.bz2"
    file=$file.bz2
    i=$(expr $i + 1)
    echo "Creating new dir $dir$i..."
    mkdir $dir$i
    cp $dir$(expr $i - 1)/$file $dir$i/
    bzip2 -d $dir$i/$file
    file=$(ls $dir$i/)
    echo "New file is: $file"
  done

  while [ -n "$(file $dir$i/$file | grep -o "gzip compressed data")" ]; do
    extract=true
    mv "$dir$i/$file" "$dir$i/$file.gz"
    file=$file.gz
    i=$(expr $i + 1)
    echo "Creating new dir $dir$i..."
    mkdir $dir$i
    cp $dir$(expr $i - 1)/$file $dir$i/
    gzip -d $dir$i/$file
    file=$(ls $dir$i/)
    echo "New file is: $file"
  done
done
