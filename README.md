
# Title: Hands up! This is a Charity!

## Abstract
In 2015, an anonymous whistleblower leaked over 11.5 millions of financial documents from the Panamanian law firm Mossack Fonseca, the biggest data leak in History. Known as the [Panama Papers](https://www.theguardian.com/news/2016/apr/03/what-you-need-to-know-about-the-panama-papers), these documents revealed the  financial client informations of more than 200,000 offshores entities and exposed dozens of public officials, politicians, corporations, and charities. We would like to investigate the story of these charities.

Most charities are non-profit voluntaries association with a purpose to serve the common good. Their main source of income comes from donations, thus their success is directly linked to their reputation. How can we tell if a charity is worthy of our money?

Additionally, it has come out that many [shell companies](https://www.reuters.com/article/us-panama-tax-charities/aid-agencies-fear-damage-to-reputation-as-red-cross-appears-in-panama-papers-idUSKCN0X828W) created by Mossack Fonseca were named after charities with which they had no connection. This of course can put the reputations of perfectly transparent charities at risk.

Therefore, we will determine the degree of involvement of charities whose names turn up in the publicly accessible Panama Papers database.
    
## Research questions
* What charities show up in the panama papers ?
* Can we establish a scale of the probability that a found company actually represents a given charity against the probability that its name was stolen ?
* Can we classify the charities that actually have offshore accounts as legitimate uses or illegal ones ? 
* How does this impact charity donations, e.g. what charities can be seen as less trustworthy as a result of this research?

## Dataset
* __Wikipedia Dataset__:
	* __Goal__: Collect information about a set of charities, including their official names and known addresses
	* __Database__: Either the given data on the cluster, or extract it ourselves from wikipedia’s page listing charitable foundations (https://en.wikipedia.org/wiki/List_of_charitable_foundations)

* __Panama Papers Dataset__:
	* __Goal__: 
		* Find companies listed under the official names of charities, or variations on their names, and classify them into “real” or “name stolen” categories based on an analysis of the information given about them (addresses, country, etc...)
		* Find out if certain Panamanian firms are connected to more “charities” (real or names stolen) 
	
	* __Database__: The data provided by the ICIJ (International Consortium of Investigative Journalists), representing a small subset of the Panama Papers, which has been cleaned of information such as bank accounts, email exchanges and financial transactions. (https://www.occrp.org/en/panamapapers/database)
	* __Example__:
		* __The Charity__:
			* __Name__: International Federation of Red Cross and Red Crescent Societies
			* __Headquarters__: Geneva, Switzerland
		* __The Mossack Fonseca Client__:
			* __Name__: THE INTERNATIONAL RED CROSS OF GENEVA (sic)
			* __Panamanian Trust__: TARBES TRUST (FIDEICOMISO) (Also representing “WORLD WILDLIFE FUND” and “UNICEF”)


## A list of internal milestones up until project milestone 2
* Gather information about top charities from wikipedia
* Create a Database for official charity names (and variations) found in the Panama Papers.
* Establish potential connections between them.


## Questions for TAa
* Is it okay for us to use wikipedia independently, or do we have to use the provided database on the cluster?
* Can we also use the Paradise Papers and other Offshore leaks provided by the ICIJ, or are we limited to the Panama Papers?

