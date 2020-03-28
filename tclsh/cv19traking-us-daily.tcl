#!/usr/bin/tclsh
#
#   Date 2020-03-23T05:36:56
#   Purpose 
#
package require http
package require json

set dataurl http://covidtracking.com/api/us/daily

#
#   https://wiki.tcl-lang.org/page/Download+file+via+HTTP
#
proc getPage { url } {
    set token [::http::geturl $url]
    set data [::http::data $token]
    ::http::cleanup $token          
    return $data
}

##
##
##
puts "URL $dataurl\n";

# get the JSON data
set jsondata [ getPage $dataurl ];

# DEBUUG
#puts "jsondata $jsondata\n" ;

#
# http://www.wellho.net/resources/ex.php4?item=t241/getpagejson
#
set asadict [::json::json2dict $jsondata];

# DEBUUG
#puts "asadict $asadict\n";
# DEBUUG
#puts [dict size $asadict];

# Validate
#puts [ llength $asadict ];


set excludeFromR [list posNeg total notes]
# maybe hash lastModified
set excludeFromR ""

# It may actually be a list.
foreach rek $asadict {
    puts ""
    #puts "rek $rek\n";
    #puts [ dict keys $rek ];
    foreach k [ dict keys $rek ] {
        if {[lsearch $excludeFromR $k  ] >= 0 } {
            #puts "found \"total\""
        } else {
            puts "$k [dict get $rek $k]";
        }
    }
    #break;
}

exit 0
