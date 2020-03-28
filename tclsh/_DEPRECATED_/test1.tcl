#!/usr/bin/tclsh
#
#   Date 2020-03-23T05:36:56
#   Purpose 
#

set asadict [ dict create CA California LA Louisana MS Missouri NY {New York}]

puts "asadict $asadict\n";

foreach k [dict keys $asadict] {
    puts "k $k\n"
}

dict for { k  a } $asadict {
    puts "k $k $a\n"
}


exit 0
