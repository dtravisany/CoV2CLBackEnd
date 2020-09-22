from django.db import models

# Create your models here.
from django.db import models


class Region(models.Model):
    Name = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Country(models.Model):
    Name = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE,related_name="reg")


class Division(models.Model):
    Name = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name="cou")


class Location(models.Model):
    Name = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    Division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="div")


class Sample(models.Model):
    internal_id = models.CharField(max_length=150, null=True)
    strain = models.CharField(max_length=150)
    virus = models.CharField(max_length=150)
    gisaid_epi_isl = models.CharField(max_length=150, null=True)
    genbank_accession = models.CharField(max_length=150, null=True)
    date = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, related_name="reg_sampled")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, related_name="cou_sampled", null=True)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING, related_name="div_sampled", null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name="loc_sampled", null=True)
    region_exposure = models.ForeignKey(Region, on_delete=models.DO_NOTHING, related_name="reg_exposure")
    country_exposure = models.ForeignKey(Country, on_delete=models.DO_NOTHING, related_name="cou_exposure", null=True)
    division_exposure = models.ForeignKey(Division, on_delete=models.DO_NOTHING, related_name="div_exposure", null=True)
    location_exposure = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name="loc_exposure", null=True)
    segment = models.CharField(max_length=100)
    length = models.IntegerField()
    host = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    originating_lab = models.CharField(max_length=300)
    submitting_lab = models.CharField(max_length=350)
    authors = models.CharField(max_length=350)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=350)
    date_submitted = models.DateField()


class GenomeSeq(models.Model):
    seq = models.TextField()


class Genome(models.Model):
    resumen = models.TextField()
    conclusiones = models.TextField()
    resultados = models.TextField()
    reads = models.IntegerField()
    General_run_summary = models.TextField(null=True)
    Basecall_summary = models.TextField(null=True)
    Basecalled_reads_length = models.TextField(null=True)
    Basecalled_reads_PHRED_quality = models.TextField(null=True)
    Basecalled_reads_length_vs_reads_PHRED_quality = models.TextField(null=True)
    Output_over_experiment_time = models.TextField(null=True)
    Read_length_over_experiment_time = models.TextField(null=True)
    Read_quality_over_experiment_time = models.TextField(null=True)
    Channel_activity_over_time = models.TextField(null=True)
    nanoQC_field = models.TextField(null=True)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name="sample")
    seq = models.ForeignKey(GenomeSeq, on_delete=models.CASCADE, related_name="sequence")


class CDSSeq(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    strand = models.CharField(max_length=1)
    aac = models.TextField()
    genome = models.ForeignKey(GenomeSeq, on_delete=models.CASCADE, related_name="genomeseq")


class CDS(models.Model):
    name = models.CharField(max_length=200)
    genome = models.ForeignKey(Genome, on_delete=models.DO_NOTHING, related_name="genome")
    seq = models.ForeignKey(CDSSeq, on_delete=models.DO_NOTHING, related_name="CDSSeq")


class snv(models.Model):
    models.ForeignKey(CDSSeq, on_delete=models.DO_NOTHING, related_name="CDSSeq")
    position = models.IntegerField()
    reference = models.ForeignKey(Genome, on_delete=models.CASCADE, related_name="greference")
    query = models.ForeignKey(Genome, on_delete=models.CASCADE, related_name="gquery")
    original = models.CharField(max_length=1)
    change = models.CharField(max_length=1)
