
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

##Project Structure
```
* _data
	* [...]
* _doc
	*  [...]
* _generated
	* _charities
		* Forbes_top_100_US_Charities.csv
			> Scraped charity info from Forbes article
		* wikipedia_charity_info.csv
			> Scraped charity info from wikipedia pages
		* wikipeida_charity_links.csv
			> Scraped charity wikipedia links
	* _INGO
		* wikipedia_INGO_info.csv
			> Scraped INGO info from wikipeda pages
		* wikipedia_INGO_links.csv
			> Scraped INGO wikipeida links
* _results
	* [...]
* _src
	* _charities
		* Forbes_list_scraping.ipynb
			> Notebook with:
				> functions to scrape the given forbes article
				> analysis of the found data
		* Wikipedia_charities_scraping.ipynb
			> Notebook with:
				> functions to scrape the given wikipedia page
				> analysis of the found data
	* _INGO
		* Wikipedia_INGO_scraping.ipynb
			> Notebook with:
				> functions to scrape the given wikipedia page
				> analysis of the found data
	* name_extraction.ipynb
	* 
* _temp
	* [...]
	
```
## Dataset

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

##Further sources: websites
* __Wikipedia__:
	* __Links__:
		* List of charitable foundations: 
		https://en.wikipedia.org/wiki/List_of_charitable_foundations
		* List of International Non-governmental organizations: 
		https://en.wikipedia.org/wiki/International_non-governmental_organization
	* __Method of Collection__: Web Scraping (Beautiful Soup)
		
	* __Information extracted__: Charity/NGO name, names of leaders, revenue, headquarters, location, other names, subsidiaries and purpose of all listed charities/NGOs, given availability of the information on the linked wikipedia pages of each charity/NGO.
	* __Reason chosen__: Abundant, easily available data whose semi-structured navboxes are relatively simple to scrape
	* __Problems encountered__: Available data varies from charity to charity, resulting in a sometimes sparse dataset. 
	
* __Forbes Website__:
	* __Links__: 
		*Article about the 100 largest charities in the USA:
		https://www.forbes.com/sites/williampbarrett/2016/12/14/the-largest-u-s-charities-for-2016/#5ca92a8d4abb
	* __Method of Collection__: Web Scraping (Beautiful Soup)
	* __Information Extracted__: Charity name, revenue, purpose, name of leader, end of last fiscal year (as of 2016), headquarters, and country of 100 of the largest charities in the USA, according to Forbes.
	* __Reason chosen__: Clean, complete, well structured and therefore easily scrapable data.
	* __Problems encountered__: Restricted to big US charities
	

## A list of internal milestones accomplished for milestone 2
* Gathering information about top charities from wikipedia (and now Forbes) and storing it as csv files
* Analysis of the Panama Papers (and Paradise and Bahamas papers too), for a better understanding of their structure. Tentative manual testing has shown that we will easily be able to cross check names.
* Set up of a number of methods to find name variants in the Panama papers, such as splitting the names of charities into separate words, removing the stop words like "the" or "for" and computing the percentage of correspondence between them and the Mossack Fonsecca entities.

## A list of internal milestones to accomplish for milestone 3
* Systematically cross-check charity names and variants of them in the Panama, Paradise and Bahamas Papers "entity" files using the cluster (while there were fewer than 1000 charities collected, the sheer size of the leaks, especially the Paradise Papers, makes running any cross-check of the name variants locally would take too much time.)
* Analyse the hits of the cross-check to determine whether they are random or genuine (this will have to be done manually, as it would take too much time to teach a train a classifer to determine whether a variant of a name is similar enough not to be random. But based on our manual tests on the ICIJ website, which gives us a search engine for the papers, we are anticipating that there will not be too many hits.)

	* Step 1:  Check the number of significant words in a charity name that match a Panama Papers entity's name
	
		*International Federation Red Cross Red Crescent Societies => THE INTERNATIONAL RED CROSS OF GENEVA*
	
	(Note that stopwords were removed from the charity name)
			
		Matches: International + Red + Cross
		Hits: 3 hits and 3/7 words correspondence
		Percentage: 3/7 for the charity, 3/6 for the entity
		
	The threshold can be varied to increase or decrease the number of hits depending on output.
	
	* Step 2: Check that this is not a random hit
	
	* Step 3: Is this a real charity's account or a fake entity using its name? 
	
	__Proposed scoring system__:
	1) If we have headquarter addresses for both, and they are the same city 
	=> very probably real
	
	2) Else if the entity connects to other hits at distance x, with x to be established: 
	For example with x=2, the following would qualify:
	```
	WWF <=> Tarbes Trust <=> Red Cross 
	```
	=> very probably fake 
	
	3) Else, if googling "charity name AND scandal" returns many results
	=> possibly real
	
	4) Else
	=> undetermined
		
* Possible alley to explore: searching for the names of CEOs of charities in the Panama Papers. However, this should be done with caution as human names can often belong to multiple unrelated people and we have no further information about these people. (For example, the top person at Salvation Army's name is David Jeffrey. This is also the name of [multiple people on linkedin](https://www.linkedin.com/pub/dir/david/jeffrey), as well as a [British football manager](https://en.wikipedia.org/wiki/David_Jeffrey).
* Create the data story, complete with profiles of charities that are very probably real account holders (using the extra data scored from the websites) and recommendations of which charities you should probably not give your money to.




