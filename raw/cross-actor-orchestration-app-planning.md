Description of Problem:

16.7% miles run are empty (ATRI, 2025). 





Interesting context of where the market is going: https://www.globaltrademag.com/4-trends-reshaping-the-last-mile-in-2026/





Questions for Mat:

What types of problems can surface downstream, from sacrifices along the triangle of profit-service-risk? 

Risk: HOS violations, driver risk;

What are hours of service requirements? This must be factored into the model. 

What is trailer pooling?

Why are ports such a bad environment?

What other environments are there? 

How is demand extrapolated? How is actual freight demand identified?

Take us through the process of running a shipment, just all of the steps that occur.

And then run us through what happens on the backside.

And why is it hard? 

Ask more about this:

Emptytimebecomes emptymiles- Detention, dockdelays, andmissed appointments destroy backhaul

feasibility upstream of the load-matching decision. Drivers were detained at 39.3% of all stops in 2023,

representing 135M hours and $11.5B in lost productivity. Solving empty miles requires solving dwell. (ATRI,

2024)



What kind of system wide optimization do you see potential for? How do you imagine this being done? Local optimization creates system-wide waste - Every party optimizes its own operation. Meaningful empty- mile reduction requires someone governing the full network, not just individual nodes.

Speak more to this: 

Governance, not collaboration, is the unlock - When sales and operations both claim the customer, no one

owns the trade-offs. Decision authority and aligned scorecards are what close the gap, not better

communication. (Final Mile Insights Feb 2026)



Eg what is done here ? is there a broader publication? 



Conflicting scorecards undermine the initiative - Teams optimizing their own metrics will consistently

produce outcomes that work against network-level empty-mile reduction. This is structural, not behavioral.

(Catalyst Insights Feb 2026)





Pattern – imperial vs local



Ok so ask.. What are the incentives at the high level and the low level and what could we resolve with software? 

For a cross-action orchestration platform, which parties would need to share data with each other? What is their likely attitude and level of maturity to this? What is the feasibility of getting adoption for a system lke this? 



Matt's thesis: 

Capturing that opportunity fully requires treating it as a governance and incentive problem, not just a routing and visibility problem, and making the profit-service-risk trade-offs explicit at every decision point in the network.

Can you unpack this whole thing? 





Intelligence to Incorporate:





Trailer pooling at ports. Pooling is a legitimate and effective tool, and it works well where dwell is unpredictable and service windows are loose, such as ocean ports. The caution is in assuming it translates directly into tighter service environments, where the cost and service trade-offs land very differently. Why is it so effective at ports and less so at other locations? Port service is well known as an unfriendly, delay and detention-ridden environment. Pooling layers a managed structure on top of an already-degraded service environment — it works precisely because the bar is already low.



Modeling time:

Emptytimebecomes emptymiles- Detention, dockdelays, andmissed appointments destroy backhaul

feasibility upstream of the load-matching decision. Drivers were detained at 39.3% of all stops in 2023,

representing 135M hours and $11.5B in lost productivity. Solving empty miles requires solving dwell. (ATRI,

2024)



**At what point does time lag become a fail point for picking up another load? Is this just the difficulty of making a match line-up within a narrow enough window of time that it's not a better idea to send that out to a dedicated new virgin load?



I think it's like this – an empty load is harder to fill than a virgin load, because it requires the driver coming off the last route to exactly hit a time window, which means that the whole prior route has to go according to plan. (Or that there is frequently enough popping up laods that he can gra a next one). 

Please indicate if you are a: *

 For-Hire Carrier, Private Carrier, Driver, Trucking Industry Supplier, University, Media, Insurance, Consultant, Association, Other

Everything starts with modeling demand — 

Market downturns expose the coordination gap - In weak freight cycles, deadhead rises because there is no

cross-party orchestration layer. The 16.7% figure reflects what happens without one. This includes

seasonality, economic changes, and other influences.



This expands the problem and the opportunity simultaneously, with more potential

matches but also more nodes, constraints, and need for governed data sharing.



Each trucker has a set of constraints mapped to them



Who needs to share data? 









Cross-Actor Orchestration







The Goal:



Goal 1: Reduce all lag —

Insights: figure out why a lag is happening and what process would need to happen to precede it and how to implement this up the chain 

Goal 1: Reduce empty miles — eg pick up a cargo in every docked location (or near it) 





What the app has to do:



Start with modeling freight demand 

To then send some kind of signal out to folks (what exactly?)

And allocate loads - how does this get done "fairly"? How do you enable efficiency without becoming a decider of who gets to work and who doesn't? Algorithm has components for thinking about evenness of spreading work 

Or maybe it's just…pop in when you're working and see if you get a ping to pick up a backhaul (like uber pings drivers) 





Empty mile

Connect a load to a backhaul trucker. 

Load has locationofpickup, set to [place, position], named [current position].Load has locationofloaddestination, which it needs to arrive to within [timewindow].Trucker is approaching locationofpickup.Trucker is returning to locationofloaddestination within [loadtimewindow].

TruckDestination1: pickup load1

TruckDestination2: dropoffload1

[match – what loads are available in the use case?; what trucker is best suited to pick up each load?]

Truck Destination 3: pickupload2

Truck Destination 4: dropoffload2





Look out ahead at what needs to be hit in terms of deadlines and then scan up the route to look for where there might be blockers.

Also, when something happens, like al ag, look back up through the rest of the fchain to see how to reallocate load if possible.

Check conditions on the route to also flag where things might become stalled.

The use case is: all of the trucks in motion continually.

And hten there's all of the operations at the port, etc. the other stations





The Vocabulary:





Time? 

(then also other metrics perhaps like price?)





Stations:

Materials: 

Loads:

Trucks:

Road:

Ports 

Warehouse 

What else?



Chassis, shipping containers, the things that are part of a process of ingredients

Situated at a station, awaiting pickup

Mobile vector, run by

driver & company

Specific road and condition of the road, traffic on the road, weather affecting the road



The things that happen (run of show at each location)





Journey of a load - lateral: The path that a load will take, from location to location to location to final mile





The map of the terrain - vertical: 

At ports 

On the road between a virgin load and a first destination

On the road between a second destination (a backhaul trip) and a third destination

At destination 

Warehouse

Final mile delivery 

Etc





The Portion Governed By Each Actor: 

Stage X: 

What does the port do?

What does a trucker do? 

What does a trucking company do? (is this an "operator"?)

Manage the triangle of profit, service, and risk. 

What does the dispatcher or AI system do? Etc. 





The Process:



Variant 1: Overseas to National – #portion this into stages 

An overseas shipper [by country; specifics could vary] ships goods [in a container] to [port location].

The journey that the good takes to leave the factory and to arrive to a shipping container and carrier.

The journey that the maritime carrier takes - and the risks on the way. (e..g, whale strike for instance)

The arrival at the port, and unloading and storage. 

Anatomy of arriving component: ship with containers with goods inside "X container"

When a ship arrives at a port, the ship needs to come [to dock]. The port has [a number] of docking slots. Depending on the [number of other ships there are already there], the ship may or may not be able to dock [for awhile; time]. This can create [lag; wait time]. (One of the hard questions: How can this lag be reduced?)

Once a ship docks, it is then unloaded. Unloading it requires pthis process, with these inputs, and these staff]. E.g., chassis. If there is not enough of the required components, [a lag will occur], [which will start at timeN and go on until <a new chassis has been procured.].  [Run: chassis procurement process at TimeN - this is the steps to procure a chassis, if no chassis here, then get a chassi there, etc, etc, and will run now and check for where all teh things are, in order to figure out what type of chassis-procurement-run is both possible and fastest, now].

When a ship is unloaded, the vessel must sit in dock, and then [this orchestration activity must unfold]. At the end of this process, the result is that [the number of containers] the ship was carrying are now off of the ship and <in location> (on the dock). These containers could perhaps have an identification tag. Also, these containers could be moved via [some other process, using chassis] to a storage location.

Once a container is in a storage location, it awaits pickup by the trucker.



Intra-National

The pickup of the container by a trucker. 

A trucker comes to pick up the container via some process. 

There can be a wait, which produces [lag].

There can be missed appointments, for [reasons], which produces [lag]. 

The delivery of the cargo. (to where? How does the final destination shape this?) 

Planning

The trucker begins a (virgin or backhaul) trip, wherein they travel a route to bring the cargo to it destination (final or next).

The cargo is loaded.

The next destination is: whatever it is.

The trucker travels on <route> hich has <current; impending status>.

The trucker has ETA of date-time.



Actual Route 

The trucker is in location at time X, and, 

The traffic conditions in locations <along the way> are currently, and the weather is <doing this>, and the <traffic is doing this>, so we can see in advance of things that may impact the road, such as <snow, ice, etc.>



Arrival

The trucker arrives at location at date-time, with load.

The trucker goes to station to unload cargo.





Return Trip - Planning

[At some point in time], the trucker is matched to a backhaul load. There must be a) a trucker who will be returning from this region to a location where they can drop something else off, and also a load at the same time.



Return Trip - Delivery 

Delivering the cargo off at the location, ideally by the time anticipated. 











—

What governance is needed? 