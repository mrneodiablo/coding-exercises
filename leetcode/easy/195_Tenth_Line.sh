if [[ $(wc -l file.txt | awk '{print $1}') -lt 10 ]] 
then
    exit 0
else
    cat file.txt | head -n 10 | tail -n 1
fi

----
# another faster solution
tail -n+10 file.txt | head -n1
