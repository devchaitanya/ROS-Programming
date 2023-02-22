<h3>1. A packet publisher publishes the name of the packet (string format)</h3>

<h3>2. A security publisher (string) converts the above packet into encrypted packet (usually the ceaser cipher, VITCC is equivalent to YLWFF).</h3>

<h3>3. A third publisher is  a Int32 publisher, publishes an integer number with number of packets.</h3> 

<h3>4.There is only one subscriber, that tells the "Number of packets encrypted" after all the publishers publishes.
i.e P1 AND P2 AND P3 => Subscriber
</h3>
