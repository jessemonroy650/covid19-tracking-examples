#!/usr/bin/tclsh
#
#   Date 2020-03-23T05:36:56
#   Purpose 
#
package require http
package require json

set dataurl http://covidtracking.com/api/states

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

#puts "jsondata $jsondata\n" ;

#
# http://www.wellho.net/resources/ex.php4?item=t241/getpagejson
#
set asadict [::json::json2dict $jsondata];

#puts "asadict $asadict\n";

puts [dict size $asadict];
puts [ llength $asadict ];

foreach rek $asadict {
    puts "rek $rek\n";
    puts [ dict keys $rek ]
    break;
}

exit 0


#foreach k [dict keys $asadict] {
#    #puts "k $k\n";
#    puts [ dict get $asadict $k ]
#    puts [ dict keys $k ]
#    puts [ dict get $k state ]
#    puts [ dict get $k positive ]
#    puts [ dict get $k grade ]
#    puts [ dict get $k totalTestResults ]
#    break;
#}


