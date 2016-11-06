echo "If you want to get cif file for all the structures produced by USPEX press 1 or for best gathered structures press 2"
read n
if [ "$n" = "1" ]
then
m="Individuals"
echo $m
l="gatheredPOSCARS"
elif [ "$n" = "2" ]
then
m="BESTIndividuals"
l="BESTgatheredPOSCARS"
fi
awk '{print $2"          " $7"             " $15"            "$5}' $m > structures
a=`wc -l structures`
tail -n +3  structures > structures-new
column -t structures-new > structures
rm structures-new

x=`wc -l structures | awk '{print $1}'`
a=`awk '{print $1}' structures`
b=`awk '{print $4}' structures`

set -- $a
set -- $b

echo $x
for i in `seq 1 $x`
do

p=`echo $a | cut -d" " -f$i`
q=`echo $b | cut -d" " -f$i`
echo "i am p $p , i am q $q"
grep -A $((7+q)) -w "EA$p" $l > POSCAR$p
python vasp2cif.py POSCAR$p

done
