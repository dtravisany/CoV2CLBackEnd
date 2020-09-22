use strict;

open L, shift; 
open W, shift;
open X, shift;

my $h;

my @region;

while(<L>){

	chomp;
	my @data=split("\t",$_);
	$h->{$data[1]}=$data[0];	
}
close L;
my $latlon;
my $i=1;
while(<X>){

	chomp;
	my @data=split("\t",$_);
	$latlon->{$data[1]}->{lat}=$data[2];
	$latlon->{$data[1]}->{lon}=$data[3];
}
close X;

my $countries;
my $seen;
while(<W>){

	chomp;
	my @data=split("\t",$_);
	next unless $h->{$data[6]};
	next unless $latlon->{$data[7]};
	next if $seen->{$data[7]}==1;
	$seen->{$data[7]}=1;
	print join("\t", $i++,$data[7], $latlon->{$data[7]}->{lat}, $latlon->{$data[7]}->{lon},$h->{$data[6]})."\n";
}
close W;





