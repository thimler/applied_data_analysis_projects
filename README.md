
# Title: Hands up! This is a Charity!

## Abstract
In 2015, an anonymous whistleblower leaked over 11.5 million financial documents from the Panamanian law firm Mossack Fonseca, the biggest data leak in History. Known as the [Panama Papers](https://www.theguardian.com/news/2016/apr/03/what-you-need-to-know-about-the-panama-papers), these documents revealed the  financial client informations of more than 200,000 offshores entities and exposed dozens of public officials, politicians, corporations, and charities. We would like to investigate the story of these charities.

Most charities are non-profit voluntaries associations with a purpose to serve the common good. Their main source of income comes from donations, thus their success is directly linked to their reputation. How can we tell if a charity is worthy of our money?

Additionally, it has come out that many [shell companies](https://www.reuters.com/article/us-panama-tax-charities/aid-agencies-fear-damage-to-reputation-as-red-cross-appears-in-panama-papers-idUSKCN0X828W) created by Mossack Fonseca were named after charities with which they had no connection. This of course can put the reputations of perfectly transparent charities at risk.

Therefore, we will search for and examine the way charities appear in the publicly accessible Panama Papers database. We will also extend our seatch into data leaks
prior and later to the Panama Papers (the Paradise Papers, the Bahamas Leaks, and the Offshore leaks).
    
## Research questions
* What charities show up in the Panama Papers (and other leaks)?
* Do charities use their actual real addresses when registering in a tax haven?
* Is there a structure to the way charities set up in tax havens? Do they generally turn to the same companies? Are there companies in tax havens specialized in charities?

## Project Structure
```
* _data
	* [...]
		>Original csv files from the leaks
* _generated
	* _scraping
		*_forbes
			* Forbes_top_100_US_Charities.csv
				> Scraped charity info from Forbes article
		* _INGO
			* wikipedia_INGO_info.csv
				> Scraped INGO info from wikipeda pages
			* wikipedia_INGO_links.csv
				> Scraped INGO wikipeida links
		
		* _wikipedia
			* Forbes_top_100_US_Charities.csv
				> Scraped charity info from Forbes article
			* wikipedia_charity_info.csv
				> Scraped charity info from wikipedia pages
			* wikipeida_charity_links.csv
				> Scraped charity wikipedia links
	*_ matches
		*_entity
			> match files connecting charities to shells marked as entities in the leaks 
		*_officer
			> match files connecting charities to shells marked as officers in the leaks 
	*_ inspected_matches
		*_entity
			>manually inspected entity match files 
		*_officer
			>manually inspected officer match files
	* _map
		* _connections
			> matches joined by leak source
		*_degree_1
			> matches and their 1-degree connections in the leaks

* _results
	* _graphs
		> saved graphs of matches and their 1-degree connections with various levels of filtering
* _src
	* panama_overview.ipynb
		> Notebook with:
			> description of Panama Papers dataset
			> analysis and stat about Panama Papers
	* _ web_scraping
		* Forbes_list_scraping.ipynb
			> Notebook with:
				> functions to scrape the given forbes article
				> analysis of the found data
		* Wikipedia_charities_scraping.ipynb
			> Notebook with:
				> functions to scrape the given wikipedia page
				> analysis of the found data
		* Wikipedia_INGO_scraping.ipynb
				> Notebook with:
					> functions to scrape the given wikipedia page
					> analysis of the found data
	* name_ extraction_spark.ipynb
		> Notebook with:
			> functions to search for matches between leaked shell company names and charity names
	* Analysis.ipynb
		> Notebook generating and analysing
			> Address pairs belonging to shell-charity matches
			> Graphs displaying the structure of matched shells in the leaks
	* Connections.ipynb
		> Notebook creating files containing information about 
			> joining matches by leak
			> connecting matched shells to nodes one degree away in the leaks
	* Graphing_network.ipynb
		> Notebook creating json files for the data story's interactive graphs
	* _network
		> files for creation of the data story interactive networks
	* http_server.py
		> data story set-up file
	
```
## Dataset

* __Panama Papers Dataset__:
	* __Goal__: 
		* Find companies listed under the official names of charities, or variations on their names, and classify them into “real” or “name stolen” categories based on an analysis of the information given about them (addresses, country, etc...)
		* Find out if certain trusts and firms are connected to more “charities” (real or names stolen) 
	
	* __Database__: The data provided by the ICIJ (International Consortium of Investigative Journalists), representing a small subset of the Panama Papers, which has been cleaned of information such as bank accounts, email exchanges, or financial transactions. (https://www.occrp.org/en/panamapapers/database)
	* __Example__:
		* __The Charity__:
			* __Name__: International Federation of Red Cross and Red Crescent Societies
			* __Headquarters__: Geneva, Switzerland
		* __The Mossack Fonseca Client__:
			* __Name__: THE INTERNATIONAL RED CROSS OF GENEVA (sic)
			* __Panamanian Trust__: TARBES TRUST (FIDEICOMISO) (Also representing “WORLD WILDLIFE FUND” and “UNICEF”)
			
			
* __Other Leaks Datasets__:

	* __Composition__: 
	
	Paradise Papers, Bahamas Leaks, and Offshore Leaks.
	
	* __Database__: 
	They are also provided by the ICIj and are structured in a smilar way as the Panama Papers Dataset (for the exception of the Bahamas Leaks that is slightly different).
	They represent a small subset of the original Leaks, which have also been cleaned of information such as banck accounts, email exchanges, or financial transactions. (https://www.occrp.org/en/panamapapers/database)

	* __Structure__: 
The datasets are organized as graph databases using nodes representing the different actors linked by edges.
		* __The officers__: 
	People or corporations that are directors, shareholders, or beneficiaries of offshore companies.
		* __The entities__: 
	The offshore companies.
		* __The intermediaries__: 
	People and organizations, such as banks, that created offshore companies or trusts.
		* __The addresses__:
	 Any address connected to any officers, entities, or intermediaries.
	
## Further sources: websites
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
* Analysis of the Panama Papers, for a better understanding of their structure. A small-scale local test has shown that we will easily be able to cross check names. (This will be completed for milestone 3.)
* Set up of a number of methods to find name variants in the Panama papers, such as splitting the names of charities into separate words, removing the stop words like "the" or "for" and computing the percentage of correspondence between them and the Mossack Fonsecca entities.

## A list of internal milestones accomplished for milestone 3
* Systematically cross-checking charity names and variants of them in the leaked papers "entity" and "officer" files, using the following algorithm (shown here simplified). Using trial-and-error and checking the results for known matches (Amnesty International, the Red Cross, Acumen and WWF), this was found to have a good recall (all the known matches present in the returned values) and a fair precision (the number of wrong matches was small enough to be removed by hand, as explained in the next step).

```python
def check_for_words(charity, shell, stop_words):
    
	 threshold = 0.6
	    
	 for word in charity:
 		if word in shell:
		    count_random_matches += 1
		    
		if word in stop_words:
			stop_word_random_matches += 1
                
	#if only stopwords match, not valid
	if count_random_matches - stop_word_random_matches < 1:
	    return False

	#"Family foundations are tricky -> make sure those two words are not the only matching parts"
	if ('family' in shell and 'foundation' in shell 
	    and 'family' in charity and 'foundation' in charity 
	    and count_random_matches < 3 
	    and len(shell) > 2 and len(charity) > 2):
	    return False

	#If there's only one word, it has to be a match
    	if len(charity) == 1 or len(shell) == 1:
        	return (np.abs(len(charity) - len(shell)) < 2  and count_random_matches == 1)
        
	#Matches must be above a certain threshold
	return ((count_random_matches/len(charity) >= threshold) and (count_random_matches/len(shell) >= threshold))

```


* Inspecting and correcting the hits of the cross-check to determine whether they are random or genuine (this is done manually, as the filtered dataset only contains a few hundred matches, so it is faster and more accurate to resort to the expertise humans possess in natural language processing than to any training tool.

	
* Finding matched shells connected by a single entity by extracting all nodes at distance 1 of the found shell companies and creating graphs to view the clusters, to better understand how charities (or fake shells using charity names) relate to each other.

	
* Comparing addresses between actors involved with the shell companies and the charities. By extracting registered addresses from first level connections, we could compare these with the corresponding charity headquarter address (if known). If the addresses match, there is an excellent chance that these two groups are one and the same.
		

* Creating the data story

.. speaking of which

## Link to Data Story

 https://charity-leaks.github.io/

## Work Distribution

 * __Ruijia:__
 	* Web-scraping INGO
 	* Designing name-matching algorithm
 	* Manually filtering reduced match dataset
 	* Computing address-matching
 	* Designing data story
 * __Sabrina:__
 	* Web-scraping Forbes and Wikipedia
 	* Designing name-matching algorithm
 	* Manually filtering reduced match dataset
 	* Computing graphs
 	* Writing Readme 
 * __Theo:__
 	* Analysing the leak datasets
 	* Computing address-matching
 	* Scoring matches
 	* Writing Readme
 	* Writing data story




