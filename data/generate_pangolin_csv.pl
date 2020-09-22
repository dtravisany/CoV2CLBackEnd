use strict;

open L,shift;

my $i=1;
my $h;

while(<L>){

	chomp;
	next if $_ =~m/^Lineage/;
	my ($lin_not_fix,$not,$spa)=split("\t",$_);
	my $lin = $lin_not_fix;
	$lin =~s/\*//g;
	my @data=split('\.',$lin);
	if(scalar(@data)==1){
		$h->{$lin_not_fix}->{id}=$i++;
		$h->{$lin}->{father}="";
		print join("\t",$h->{$lin_not_fix}->{id},$lin_not_fix,$h->{$lin}->{father},$spa)."\n";
	}elsif(scalar(@data)==2){
		$h->{$lin_not_fix}->{id}=$i++;
		$h->{$lin}->{father}=$h->{$data[0]}->{id};
		print join("\t",$h->{$lin_not_fix}->{id},$lin_not_fix,$h->{$data[0]}->{id},$spa)."\n";
	}elsif(scalar(@data)>=3){
		$h->{$lin_not_fix}->{id}=$i++;
		$h->{$lin}->{father}=$h->{$data[0].".".$data[1]}->{id};
		print join("\t",$h->{$lin_not_fix}->{id},$lin_not_fix,$h->{$data[0].".".$data[1]}->{id},$spa)."\n";
	}
}

