## An Open Knowledge Network Pilot for Trust Infrastructure In the Freight Industry

A concept note following from the NIST "Building the Supply Chain Open Knowledge Network" workshop



The Problem With Freight

Freight is the foundation of the domestic supply chain, resting on a dynamic range of cross-actor orchestration between many stakeholders. Daily operations are undertaken primarily by shippers, carriers and 3PLs, facilitated by freight brokers. Carrier drivers thereafter undertake delivery journeys, moving across a wide range of public and private facilities, from ports, rail stations, and roads through to warehouses, delivery locations, and service stations. Supportive roles are played by service providers such as software companies and pay vendors, as well as insurance companies. Federally, the Department of Transportation (DOT) and Federal Motor Carrier Safety Administration (FMCSA) provide regulatory oversight. In addition, at times of large-scale industry disruption, other state and federal agencies may provide ancillary support.



The logistics professionals who perform these day-to-day operations are in turn supported by a range of technologies. Trucking management software (TMS) forms the primary technological layer of the logistics industry; these systems typically support individual job functions in executing a range of narrowly defined activities. As a result, there are numerous software solutions targeting different user personas and different processes. This in turn results in a siloed landscape of software solutions, all delivered by private companies driven by market forces to retain their existing products and market share. Unfortunately, this incentive structure  stymies innovation, leaving problems that are not already solved, or tightly focused around the needs of a specific logistics role, unaddressed. The gap between what the industry can and what it needs to do is only expanding, as a new class of broad-scale problems have emerged in the industry, with major consequences on the overall resilience of both the supply chain and the companies who operate it.  



As one example, the U.S. freight industry loses an estimated $7-16 billion annually to two distinct but structurally-related wide-scale industry challenges: 1) carrier identity fraud, and 2) detention. Both stem from the same, technological root cause: no neutral, cross-party data layer exists to establish a shared record of truth for all industry participants. Thus, shippers are unable to validate carrier legitimacy or track delivery journeys, leaving them exposed to cargo fraud and double brokering. Similarly, lack of visibility into detention results in costly billing disputes, as reporting about the actual path of a delivery journey is often discrepant across payor and payee systems. Meanwhile, possible corrective efforts are stymied, as facilities, shippers, carriers and operational procedures that produce delays are not well-identified. These issues are two of several similar, wide-scale issues which result in substantial financial losses, as shown in the figure below. 











Figure 1: Cost of Outstanding, Broad-based Problems WIthin the Freight Industry 



Despite these costs, industry is structurally unable to produce a solution. As mentioned, market incentives entrench existing technological solutions, and no private company possesses the resources or the motive to produce a broadly available, public asset capable of moving the overall state-of-the-art of industry practice forward. So, the entire industry continues to pay the price.



The limitations of existing technologies also obstruct public coordinated responses to broad disruption events, such as the COVID-19 pandemic, the closure of the Port of Baltimore, or the war in Iran. Although government agencies bear responsibility to respond to these scenarios, staff are often unable to gain visibility into current dynamics in the operational environment, or to access sufficient information for coordinating with other federal, state, and industry partners. As a result, essential response to wide-scale disruption remains constrained, engendering both great cost as well as great risk for the public at large.



Current trajectories of geopolitical, environmental, and cybersecurity risk indicate that large-scale disruption events are likely to continue occurring. Therefore, it is necessary to produce a technological infrastructure that can enable rapid and effective whole-of-industry response in such scenarios.



Given the constraints of commercial investment incentives, and the national strategic interest of supply chain security, this technological infrastructure is most suitably initiated by the federal government. However, for successful adoption, this technology must also address immediate industry needs. This concept note details a vision of such an approach, based on discussions that originated during the "Building the Supply Chain Open Knowledge Network" workshop held at NIST on March 9 and 10. 



## An Open Knowledge Network for Freight Trust

In 2022, the National Science Foundation and Office of Science and Technology Policy produced a vision for a common national infrastructure that could deliver data for complex, real-world use cases. This report, entitled "Open Knowledge Network Roadmap: Powering the Next Data Revolution," positions knowledge graphs and knowledge networks as the technological solution for facilitating cross-actor, mulitparty coordination in domains such as supply chain resilience. 



The report defines an open knowledge network (OKN) as "a technology network composed of multiple knowledge graphs, which are able to interact around a core infrastructure of shared interoperability frameworks, schemas, and data. As such, an OKN offers a pathway for orchestrating multi-party information share across systems."



OKNs are composed using knowledge graph technology, which functions as a mechanism for linking data to conceptual descriptions, through metadata, as shown in the example below.



picture



Knowledge graphs and knowledge networks are indeed the industry standard for addressing this kind of complex, multi-party, multi-database use case. Due to their inherent structure, knowledge graphs and networks are uniquely capable of providing technological scaffolding to integrate distributed datasets, linking data wherever it may sit to produce information that can provide the sophisticated, dynamic insights required by various network actors. 



An OKN goes up one level of scale, to construct an infrastructure that can provide the structural basis for a number of discrete knowledge graphs to be interconnected into an overarching network. 



Picture



As an architecture comprising multiple knowledge graph systems, the open knowledge network concept parallels the structure of the web. In fact, knowledge graph technology was initially conceptualized by the creator of the web, Sir Tim Berners-Lee, who recognized that, as the web grew, data would become irretrievable without any kind of attached description. This description, called metadata, is what the knowledge graph suite of languages (RDF, OWL) enable engineers to construct in a machine-readable format. While a knowledge graph introduces connectivity between data and concepts, a knowledge network adds an additional infrastructure layer to support connectivity between data from different private databases, each administered by a different owner.



In a public, cross-industry use case such as freight, an open knowledge network is particularly suitable. What this enables is streamlined cross-network information exchange – effectively, producing a customized "dedicated web" for the industry space, accessible by all industry participants to transact with necessary data.



If adopted to support the daily operating activities of the freight industry, this infrastructure would also provide a surface for visibility into real-time activities, as needed to orchestrate public-private responses to emergent disruption events. 



Freight Trust 

In the logistics industry, what an open knowledge network could deliver is freight trust. Freight trust describes an impartial, third-party, and authoritative record of consensus ground truth that all parties are able to reference as a shared ledger of verified activity. Freight trust is not a marketplace, not a single vendor's proprietary database, and not a new software category–it is public infrastructure that enables the industry as a whole to perform more effectively. 

The envisioned outcome is a shared, neutral, privacy-respecting infrastructure layer that links identity, events, and accountability across all freight parties, including carriers, brokers, shippers, facilities, insurers, and regulators. 



These participants would deliver time-stamped records of performed activities. They would be able to access and combine this information in particular ways, in order to address existing use cases as well as those that may evolve in the future. Real-time data from participants would be combined with existing datasets to produce new instruments that can address core questions in the space. 



In the section below, specific knowledge graph applications are envisioned, addressing the two problems identified at the NIST workshop: fraud, addressed through a carrier credentialing graph, and detention, addressed through a facility-performance graph.



## Use Cases and Solution Concepts

Following initial identification during the supply chain workshop, these use cases were further developed in consultation with industry practitioners. Early industry contacts have validated these needs and indicated positive reception to the notion of a federally-led OKN solution. 



Use Case 1: Cargo Shrinkage via Fraudulent Drivers

750M - 1 billion dollar loss in industry per year



Problem Statement:

When hiring new drivers, carriers face an increasing risk of contracting with fraudulent drivers, who are able to simulate the appearance of authentic professional drivers by registering for an MC number with the Department of Transportation. However, instead of delivering freight as anticipated, fraudulent drivers seize cargo instead, to later resell on digital markets. A very public example of this fraud occurred recently, when 12 tons of KitKat candies were stolen by a fraudulent driver. While this example affected a European market, the problem is endemic in the United States as well, with one trade newspaper reporting fraud experiences reported by virtually all of their readers. 



Without a provenance record for evaluating drivers, carriers lack the capacity to identify whether prospective new drivers are presenting truthful information. Although a commercial scoring system exists, administered federally by FMCSA, this score is insufficient for identifying potential fraudulent drivers. For example, FMCSA is not able to provide information about state registration, which is one indicator of fraudulent driver registrations. 



In addition, behavioral parameters, such as OTIF – "on-time in-full"--would be helpful for evaluating the quality of all drivers, within general day-to-day industry operations. At present, accessing driver information is a cumbersome process, as relevant information are widely disaggregated, and often not documented in a standardized manner, or at all. 



Carrier fraud causes a number of follow-on issues for every stakeholder in the industry. Shippers lose inventory, resulting in increased insurance claims as well as opportunity costs at retail points-of-sale. Freight brokers, who select carriers on behalf of shippers, are liable for cargo loss from fraudulent carriers. Legitimate carriers face two risks – of identity theft via impersonation of their MC number, with related reputational damage, and of increasing insurance premiums, which insurance providers levy broadly without access to specific carrier risk data. The operational work of reconciling all of these invoices falls to trucking management software companies and audit and pay vendors, with substantial manual effort and associated cost. 



FMCSA faces substantial operational overhead and pressure to address increasing incidence of fraud, with major new initiatives announced in late March 2026, spurred by DOT Secretary Sean Duffy. As one element of these initiatives, FMCSA is seeking better data reporting from truckers in the field, as the agency is struggling to verify whether complaints of fraud are themselves fraudulent. 



Similarly, without technology enabling system-wide reporting, the Department of Justice, FBI, DHS and other involved law enforcement agencies are constrained in their efforts to identify and curtail organized criminal activities.



Solution Concept: Carrier Credentialing Graph

Knowledge graphs are ideal for surfacing fraud because, while fraudulent transactions appear acceptable in isolation, they exhibit suspicious interlinkages when viewed in a broader context. 



Thus, a carrier credentialing graph would be able to collect rich data about real-time delivery journeys, serving as an authoritative provenance record of driver, carrier, facility, and shipper performance.



In the early stages of the delivery journey, the system can help users recognize fraudulent actors by provisioning clearer information about carrier and driver provenance. Currently, the FMCSA database is the primary reference tool for evaluating carriers. However, this is a static registry, which does not cross-reference behavioral history, related entities, or real-time status. 



By contrast, the carrier credentialing graph is equipped to resolve entities across multiple data sources: USDOT number, EIN, owner identity, registered address, commercial score, performance history (OTIF-"on-time in-full", length of activity, number of loads), insurance certificates, broker relationships, and claims history into a single, queryable profile. Additional data from broader data sources,, such as state registration databases, or driving schools, can also be integrated.. 

 

Pattern analysis algorithms, which are commonly used to detect money laundering and other forms of financial fraud, can be developed to automatically scan the broad system for signals of threat. Suspicious activities, such as an MC number sharing a registered address with fourteen other carriers, all of whom have been flagged for fraud in the past six months, can generate automatic alerts, which can be lodged against the entity node, as well as communicated directly to law enforcement. 



All of these data can be assessed to deliver a Freight Trust Index. The Freight Trust Index would include data about carrier and driver performance, yielding calculated trust and risk scores, a facility dwell/reliability score (addressing detention), and a load confidence score based on provenance across the shipment lifecycle. These scores would integrate existing FMCSA authority, identity, and carrier data, subsequently enhanced with cross-party provenance, behavioral pattern detection, and network-based risk scoring – capabilities enabled by the data supplied by industry participants into the knowledge graph, which go beyond the available tools available today. 



The carrier credentialing graph can also serve as a surface to orchestrate information flows between shippers, carriers, freight brokers, insurance companies, and law enforcement, in order to enable communications and information exchange that serve to ultimately reduce the number of transactions with fraudulent carriers and the related costs realized by various industry participants. 





Anticipated Industry Benefits

This system rests on the data provided by legitimate carriers, who have an incentive to participate in this system, to distinguish themselves from fraudulent and lower performance carriers. This verified identity graph will serve as a credentialing service, capable of both reputation security in the event of fraudulent impersonation, as well as signalling trustworthiness to shipping clients. 



Shippers will be able to use the verified identity graph to secure reliable delivery partners, and to reduce their exposure to realized loss as well as increased insurance premiums. Freight brokers can use the verified identity graph to evaluate prospective carriers, and can also self-report their performance to indicate to shippers their own reliability in due diligence. Aggregate indicators of fraud patterns, such as high volumes of reported fraud in particular geographic locations, can also be collected and delivered to alert brokers of conditions that require additional vigilance. 



Throughout the industry, support staff such as TMS/audit and pay vendors will be freed from the often manual task of data reconciliation, to apply resources to providing higher value products and activities. This will in turn realize greater efficiencies and innovation throughout the industry over time.



Insurance companies will receive greater access to information through this database of record, and will also realize reduced claims loss over time. 



As the principal respondent to fraud, FMCSA's efforts to curtail fraud will be greatly augmented, and in fact the Freight OKN could integrate directly with the new Motus system, designed to function as a "'one-stop shop' for carriers 'to do any and every transaction with FMCSA related to registration, biannual updates' and more, all the way to managing inspection data and filing DataQs requests to address fraud."

 

The FBI, DOJ and law enforcement can apply machine learning techniques to the identity graph to surface patterns that indicate fraud, as is currently practiced in banking. 



The following figure lays out the participation matrix for this use case, demonstrating how the carrier credentialing graph addresses existing challenges for each stakeholder, and their anticipated attitude towards participation. Figure 2. Stakeholder Matrix: Carrier Fraud





Section 2. Use Case 2: Detention 

$15 billion dollar economic loss per year



Problem Statement:

Delivery contracts are structured around delivery windows, during which cargo is expected to be delivered, unloaded or picked up. "Detention" describes occasions when these windows are not met, and cargo is forced to reside in place for longer than the two-hour grace period.



Late pick-up or delivery is penalized via costs specified within a particular contract. This represents a substantial fee cost throughout the industry, as well as downstream economic

effects, with the total yearly economic cost of detention estimated at $15 billion by the American Transportation Research Institute.



Driver detention is a widespread, recurring issue that undermines efficiency across the entire freight network, as downstream disruptions affect additional drivers, trucks, parking space, and other materials. An additional delay multiplier occurs when drivers waiting for cargo reach their limit of maximum allowable daily working hours, which then necessitates that they stop for an overnight break.



Lags such as these accumulate and cascade throughout the chain. Ultimately, late deliveries cause a variety of costs that can also transfer to other actors in the supply chain. Shippers lose retail income, and drivers face further detention in future delivery windows, bottlenecks at public facilities like ports, and disorganization in private operations facilities.





Solution Concept: A Facility Performance Knowledge Graph

What would help industry address this problem is a neutral, provenance-backed evidentiary layer that all parties trust, to collect and display performance data across facilities.This facility performance knowledge graph would record:



Performance at Facility Nodes: Every distribution center, plant, and terminal will be represented in the system, publishing driver and facility reports to produce a dwell-time record including average wait times by day, time of day, appointment slot performance, OTIF ("on time, in full") rates, and so forth.



Event Graph: To determine delivery timelines and thus detention timelines, events across the delivery journey will be recorded: load tendered, appointment scheduled, truck arrived, dock assigned, loading began, departure. All events will be timestamped and cross-referenced between participants. This system will thus clarify dispute resolution: when a carrier claims 3.5 hours and a shipper claims 1.5 hours, the timestamped graph record is the arbiter, not either party's internal system.



Behavioral Scoring: Facilities are scored in the same way as carriers are in the carrier identity graph. Dwell performance becomes an established fact. Through the corpus of collected data, analytics may provide insights into why detention rates are occurring where they are, and directions for studying how to address these through additional data, operational, or software products, at both the facility and network level.







Anticipated Industry Benefits

All carriers stand to benefit from timestamped delivery information, which can support collection rate for detention fees. Small carriers, specifically, will be able to access equal evidentiary standing, regardless of fleet size, in negotiations with shippers. 



A scorecard for shippers' facilities can be introduced, enabling visibility into operational inefficiencies for shippers to improve processes, as well as predictive information for carriers about which shippers are currently likely to produce detention. This would enable 3PLs and logistics managers to maneuver the graph to identify real-time load allocation across the network, thereby increasing efficiency and performance.



With a neutral record, freight brokers can be removed from billing disputes, reducing liability claims. 



Automated dispute resolution can free trucking management software companies and audit and Pay Vendors to apply resources to value-added features.



Carriers' and shippers' detention history, and real-time information about facilities such as ports, can be used by all relevant operators to improve performance, as well as provide sufficient visibility to FMCSA and DOT to enforce regulations. 



Other federal agencies will also have visibility to intervene as necessary into unfolding systemic disruptions, in the form of aggregated real-time field reports, relevant insights, and stakeholder contact information.



The following figure succinctly lays out the participation matrix, demonstrating how the facility-performance graph addresses existing challenges for each stakeholder, and their anticipated attitude towards participation. 























Figure 3. Stakeholder Matrix: Detention







## Shared Infrastructure Approach

Both of these systems share a single underlying architecture - the open knowledge network. The OKN includes the standardized structures for organizing data exchange across the network, in addition to the specific technology needed for each knowledge graph solution. The architecture design for these systems must also be sociotechnical, including parameters for governance, privacy, cybersecurity, and other concerns related to the operational integrity of the platform. 



The Freight OKN will require a clear framework across three dimensions:



Technical Architecture: a hybrid open-system architecture with connected closed nodes (for individual company knowledge graphs), a dynamic system reflecting real-world information updates, the ability to link diverse information and deduce linkages among related information elements, and a simultaneous focus on the use-case driven "vertical" graphs as well as the network-driven "horizontal" aspects of technological development

Data & Semantics: shared ontologies and standards to create consistent, interoperable context

Governance & Incentives: stewardship models, trust boundaries, and aligned incentives across stakeholders 



These structured decision-making frameworks will enable multiple stakeholders to operate cohesively and safely across the network. 



Technical Architecture

The technical architecture is envisioned to include data ingestion tooling capable of integrating data from diverse sources into the OKN; a technical architecture that includes a semantic triple store, potential integrations with property graphs (based on integration requirements), and, dependent on the scale of data, possibly a hybrid architecture utilizing both triplestores for the knowledge graph and Hadoop or some other very high volume data store with efficient search algorithms such as Map/Reduce. API integrations and dedicated manual and automatic data entry portals, for each party to contribute to the graph, will also be developed, as well as a range of GUIs, permissioned access, governance tooling, and cybersecurity protections..



Standardized Ontologies 

A standardized ontology schema, for interoperable data representation and exchange between all of the knowledge graphs participating within the network, as well as specific "local" ontologies for the carrier credentialing and facility performance graphs will be developed. 



A central ontology will map out all of the phases comprising the goods movement process. This ontology will be developed in sight of existing industry standards. It is important to note that standardization is essential here, so that the resulting ontology is able to serve as a lingua franca for all industry participants to build on, reference, or translate to, when constructing the schemas within local graphs. 



This ontology will be designed to be capable of expanding in a number of directions, as needed for various use cases both currently anticipated and that evolve the future. To represent the lifecycle of a delivery journey, concepts to model would include at minimum: 

The cargo - shipper, cargo, and required destination and time of arrival 

The contract - the broker and and carrier(s) engaged in transport, and relevant documentation 

The delivery journey - the driver, route, expected destination and times of arrival, actual stops made, as well as broader geographical influences such as weather and traffic 

The delivery environment - facilities, anticipated time windows, actual conditions and performance



Local ontologies for the carrier credential graph and the facility performance graph will be extended from this core standard. 



Governance Structure  

Critical aspects of the system include the guiding principles to enable logistics stakeholders to design, direct and oversee policies, design, development, operations, and management of the system. These will include addressing several topics: how data is sourced and from whom; how data is stored; what data is made public to the network versus what data is stored and owned locally within individual users' graphs; processes for developing the ontological standards and suggesting additions and improvements over time; how access to raw data versus aggregated scores is distributed across the network; and what privacy and cybersecurity measures will be taken to ensure data remains secure. This governance structure must also be explicitly designed to establish guardrails against anti-competitive behavior between companies within the network.



## Anticipated Impact

The Freight Trust OKN has the opportunity to modernize the data environment that freight operators, vendors, and public agencies rely on. A parallel that exposes how helpful this kind of regulation can be to enhance the operations of an industry can be witnessed in the airline industry. In 1987, DOT mandated public disclosure of on-time statistics from airline companies. Carrier behavior improved almost immediately. Detention at facilities is equivalent to this challenge; through an OKN, facility performance can potentially be improved directly through data standardization–without requiring new legislation.. 



In contrast to legislation, the Freight OKN is also able to simultaneously deliver a highly-useful, cost-saving innovation that industry is unable to develop within the framework of private market incentives. For these reasons, this is also a rare case where industry would welcome federal leadership to yield standardized materials, protocols and infrastructure that are impossible to develop commercially. 



Industry stands to realize a number of other immediate and long-term benefits, as well.



Cost, risk, and overhead reductions 

For industry, benefits are immediate and tangible. The Freight OKN would directly address pain points in fraud and detention, saving billions of dollars, reducing risk, and streamlining operations throughout the operations environment. These technologies would also support follow-on benefits in related activities. For instance, billing reconciliation, which often requires time-consuming, manual correspondence and engages approximately $50B in value each year, could be streamlined by aggregating and applying the right rate framework to each leg of an unfolding delivery journey. Potentially, greater efficiencies could reduce prices for consumers downstream–a welcome relief from current price pressures.  



AI-ready technology infrastructure

The Freight OKN also represents a ready infrastructure for additional AI integrations, in keeping with the 2025 White House AI Action Plan. The primary foundation of AI readiness is data preparation; the infrastructure developed through the OKN would therefore support myriad future projects, reducing future costs and barriers to entry.



Similarly to the development of Google Maps– initially informed by geographical data mapping from Census–the Freight OKN could serve as a broad surface layer for industry developers, spawning, potentially, a whole new layer of possible applications. Rationalizing the data surface would benefit software providers, by freeing significant engineering resources which are currently spent on low-value data wrangling tasks, like parsing paper invoices via OCR, normalizing carrier EDI formats, matching rate confirmations to invoices, flagging duplicates, and so forth. This work is currently necessary because the underlying data layer is fragmented and non-standardized. A knowledge network reduces that burden and frees vendors to compete on higher-value capabilities: analytics, exception prevention, contract intelligence, and optimization.



Moreover, through rigorous design and development, the Freight OKN can also serve as an infrastructure that wards off future potential risks, intrinsic to the AI transition. For instance, haphazard introduction of new technologies on top of legacy platforms could result in an even more byzantine work environment, or in spot failures brought forward by Generative AI-based errors, or cybersecurity vulnerabilities. The Freight OKN offers an opportunity to level the playing field, so that all participants in the freight industry can access a safe and reliable data fabric. 



Currently, there is also an opportunity to connect with the NSF-funded Proto-OKN, a broader national AI infrastructure effort. The NSF, which coined the term "open knowledge network" in the aforementioned seminal report, and which defines OKNs as an essential element of a national AI infrastructure, has awarded $80 million in contracts to approximately thirty use cases, which together form the nucleus of a Proto-OKN network. The Freight OKN has the opportunity to become the first OKN that originates not from academia but from a real world context, which can both integrate with the broader Proto-OKN to support the realization of national AI readiness, as well as inform future efforts to expand the Proto-OKN and successfully engage additional industry participation.  



Enhanced resilience to disruption

By providing all logistics industry stakeholders — federal agencies, shippers, carriers, 3PLs, freight brokers, insurance companies, and vendors— access to integrated information for a variety of uses, operators will have more visibility into both their own and network operations, and increased flexibility to respond to evolving circumstances. In addition, federal agencies will have greater visibility into the health and real-time status of the supply chain, supporting efforts to ensure efficient and stable operations across the domestic supply chain, and to orchestrate efforts to plan for, prevent and manage disruptions when necessary.  





Pilot Design Concept 

The Freight OKN concept has been shared with a number of supply chain professionals by the authors of this report; it has been well-received. In a partnership bridging knowledge network expertise with industry insight and access, Common Action, LLC and Catalyst propose to jointly undertake a pilot solution, composed of the following activities.   



The project would kick off with a review of existing resources in order to identify and assess usability of existing digital standards, and the current state of relevant industry data modernization initiatives. This would include assessment of materials from industry associations and work groups, such as:



The ASTM International Technical Committee F49 on Digital Information in the Supply Chain. A major area of work for this group is defining terms and data needed for the Goods Movement Process (GMP).  Major elements of this are definitions of events and statuses in the GMP, and codes for the same. This type of material will be critical to establish within standardized ontologies. Additionally, efforts will be made to connect with experts involved in this and similar groups, who may be able to provide advice into contemporary problems and how data could address them.

A number of open source APIs for the logistics industry exist. OpenAPI exists to support scheduling, while additional APIs exist for electronic Bill of Lading (eBOL), pickup request and visibility, and preliminary freight charges, and beyond. Reviewing these materials will shed light both on data types, elements and codes that may be relevant for ontological development. The different approaches demonstrated in style and format will also be useful to identify the delta and nature of differing representation schemes which are currently used within the industry. 



To solicit important contextual information, design insights, and critical feedback, we would next engage stakeholders across the delivery journey through interviews and focus groups. A range of instruments and activities would be designed, based on initial exploratory conversations, to elicit a complete perspective of the challenges that exist in this space, as well as the considerations necessary to deploy a real world technology solution. 



Initial exploration has begun, with interviews currently arranged with a number of candidates, to solicit feedback on the idea presented within this concept note. These candidates include: 

A veteran of the carrier and shipper space and current fortune 500 manufacturing executive, who can describe a day in the life of both a carrier and shipper, load boards, contract freight, detention, and billing

A supply chain executive well-known among startup carriers, who can speak to the challenges faced by small carriers

A fortune 500 safety leader, who can demonstrate how companies currently use the FMCSA dashboards as a reference for the freight trust concept

A software developer/expert in the TMS space, who can explain what current TMS systems do and don't do



These exploratory efforts would be later expanded to include interviews with representatives for every persona type (e.g, shippers, carriers, brokers, drivers, insurance companies, FMCSA, DOT, law enforcement). We intend also to arrange a number of focus groups and design workshops with representatives from relevant industry associations, including: 



Associations: American trucking associations (ATA), National Private Truck Council (NPTC), Owner-Operator Independent Drivers Association (OOIDA), National Association of Small Trucking Companies (NASTC), Truck Load Carriers Association (TCA), National Association of Independent Truckers (NAIT), Commercial Vehicle Safety Alliance (CVSA)   

Shippers: Food Shippers of America (FSA), International Foodservice Distribution Association, the National Association of Wholesalers

Retailers: National Retail Federation and National Grocers Association (NGA)



After completion of these preliminary investigations, the bulk of the technical design work would commence. Design artifacts will include technical scoping for the OKN architecture; the definition of a standard for interoperable data representation across the knowledge network; domain ontologies for each identified use case; data collection strategies and ingestion pipelines and tools; the development of the Freight Trust Index and other analytical tools; and development of stakeholder-specific GUIs. Design artifacts would be produced in the first stage, which would then be demonstrated back to industry collaborators for feedback and refinement, before development of the full system. Development would be undertaken in an Agile structure, and include iterative feedback with client representatives. This work would be followed by testing and other finalization necessary for production-ready deployment. 



Finally, the working prototype would be socialized with industry contacts, to solicit final feedback, and explore avenues for further roll-out, including integration with currently used technologies.





