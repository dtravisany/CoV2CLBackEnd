use strict;
use warnings;

use DBI;
my $dns="DBI::mysql::cov2cl";

my $username="cov2admin";
my $password="cov2dev";

my %attr = {	PrintError=>0,
		RaiseError=>1};

my $dbh = $DBI->connect($dns,$username,$password,\%attr);

$dbh->disconnect();


open L,shift();

while(<L>){
	next if $_ =~m/^#/;
	chomp;
	my @data=split("\t",$_);
	if($data[3] ne '--'){
		my @mutations =split(",",$data[2]);
		my @ids;
		foreach my $ele(@mutations){
			push @ids,&query_links_by_target($dbh,"mutation",$value);
		}
	}

}
close L;

sub get_links{
	 my $cmd = '';
	 my @links;
	 # get links from the command line
	 my($title,$url,$target);

	 # repeatedly ask for link data from command line
	 do{
		 say "title:";
		 chomp($title = <STDIN>); 

		 say "url:";
		 chomp($url = <STDIN>);

		 say "target:";
		 chomp($target = <STDIN>);

		 #
		 my %link = (title=> $title, url=> $url, target=> $target);

		 push(@links,\%link);

		 print("\nDo you want to insert another link? (Y/N)?");
		 chomp($cmd = <STDIN>);
		 $cmd = uc($cmd);
	 }until($cmd eq 'N');

	 return @links;
}


sub query_links_by_target{
	# query from the links table by target

	my ($dbh,$table,$target) = @_;
	my $sql = "SELECT id
	FROM $table WHERE name = ?";
	my $sth = $dbh->prepare($sql);

	# execute the query
	$sth->execute($target);
	my $id;
	while(my @row = $sth->fetchrow_array()){
		$id=$row[0];
	}
	$sth->finish();
	return $id;
}


