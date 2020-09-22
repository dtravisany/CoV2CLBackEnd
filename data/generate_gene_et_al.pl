use strict;

open L,shift;

my $gid=1;
my $stemid=1;
my $utr=1;

while(<L>){
	chomp;
	my @data=split("\t",$_);
	if ($data[2] eq "gene"){
		my @elsevalues;
		my @feats=split(";",$data[8]);
		foreach my $feat(@feats){
		 	my ($idfeat,$value)=split("=",$feat);
			push (@elsevalues,$value);
		}
		my $last=join("\t",$elsevalues[0],$elsevalues[1],$elsevalues[2],$elsevalues[4],$elsevalues[6]);
		print join("\t",$gid,$data[3],$data[4],$data[6],$last)."\n";
		$gid++;
	}

}
close L;



