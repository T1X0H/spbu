#!/bin/bash

n=0
mn=1
h=false
flag=true
dirs=()



while [[ $# -gt 0 ]]; do
	if $flag; then
		if [[ "$1" == "--usage" ]]; then
			echo "$0 [--help] [-h] [-n] [-s mn] [--] [dir...]"
			exit 0
		elif [[ "$1" == "--help" ]]; then 
			echo "vers 1.5, make by Treskin"
			exit 0
		elif [[ "$1" == "-h" ]]; then
			h=true
			shift
		elif [[ "$1" =~ ^-[0-9]+$ ]]; then
			str="$1"
			n=${str:1}
			shift
		elif [[ "$1" == "-s" ]]; then
			mn=$2
			shift 2
		elif [[ "$1" == "--" ]]; then
			flag=false
			shift
		else
			echo "Error. No such opition" >&2
			exit 1
		fi
	else
		if [[ "$1" == -* ]]; then
            dirs+=("./$1")
        else
            dirs+=("$1")
        fi
		shift
	fi
done



if [[ ${#dirs[@]} -eq 0 ]]; then
    dirs=(.)
fi



find "${dirs[@]}" -type f -size +"${mn}c" -printf "%s %p\n" | sort -nr | {
    if $h; then
        while read -r size path; do
            h_size=$(numfmt --to=iec-i --suffix=B "$size")
            echo "$h_size $path"
        done
    else
        cat
    fi
} | {
    if [[ $N -gt 0 ]]; then
        head -n "$n"
    else
        cat
    fi
}



exit 0







