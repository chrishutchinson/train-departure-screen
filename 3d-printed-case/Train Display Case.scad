$fa = 1;
$fs = 0.4;

difference(){
    cube([105,2,39]);
    translate([16.70,0,11.34])
        cube([70.10,2,19.26]);
}
rotate([270,0,0])
    translate([5.25,-5,2])
        cylinder(h=6,r=1.5);
rotate([270,0,0])
    translate([5.25,,-34,2])
        cylinder(h=6,r=1.5);
rotate([270,0,0])
    translate([99.25,-5,2])
        cylinder(h=6,r=1.5);
rotate([270,0,0])
    translate([99.25,-34,2])
        cylinder(h=6,r=1.5);

