#/bin/sh

for d in */ ; do
	if [ $d == rv_* ]; then
    	echo "$d"
    fi
done
