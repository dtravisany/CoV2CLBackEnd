use strict;
use DBI;

open L,shift;
open X,shift;

my $h;
while(<X>){
	chomp;
	my ($name,$clade)=split("\t",$_);
	$h->{$name}=$clade;

}
close X;



my $dbh = DBI->connect("DBI:mysql:cov2seq",'cov2admin','cov2dev');

die "failed to connect to MySQL database:DBI->errstr()" unless($dbh);


sub get_ids{

	my $field=shift;
	my $table=shift;
	my $value=shift;


	# prepare SQL statement
	my $sth = $dbh->prepare("SELECT id FROM $table WHERE $field = ?") or die "prepare statement failed: $dbh->errstr()";

	$sth->execute($value) or die "execution failed: $dbh->errstr()"; 

	my $id;
	my $value;

	while(($id) = $sth->fetchrow()){                   
		$value=$id;;	
	}
	$sth->finish();
	return $value;
}





#strain[0]
#virus[1]
#gisaid_epi_isl[2]
#genbank_accession[3]       
#date[4]
#region[5]
#country[6]
#division[7]
#location[8]
#region_exposure[9] 
#country_exposure[10]      
#division_exposure[11]    
#segment[12]
#length[13]
#host[14]
#age[15]
#sex[16]
#pangolin_lineage[17]
#GISAID_clade[18]      
#originating_lab[19]
#submitting_lab[20]
#authors[21]
#url[22]
#title[23]  
#paper_url[24]       
#date_submitted[25]
my $i=1;
while(<L>){

	chomp;
	next if $_ =~m/strain\t/;
	my @data=split("\t",$_);
	my $region=&get_ids("name","cov2cl_region",$data[5]);	
	my $country=&get_ids("name","cov2cl_country",$data[6]);	
	my $division=&get_ids("name","cov2cl_division",$data[7]);	
	my $location=&get_ids("name","cov2cl_location",$data[8]);	
	my $region_ex=&get_ids("name","cov2cl_region",$data[5]);	
	my $country_ex=&get_ids("name","cov2cl_country",$data[6]);	
	my $division_ex=&get_ids("name","cov2cl_division",$data[7]);
	my $pangolin=&get_ids("lineage","cov2cl_pangolinlineage",$data[17]);
	my $gisaid=&get_ids("clade","cov2cl_gisaidclade",$data[18]);
	my $nextstrain=&get_ids("clade","cov2cl_nextstrainclade",$h->{$data[0]});
	#print join("\t",$data[17],$pangolin,$data[18],$gisaid)."\n";
	$nextstrain	="\\N" if $nextstrain eq "";
	$pangolin	="\\N" if $pangolin eq "";
	$gisaid		="\\N" if $gisaid eq "";
	$location	="\\N" if $location eq "";
	$division	="\\N" if $division eq "";
	$division_ex	="\\N" if $division_ex eq "";
	$country	="\\N" if $country eq "";
	$country_ex	="\\N" if $country_ex eq "";

	my $j=0;
	while($j<scalar(@data)){
		$data[$j] ="\\N" if $data[$j] eq "?";
		$j++;
	}

	print join ("\t",$i,"\\N",$data[0],$data[1],$data[2],$data[3],$data[4],$data[12],$data[13],$data[14],$data[15],$data[16],$data[19],$data[20],$data[21],$data[22],$data[23],$data[25],$country,$country_ex,$division,$division_ex,$location,$region,$region_ex,$gisaid,$nextstrain,$pangolin,$data[24])."\n";
		
	$i++;
}
close L;

$dbh->disconnect();
