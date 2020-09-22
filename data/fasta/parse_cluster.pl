use strict;

open L,shift;

my $name;
while(<L>){
	chomp;
	if ($_ =~m/^>(.*)/){
		$name=$1;
	#0       29983aa, >Chile/Santiago_58/2020... *
	}elsif($_ =~m/(\d+)\s+(d+)/){


	}
	

}
close L;



