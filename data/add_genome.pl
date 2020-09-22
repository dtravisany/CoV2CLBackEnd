use strict;

my $i=1;
while($i<188){
	chomp;
	print join("\t",$i,"\\N","\\N","\\N","\\N","\\N","\\N","\\N","\\N","\\N","\\N","\\N","\\N","\\N","\\N",$i)."\n";	
	$i++;
}
