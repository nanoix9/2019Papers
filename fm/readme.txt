ENSE803 ASSESSMENT 2 TEAM 1


TEAM MEMBERS:

Sherin Jacob
Maitreyee Pande
Stone Fang


NOTES:

In the simulation trace output files, some traces start with an initial drink
amount of 3. However, such setting is not suitable for simulation of the 4th 
scenario, which requires zero amount of a drink and we would have to purchase
3 extra times to run out that drink. As a result, in some cases the initial 
value is set to 1 so we can run out of the available drink in one extra round 
of purchase.


SUBMITTED FILES:

8 files in total in a zip file.

Model implementation in nuXmv with LTL specs:
    vending-machine.txt 

Simulation trace output of 5 scenarios:
    1-pay-clearwater-correct-output.txt
    2-pay-kiwicola-incorrect.txt
    3-selectdrink-error-output.txt
    4-no-more-clearwater.txt
    5-purchase-bolt-energy-and-clear-water.txt

LTL spec verification output (Formula go within the code):
    ltlspec-output.txt

Additional information
    readme.txt