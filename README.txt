This is a DVD renting system.

Supports adding DVD's, customers,
renting and returning DVD's, and 
finding rental information from
either the DVD or Customer object.

The inventory is a dictionary
where the key is the DVD UPC code,
and the value is the DVD object.
This provides O(1) lookup.

The number of copies of a particular
DVD, and thus it's rental availability,
is maintained by the DVD object.
Total copies are not counted at
this time, but can be done quite
easily.

A DVD object knows who its
current renters are, and a
Customer object knows which DVD's
it is has rented.

A test run is included at the end 
of the script.

Usage: 

        $ python rentingSystem.py