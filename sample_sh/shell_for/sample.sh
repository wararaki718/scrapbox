#!/bin/bash

# enumerate numbers
for i in 1 2 3
do
    echo $i
done

# refs params
NUMS="
1
2
3
"
for i in $NUMS
do
    echo $i
done


# range
for i in `seq 1 3`
do
    echo $i
done

echo "DONE"