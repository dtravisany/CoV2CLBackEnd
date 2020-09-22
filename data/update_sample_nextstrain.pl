use strict;
use DBI;


my $dns = "DBI:mysql:database=cov2seq;host=localhost";
my $dbh = DBI->connect($dns, "cov2admin","cov2dev");

open L,shift;

while(<L>){
chomp;
my @data=split("\t",$_);

next if $data[0] eq "Strain";
my $sth = $dbh->prepare(
    'SELECT id FROM cov2cl_nextstrainclade WHERE clade = ?')
    or die "prepare statement failed: $dbh->errstr()";
$sth->execute($data[1]) or die "execution failed: $dbh->errstr()";
while (my $ref = $sth->fetchrow_hashref()) {
	my $tth = $dbh->prepare(
	'UPDATE cov2cl_sample SET nextstrain_id = ? WHERE strain = ?')or die "execution failed: $dbh->errstr()";

$tth->execute($ref->{id},$data[0]);
$tth->finish;
}
$sth->finish;



}





