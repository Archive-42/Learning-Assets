{#main}
WHAT IS AN ALGORITHM? {#what-is-an-algorithm .titles}
=====================

The best definition of algorithms that I have come across is the
following:

**Algorithms are a series of steps or rules for solving a computational
problem.**

A **computational problem** is a collection of questions that computers
might be able to solve.

An example of a simple algorithm could be one used by a coffee maker, it
might look something like this:

{.code-div}

        if (clock.getTime() == 7am){
            coffeMaker.boilWater();

            if(water.isBoiled()){
                coffeMaker.addCoffee();
                coffeMaker.pourCoffee();
            }

        } else{
            coffeMaker.doNothing();
        }



{.division}

# ALGORITHM EFFICIENCY {#algorithm-efficiency .titles}

Algorithm efficiency is the study of the amount of resources used by an
algorithm. The less resources used by the algorithm the more efficient
it is. Nevertheless, to have a good comparison between different
algorithms we can compare based on the resources it uses: how much time
it needs to complete, how much memory it uses to solve a problem or how
many operations it must do in order to solve the problem

**Time efficiency:** a measure of amount of time an algorithm takes to
solve a problem.

**Space efficiency:** a measure of the amount of memory an algorithm
needs to solve a problem.

**Complexity theory:** a study of algorithm performance based on cost
functions of statement counts.

{.division}
