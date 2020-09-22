use strict;

open L, shift;
open W, shift;

my $h;

while(<L>){

	chomp;
	my @data=split("\t",$_);
	$h->{$data[1]}->{lat}=$data[2];
	$h->{$data[1]}->{lon}=$data[3];
}
close L;

while(<W>){

	chomp;
	my @data=split("\t",$_);
		
}
close W;





