infile=$1
outfile=$2
awk -F '\t' '{print $0"\t"substr($1,0,5)"\t"substr($1,5,2)"\t"substr($1,7,2)"\t"substr($1,9,2)}' $infile > $outfile
