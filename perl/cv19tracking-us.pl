#!/usr/bin/perl
#
#   2020-03-23T17:57:56
#
#   Dereferencing the reference after decoding the JSON can be tricky.
#   For veterans of perl, it's old hat.
#
#   get JSON from http://covidtracking.com/api/us
#
# Needed to install JSON on my machine 'sudo cpan JSON'
# https://stackoverflow.com/questions/11753529/install-perl-json-on-centos
use JSON;
#use Data::Dumper; # This is for debugging.

#
#   https://perlmaven.com/simple-way-to-fetch-many-web-pages
#
use LWP::Simple qw(get);
my $url      = 'https://covidtracking.com/api/us';
my $jsonfile = get $url;

print "url $url\n";
print "jsonfile $jsonfile\n";
$json_array =  decode_json($jsonfile);

# Retrieving from a Hash in Insertion Order
# https://www.oreilly.com/library/view/perl-cookbook/1565922433/ch05s07.html
#
foreach $k (keys $json_array->[0]) {
    print "$k $json_array->[0]->{$k}\n";
}

print "\n";

print "positive $json_array->[0]->{'positive'}";
print "\n";

