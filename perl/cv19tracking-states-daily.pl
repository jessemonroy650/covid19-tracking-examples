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
my $url      = 'https://covidtracking.com/api/states/daily';
my $jsonfile = get $url;

print "url $url\n";
print "jsonfile $jsonfile\n";
# decode the JSON file
$json_array =  decode_json($jsonfile);
# get length of the array
$ja_length  =  @{$json_array};
# make a copy of the array
@ja_copy    =  @{$json_array};

$item_index = 0;
foreach $item_ja (@ja_copy) {
    print "\n** $item_index **\n";
    # extract the keys from the JSON item, now an "associative arrays"
    @thekeys = sort keys $item_ja;
    #
    print "date $item_ja->{'date'}\n";
    print "state $item_ja->{'state'}\n";
    # Retrieving from a Hash in Insertion Order
    # https://www.oreilly.com/library/view/perl-cookbook/1565922433/ch05s07.html
    foreach $ky (@thekeys) {
        print "$ky $item_ja->{$ky}\n";
    }
    $item_index++;
}

print "\n";

