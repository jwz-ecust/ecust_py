sum=0
while [ $# -gt 0 ]; do
  i=$1
  sum=$( echo "$sum +$i" | bc )
  shift
done
echo $sum
echo $#
