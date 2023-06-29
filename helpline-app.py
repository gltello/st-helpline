import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define the questions and their weights
questions = [
    {
        'question': 'In which phase of the  do you feel your digital channel implementation is?',
        'topic': "IT Infrastructure",
        'weight': 0.077,
        'answers': {
            '0. Risk management plan': 0,
            '1. Infrastructure Upgrade': 1,
            '2. Infrastructure Audit': 2,
            '3. Staff Training': 3,
            '4. Contingency Planning': 4,
            '5. User Acceptance Testing (UAT)': 5
        },
        'recomendations': {
            'Africa': {
                0: "**Risk Management Plan:**<br>Develop a detailed risk management plan that takes into account specific risks in Africa, such as natural disasters (e.g., droughts, floods in Sub-Saharan Africa), political states (e.g., geopolitical tensions, regulatory changes), and data protection regulations (e.g., General Data Protection Regulation in the EU, data privacy laws in specific African countries). Customize the plan to address the cultural nuances and geopolitical landscape of each country or region within Africa.<br>Estimated Time: 1 week",

                1: "**Infrastructure Upgrade:**<br>Conduct an assessment of the existing IT infrastructure to determine if any upgrades or modifications are necessary to meet the unique demands of each country in Africa. Consider factors such as localized scalability, power supply stability (e.g., availability of backup power solutions), and network connectivity in remote or underserved areas.<br>Estimated Time: 2 weeks",

                2: "**Infrastructure Audit:**<br>Perform a comprehensive audit of the current IT infrastructure, taking into account specific regional considerations in Africa. Consider factors such as vulnerability to natural disasters (e.g., drought-resistant infrastructure in arid regions, infrastructure resilience in flood-prone areas), political stability (e.g., potential impact on infrastructure availability and reliability), and adherence to local data protection laws and regulations.<br>Estimated Time: 1 week",

                3: "**Staff Training:**<br>Provide cultural and language training to the team involved in managing the digital channel to ensure they have a deep understanding of the diverse cultures and customs within Africa. Consider factors such as language preferences (e.g., English, French, Arabic), cultural norms and sensitivities, and specific communication styles in different countries or regions.<br>Estimated Time: 2 weeks",

                4: "**Contingency Planning:**<br>Develop a contingency plan that specifically addresses the unique challenges and risks associated with each country or region in Africa. Consider factors such as vulnerability to specific natural disasters (e.g., desertification in the Sahel region, cyclones in coastal areas), political instability (e.g., civil unrest, political transitions), and localized cybersecurity threats (e.g., emerging cybercrime activities).<br>Estimated Time: 1 week",

                5: "**User Acceptance Testing (UAT):**<br>Conduct user acceptance testing with a diverse group of African users to gather feedback and ensure the digital channel meets their expectations and requirements. Consider factors such as language preferences, usability based on cultural norms, and local user behavior influenced by various cultures and ethnic groups across Africa.<br>Estimated Time: 2 weeks",
        },
            'Asia': {
            0: "**Risk Management Plan:**<br> Develop a detailed risk management plan that takes into account specific risks in Asia, such as natural disasters (e.g., earthquakes in Japan, typhoons in Southeast Asia), political states (e.g., geopolitical tensions, regulatory changes), and data protection regulations (e.g., General Data Protection Regulation in the EU, Personal Data Protection Act in Singapore). Customize the plan to address the cultural nuances and geopolitical landscape of each country or region within Asia.<br>Estimated Time: 1 week",
                
            1: "**Infrastructure Upgrade:**<br> Conduct an assessment of the existing IT infrastructure to determine if any upgrades or modifications are necessary to meet the unique demands of each country in Asia. Consider factors such as localized scalability, localization of data storage (e.g., data sovereignty requirements), and network connectivity in remote areas with limited infrastructure.<br>Estimated Time: 2 weeks",
                
            2: "**Infrastructure Audit:**<br> Perform a comprehensive audit of the current IT infrastructure, taking into account specific regional considerations in Asia. Consider factors such as vulnerability to natural disasters (e.g., earthquake-resistant infrastructure in earthquake-prone areas), political stability (e.g., potential impact on infrastructure availability and reliability), and adherence to local data protection laws and regulations.<br>Estimated Time: 1 week",
                
            3: "**Staff Training:**<br> Provide cultural and language training to the team involved in managing the digital channel to ensure they have a deep understanding of the diverse cultures and customs within Asia. Consider factors such as language preferences (e.g., Mandarin Chinese, Hindi, Japanese), cultural norms and sensitivities, and specific communication styles in different countries or regions.<br> Estimated Time: 2 weeks",

            4: "**Contingency Planning:**<br> Develop a contingency plan that specifically addresses the unique challenges and risks associated with each country or region in Asia. Consider factors such as vulnerability to specific natural disasters (e.g., flooding in Bangladesh, tsunamis in coastal areas), political instability (e.g., civil unrest, regime changes), and localized cybersecurity threats (e.g., targeted hacking groups).<br>Estimated Time: 1 week",
            
            5: "**User Acceptance Testing (UAT):**<br>Conduct user acceptance testing with a diverse group of Asian users to gather feedback and ensure the digital channel meets their expectations and requirements. Consider factors such as language preferences, usability based on cultural norms, and local user behavior influenced by various cultures within Asia (e.g., collectivism in East Asian countries, diversity in religious practices across the region).<br>Estimated Time: 2 weeks"
            },
            'Europe': {
                0: "**Risk Management Plan:**<br>Develop a detailed risk management plan that includes risk identification, assessment, response planning, and monitoring.<br>Estimated Time: 1 week",

                1: "**Infrastructure Upgrade:**<br> Based on the audit results, upgrade the IT infrastructure as necessary. This could involve increasing server capacity, updating software, etc.<br>Estimated Time: 2 weeks",

                2: "**Infrastructure Audit:**<br> Conduct a thorough audit of the existing IT infrastructure to ensure it can support the new digital channel launch. This step is crucial in mitigating the risk early on.<br>Estimated Time: 1 week",

                3: "**Staff Training:**<br> Provide technical training to the team involved in managing the digital channel. They should be able to operate, maintain, and troubleshoot the new channel.<br>Estimated Time: 2 weeks",

                4: "**Contingency Planning:**<br> Despite all efforts, there may still be unforeseen problems. Having a robust contingency plan can help manage these effectively.<br>Estimated Time: 1 week",

                5: "**User Acceptance Testing (UAT):**<br> Implement a structured User Acceptance Testing phase where a select group of end-users try out the new digital channel before it's fully launched. Their feedback can be used to make final adjustments, ensuring the channel meets user expectations and requirements.<br>Estimated Time: 2 weeks"
            },
            
            'North America': {
                0:"**Risk Management Plan:**<br>Develop a detailed risk management plan that includes risk identification, assessment, response planning, and monitoring. Consider factors specific to North America, such as potential natural disasters (e.g., hurricanes, wildfires), political stability, data protection regulations (e.g., General Data Protection Regulation in certain jurisdictions), and cultural diversity across different states and provinces.<br>Estimated Time: 1 week",

                1:"**Infrastructure Upgrade:**<br>Based on the audit results, upgrade the IT infrastructure as necessary. Consider factors such as resilience against natural disasters (e.g., backup power systems, data centers in secure locations), scalability to handle high volumes of traffic, compliance with data protection laws specific to North America (e.g., CCPA in California, PIPEDA in Canada), and multilingual support to accommodate the diverse languages spoken in the region.<br>Estimated Time: 2 weeks",

                2:"**Infrastructure Audit:**<br>Conduct a thorough audit of the existing IT infrastructure to ensure it can support the new digital channel launch. Consider factors such as varying internet connectivity speeds across different regions, infrastructure vulnerabilities to potential natural disasters, and compliance with data protection regulations applicable to each state or province.<br>Estimated Time: 1 week",

                3:"**Staff Training:**<br>Provide technical training to the team involved in managing the digital channel. Ensure the training covers cultural sensitivity, understanding the diverse languages (e.g., English, Spanish, French) and cultural nuances prevalent in North America, and knowledge of specific issues and challenges faced by children in the region.<br>Estimated Time: 2 weeks",

                4:"**Contingency Planning:**<br>Despite all efforts, there may still be unforeseen problems. Develop a robust contingency plan that accounts for potential natural disasters, technological failures, cybersecurity threats, and coordination with local authorities and organizations during emergencies. Consider the specific risks associated with the region, such as hurricanes in coastal areas or wildfires in certain states.<br>Estimated Time: 1 week",

                5:"**User Acceptance Testing (UAT):**<br>Implement a structured User Acceptance Testing phase where a select group of end-users try out the new digital channel before it's fully launched. Ensure the testing includes participants from diverse cultural backgrounds, language preferences, and regions within North America to validate the channel's usability and effectiveness.<br>Estimated Time: 2 weeks"
            },
            'South America': {
                0:"**Risk Management Plan:**<br>Develop a detailed risk management plan that includes risk identification, assessment, response planning, and monitoring. Consider factors specific to South America, such as vulnerability to natural disasters (e.g., earthquakes, floods), political instability in certain regions, and data protection regulations specific to each country.<br>Estimated Time: 1 week",

                1:"**Infrastructure Upgrade:**<br>Based on the audit results, upgrade the IT infrastructure as necessary. Consider the potential impact of natural disasters on infrastructure stability and the need for backup systems and contingency plans. Also, ensure compliance with data protection laws specific to each country in South America.<br>Estimated Time: 2 weeks",

                2:"**Infrastructure Audit:**<br>Conduct a thorough audit of the existing IT infrastructure to ensure it can support the new digital channel launch. Consider factors such as infrastructure disparities across regions, varying internet connectivity speeds, and compliance with data protection laws in each South American country.<br>Estimated Time: 1 week",

                3:"**Staff Training:**<br>Provide technical training to the team involved in managing the digital channel. In addition to technical skills, ensure the training addresses cultural sensitivity, understanding the diverse languages, and cultural practices prevalent in South America.<br>Estimated Time: 2 weeks",

                4:"**Contingency Planning:**<br>Despite all efforts, there may still be unforeseen problems. Develop a robust contingency plan that accounts for potential natural disasters, political changes, and coordination with local authorities and organizations. Consider specific risks related to the region, such as earthquakes, hurricanes, political unrest, and cyber threats.<br>Estimated Time: 1 week",

                5:"**User Acceptance Testing (UAT):**<br>Implement a structured User Acceptance Testing phase where a select group of end-users try out the new digital channel before it's fully launched. Ensure the testing includes participants from different language backgrounds, cultures, and regions within South America to validate the channel's usability and effectiveness.<br>Estimated Time: 2 weeks"
            },
            'Australia': {
                0:"**Risk Management Plan:**<br>Develop a detailed risk management plan that takes into account specific risks in Australia, such as natural disasters (e.g., bushfires, cyclones), political states (e.g., regulatory changes, government policies), and data protection regulations (e.g., Privacy Act, Australian Privacy Principles). Customize the plan to address the cultural nuances and geopolitical landscape of Australia.<br>Estimated Time: 1 week",

                1:"**Infrastructure Upgrade:**<br>Conduct an assessment of the existing IT infrastructure to determine if any upgrades or modifications are necessary to meet the unique demands of Australia. Consider factors such as localized scalability, resilience to natural disasters, and compliance with Australian data protection and privacy regulations.<br>Estimated Time: 2 weeks",

                2:"**Infrastructure Audit:**<br>Perform a comprehensive audit of the current IT infrastructure, taking into account specific regional considerations in Australia. Consider factors such as vulnerability to natural disasters (e.g., bushfire preparedness in fire-prone areas), political stability (e.g., potential impact on infrastructure availability and regulations), and adherence to local data protection laws and regulations.<br>Estimated Time: 1 week",

                3:"**Staff Training:**<br>Provide cultural and language training to the team involved in managing the digital channel to ensure they have a deep understanding of the Australian culture, including Indigenous cultures, and can effectively communicate with diverse populations. Consider factors such as language preferences (e.g., English, Indigenous languages), cultural sensitivities, and specific communication styles.<br>Estimated Time: 2 weeks",

                4:"**Contingency Planning:**<br>Develop a contingency plan that specifically addresses the unique challenges and risks associated with Australia. Consider factors such as vulnerability to specific natural disasters (e.g., floods in coastal areas, cyclones in northern regions), political and environmental changes (e.g., climate change impacts), and localized cybersecurity threats.<br>Estimated Time: 1 week",

                5:"**User Acceptance Testing (UAT):**<br>Conduct user acceptance testing with a diverse group of Australian users to gather feedback and ensure the digital channel meets their expectations and requirements. Consider factors such as language preferences, usability based on cultural norms, and local user behavior influenced by the diverse communities and Indigenous populations in Australia.<br>Estimated Time: 2 weeks"
            }
        }
    },
    {
        'question': 'How complete is your technology stack for digital channels?',
        'topic': "Partnerships with other institutions",
        'weight': 0.098,
        'answers': {
            '0. Technology review and enhancement': 0,
            '1. Strategic Partnership Development': 1,
            '2. Staff Technology Training': 2,
            '3. Regular Technology Updates and Maintenance': 3,
            '4. Innovative Technology Exploration': 4,
            '5. Risk Assessment for New Technology Implementation': 5
        },
        'recomendations': {
            'Africa': {
                0:"**Technology Review and Enhancement:**<br>Conduct a comprehensive technology review to evaluate the current state of the digital channel technologies in place, considering the specific factors relevant to Africa. Assess the political landscape, including stability and regulatory frameworks, in each country or region where your digital channels operate. Ensure compliance with data protection laws and regulations, such as the General Data Protection Regulation (GDPR) for countries in the European Union or the Protection of Personal Information Act (POPIA) in South Africa. Consider linguistic diversity and language preferences across Africa, adapting your digital channels to cater to local languages and cultural nuances.<br>Estimated Time: 2 weeks",

                1:"**Strategic Partnership Development:**<br>Foster partnerships with other institutions, tech companies, and local organizations in Africa. Collaborate on technology integration and knowledge sharing to enhance your digital channel offerings. Take into account the political environment and consider partnerships with organizations that have experience navigating the regulatory landscape and political dynamics in specific African countries. Ensure compliance with local laws and regulations related to partnerships and data sharing.<br>Estimated Time: 2 weeks",

                2:"**Staff Technology Training:**<br>Provide comprehensive training programs to staff members, focusing on digital technologies, data protection, and regional trends specific to African countries. Address language preferences and cultural sensitivities to ensure effective communication and engagement with diverse users. Take into consideration the linguistic diversity and adapt training materials to cater to the languages spoken in the respective countries or regions. Also, provide training on data protection laws and regulations specific to each country, such as the Nigerian Data Protection Regulation (NDPR) or the Kenya Data Protection Act.<br>Estimated Time: Ongoing",

                3:"**Regular Technology Updates and Maintenance:**<br>Implement a maintenance schedule to regularly update and service your technology stack, considering the specific laws and regulations related to data protection in African countries. Ensure compliance with regional and national data protection laws and establish protocols for handling data breaches and security incidents. Take into account the availability of reliable internet connectivity in different African regions and adapt your technology updates and maintenance plans accordingly. Also, consider the potential impact of power outages or infrastructure limitations on technology operations.<br>Estimated Time: 1 week per briefing, done quarterly",

                4:"**Innovative Technology Exploration:**<br>Research and explore cutting-edge technologies that are relevant to the African market, considering regional needs, infrastructural limitations, and cultural acceptance. Take into account the political dynamics and the varying levels of technology adoption across different African countries. Consider technologies that can address unique challenges in Africa, such as mobile-based solutions, offline capabilities, or low-bandwidth optimization. Additionally, explore solutions that promote inclusivity and accessibility, taking into consideration the linguistic and cultural diversity in Africa.<br>Estimated Time: Ongoing",

                5:"**Risk Assessment for New Technology Implementation:**<br>Prior to rolling out new technologies in Africa, conduct a thorough risk assessment that takes into account the political environment, data protection laws, and cultural acceptance of technology. Assess the potential impact of political instability, regulatory changes, or state control on technology operations and data privacy. Mitigate potential risks by ensuring compliance with data protection laws specific to each African country and by having contingency plans in place to address potential disruptions. Additionally, consider the potential impact of limited internet connectivity and tailor your technology implementation accordingly.<br>Estimated Time: As needed, typically 2-4 weeks per assessment"
        },
            'Asia': {
                0: "**Technology Review and Enhancement:**<br>Conduct a comprehensive technology review to evaluate the current state of the digital channel technologies in place, considering the specific factors relevant to Asia. Assess the vulnerability to natural disasters like earthquakes, typhoons, cyclones, and floods in regions like Japan, the Philippines, Bangladesh, and India. Consider the political states of the countries involved, including regulatory frameworks, cybersecurity policies, and government support for digital initiatives. Ensure compliance with data protection laws and regulations that vary across Asian countries, such as the Personal Data Protection Act (PDPA) in Singapore or the Cybersecurity Law in China. Address the diverse languages and cultures present in Asia and assess the localization needs for your digital channels.<br>Estimated Time: 2 weeks",

                1: "Strategic Partnership Development:**<br>Foster partnerships with other institutions and tech companies in Asia, considering the specific natural disaster risks prevalent in different regions. Collaborate on technology integration to enhance your digital channel offerings, taking into account the linguistic and cultural diversity across Asia. Explore partnerships with local organizations to ensure alignment with regional needs and preferences. Consider specific partnerships with companies experienced in dealing with natural disaster response systems, such as earthquake early warning systems in Japan or flood monitoring technologies in Southeast Asian countries.<br>Estimated Time: 2 weeks",

                2: "**Staff Technology Training:**<br>Provide comprehensive training programs to staff members, considering the technological trends and preferences specific to Asian countries. Address cultural nuances, language preferences, and specific technology adoption patterns within different Asian countries or regions. Consider providing language-specific training and cultural sensitivity training to ensure effective communication and engagement with diverse users. Also, consider providing disaster response training to staff members, including protocols for handling emergencies related to natural disasters, such as earthquake preparedness or flood response procedures.<br>Estimated Time: Ongoing",

                3: "**Regular Technology Updates and Maintenance:**<br>Implement a maintenance schedule to regularly update and service your technology stack, taking into account regional factors such as localized software patches and hardware maintenance. Ensure compliance with data protection regulations specific to each Asian country, such as the General Data Protection Regulation (GDPR) for data protection in the European Union or the Personal Information Protection Commission (PIPC) in Japan. Consider incorporating disaster recovery and backup solutions to safeguard against natural disasters or system failures. Additionally, develop contingency plans that account for potential disruptions caused by natural disasters, such as establishing backup data centers in safer locations or implementing redundant communication networks.<br>Estimated Time: 1 week per briefing, done quarterly",

                4: "**Innovative Technology Exploration:**<br>Research and explore cutting-edge technologies that are relevant to the Asian market, considering specific regional needs and preferences. Take into account the potential impact of natural disasters such as earthquakes, typhoons, cyclones, or floods on technology infrastructure. Explore technologies that can assist in disaster response and recovery, such as AI-powered early warning systems, satellite imagery for disaster assessment, or blockchain-based systems for transparent aid distribution. Consider cultural acceptance and language requirements while implementing AI, chatbots, or other advanced technologies to improve service delivery and user satisfaction. Also, explore solutions that address connectivity challenges in rural or remote areas, such as satellite internet or community mesh networks.<br>Estimated Time: Ongoing",

                5: "**Risk Assessment for New Technology Implementation:**<br> Prior to rolling out new technologies in the Asian market, conduct a thorough risk assessment that considers regional factors such as cybersecurity risks, compatibility with existing systems, and cultural acceptance of technology. Pay special attention to data protection and privacy regulations specific to each Asian country, such as the Personal Data Protection Act (PDPA) in Singapore or the Personal Information Protection Commission (PIPC) in Japan. Mitigate potential risks and ensure staff training addresses cultural sensitivity, disaster response protocols, and language requirements. Establish clear protocols for data breach incidents and have plans in place to respond to potential cyber threats, especially considering the geopolitical landscape and the presence of state-sponsored cyber activities in some Asian countries.<br>Estimated Time: As needed, typically 2-4 weeks per assessment"
            },
            'Europe': {
                0:"**Technology Review and Enhancement:**<br>Conduct a comprehensive technology review to evaluate the current state of the digital channel technologies in place. Identify gaps and areas for improvement.<br>Estimated Time: 2 weeks",

                1:"**Strategic Partnership Development:**<br>Foster partnerships with other institutions and tech companies. Collaborate on technology integration to enhance your digital channel offerings.<br>Estimated Time: 2 weeks",

                2:"**Staff Technology Training:**<br>Provide comprehensive training programs to staff members, focusing on digital technologies and trends. Ensure that the team is well-equipped to manage and optimize your technology stack.<br>Estimated Time: Ongoing",

                3:"**Regular Technology Updates and Maintenance:**<br>Implement a maintenance schedule to regularly update and service your technology stack. This ensures the technology remains current and supports your digital channels effectively.<br>Estimated Time: 1 week per briefing, done quarterly",

                4:"**Innovative Technology Exploration:**<br>Research and explore cutting-edge technologies like AI, chatbots, and advanced data analytics. Implement these tools into your digital channels to improve service delivery and user satisfaction.<br>Estimated Time: Ongoing",

                5:"**Risk Assessment for New Technology Implementation:**<br>Prior to rolling out new technologies, conduct a thorough risk assessment. Mitigate potential issues, ensuring compatibility with current systems, and preparing staff training.<br>Estimated Time: As needed, typically 2-4 weeks per assessment"
            },
            'North America': {
                0:"**Technology Review and Enhancement:**<br>Conduct a comprehensive technology review to evaluate the current state of the digital channel technologies in place, considering the diverse geographical and climatic regions of North America. Identify gaps and areas for improvement, taking into account potential risks posed by natural disasters such as hurricanes, earthquakes, or wildfires. Additionally, ensure compliance with data protection regulations such as the General Data Protection Regulation (GDPR) and local privacy laws.<br>Estimated Time: 2 weeks",

                1:"**Strategic Partnership Development:**<br>Foster partnerships with other institutions and tech companies in North America, considering the political states and regulations within each region. Collaborate on technology integration to enhance your digital channel offerings, aligning with local government initiatives and industry standards. Tailor partnerships to address specific language needs and cultural sensitivities of different communities within North America.<br>Estimated Time: 2 weeks",

                2:"**Staff Technology Training:**<br>Provide comprehensive training programs to staff members, focusing on digital technologies and trends relevant to North America's diverse linguistic and cultural landscape. Ensure that the team is well-equipped to manage and optimize your technology stack, with an emphasis on understanding cultural nuances, communication preferences, and language diversity within the region.<br>Estimated Time: Ongoing",

                3:"**Regular Technology Updates and Maintenance:**<br>Implement a maintenance schedule to regularly update and service your technology stack, considering the potential impact of natural disasters on infrastructure stability. Ensure that the technology remains current and supports your digital channels effectively, with quarterly briefings addressing any specific risks related to natural disasters and political developments in the region.<br>Estimated Time: 1 week per briefing, done quarterly",

                4:"**Innovative Technology Exploration:**<br>Research and explore cutting-edge technologies like AI, chatbots, and advanced data analytics, considering their potential application in addressing language barriers and cultural diversity within North America. Implement these tools into your digital channels to improve service delivery and user satisfaction, while ensuring compliance with data protection regulations and respecting cultural sensitivities.<br>Estimated Time: Ongoing",

                5:"**Risk Assessment for New Technology Implementation:**<br>Prior to rolling out new technologies, conduct a thorough risk assessment specific to North America, taking into account potential risks posed by natural disasters, data breaches, or political instability. Mitigate these issues by ensuring compatibility with current systems, conducting regular backups, and implementing security measures. Staff training should include preparedness for potential disruptions caused by natural disasters and emergency response protocols.<br>Estimated Time: As needed, typically 2-4 weeks per assessment"
            },
            'South America': {
                0:"**Technology Review and Enhancement:**<br>Conduct a comprehensive technology review to evaluate the current state of the digital channel technologies in place, considering the diverse geographical and climatic regions of South America. Identify gaps and areas for improvement, taking into account potential risks posed by natural disasters such as earthquakes, floods, volcanic eruptions, or tropical storms. Additionally, ensure compliance with data protection regulations specific to each country in South America.<br>Estimated Time: 2 weeks",

                1:"**Strategic Partnership Development:**<br>Foster partnerships with institutions and tech companies in South America, considering the political states and regulations within each country. Collaborate on technology integration to enhance your digital channel offerings, aligning with local government initiatives and industry standards. Tailor partnerships to address specific language needs and cultural sensitivities of different communities within South America.<br>Estimated Time: 2 weeks",

                2:"**Staff Technology Training:**<br>Provide comprehensive training programs to staff members, focusing on digital technologies and trends relevant to South America's diverse linguistic and cultural landscape. Ensure that the team is well-equipped to manage and optimize your technology stack, with an emphasis on understanding cultural nuances, communication preferences, and language diversity within the region.<br>Estimated Time: Ongoing",

                3:"**Regular Technology Updates and Maintenance:**<br>Implement a maintenance schedule to regularly update and service your technology stack, considering the potential impact of natural disasters on infrastructure stability. Ensure that the technology remains current and supports your digital channels effectively, with quarterly briefings addressing any specific risks related to natural disasters and political developments in the region.<br>Estimated Time: 1 week per briefing, done quarterly",

                4:"**Innovative Technology Exploration:**<br>Research and explore cutting-edge technologies like AI, chatbots, and advanced data analytics, considering their potential application in addressing language barriers and cultural diversity within South America. Implement these tools into your digital channels to improve service delivery and user satisfaction, while ensuring compliance with data protection regulations and respecting cultural sensitivities.<br>Estimated Time: Ongoing",

                5:"**Risk Assessment for New Technology Implementation:**<br>Prior to rolling out new technologies, conduct a thorough risk assessment specific to South America, taking into account potential risks posed by natural disasters, data breaches, or political instability. Mitigate these issues by ensuring compatibility with current systems, conducting regular backups, and implementing security measures. Staff training should include preparedness for potential disruptions caused by natural disasters and emergency response protocols.<br>Estimated Time: As needed, typically 2-4 weeks per assessment"
            },
            'Australia': {
                0:"**Technology Review and Enhancement:**<br>Conduct a comprehensive technology review to evaluate the current state of the digital channel technologies in place, considering the specific factors relevant to Australia. Assess the political landscape and regulatory frameworks, such as the Australian Privacy Principles (APPs) and the Privacy Act 1988, which govern data protection and privacy in Australia. Consider the linguistic diversity and cultural nuances in different regions of Australia, adapting your digital channels to cater to local languages and preferences.<br>Estimated Time: 2 weeks",

                1:"**Strategic Partnership Development:**<br>Foster partnerships with other institutions, tech companies, and local organizations in Australia. Collaborate on technology integration, knowledge sharing, and regulatory compliance. Take into account the political environment and consider partnerships with organizations that have expertise in navigating Australian regulations and policies related to digital channels and data protection.<br>Estimated Time: 2 weeks",

                2:"**Staff Technology Training:**<br>Provide comprehensive training programs to staff members, focusing on digital technologies, data protection, and compliance with Australian laws and regulations. Address language preferences and cultural sensitivities to ensure effective communication and engagement with diverse users in Australia. Also, provide training on data protection laws and regulations specific to Australia, such as the Notifiable Data Breaches scheme and the Australian Consumer Law.<br>Estimated Time: Ongoing",

                3:"**Regular Technology Updates and Maintenance:**<br>Implement a maintenance schedule to regularly update and service your technology stack, ensuring compliance with Australian data protection laws and regulations. Establish protocols for handling data breaches and security incidents, following the guidelines outlined by the Office of the Australian Information Commissioner (OAIC). Take into account the reliability of internet connectivity and the availability of infrastructure in different regions of Australia when planning technology updates and maintenance.<br>Estimated Time: 1 week per briefing, done quarterly",

                4:"**Innovative Technology Exploration:**<br>Research and explore cutting-edge technologies that are relevant to the Australian market, considering regional needs and regulatory requirements. Take into account the political dynamics and consumer expectations in Australia. Consider technologies that promote privacy, security, and accessibility, aligning with the Australian Digital Service Standard and the Web Content Accessibility Guidelines (WCAG) 2.1.<br>Estimated Time: Ongoing",

                5:"**Risk Assessment for New Technology Implementation:**<br>Prior to rolling out new technologies in Australia, conduct a thorough risk assessment that considers the political environment, data protection laws, and consumer privacy expectations. Mitigate potential risks by ensuring compliance with Australian data protection regulations, including conducting Privacy Impact Assessments (PIAs) where necessary. Stay informed about legislative changes and regulatory updates that may affect technology implementation in Australia.<br>Estimated Time: As needed, typically 2-4 weeks per assessment"
            }
        }
    },
    {
        'question': 'How do you feel your fundraise strategy is  enough and steady to cover your cost short and long term?',
        'topic': "Funding",
        'weight': 0.115,
        'answers': {
            '0. Fundraising strategy development': 0,
            '1. Financial Sustainability Planning': 1,
            '2. Grant Applications and Donor Outreach': 2,
            '3. Fundraising Events and Campaigns': 3,
            '4. Diversification of Funding Sources': 4,
            '5. Regular Review and Adjustment of Fundraising Strategy': 5
        },
        'recomendations': {
            'Africa': {
                0:"**Fundraising Strategy Development:**<br>Develop a comprehensive fundraising strategy tailored to the Africa region, taking into account the diverse cultural, linguistic, and political contexts across different countries. Identify potential funding sources, including grants, foundations, corporate partnerships, and international development organizations.<br>Estimated Time: 2 weeks",

                1:"**Financial Sustainability Planning:**<br>Develop a financial sustainability plan that reflects the economic and political realities of each country in Africa. Consider local laws, regulations, and reporting requirements related to fundraising activities. Adapt the strategy to the specific challenges and opportunities present in each country.<br>Estimated Time: 2 weeks",

                2:"**Grant Applications and Donor Outreach:**<br>Research and identify grant opportunities and key donors relevant to your organization's work in each African country. Customize grant applications and proposals to align with local priorities, development agendas, and funding criteria. Establish strong relationships with local donors, NGOs, and international development agencies operating in the region.<br>Estimated Time: Ongoing",

                3:"**Fundraising Events and Campaigns:**<br>Plan and organize fundraising events and campaigns that resonate with the diverse cultures, languages, and customs across Africa. Consider local traditions and sensitivities in event planning and messaging. Collaborate with local partners, community leaders, and influencers to maximize outreach and engagement.<br>Estimated Time: 3-4 weeks per event",

                4:"**Diversification of Funding Sources:**<br>Avoid overreliance on a single funding source by seeking to diversify your funding streams. Explore opportunities for partnerships with local businesses, foundations, and government entities. Leverage diaspora networks and international collaborations to expand your fundraising reach.<br>Estimated Time: Ongoing",

                5:"**Regular Review and Adjustment of Fundraising Strategy:**<br>Conduct regular reviews of the fundraising strategy for each African country to evaluate its effectiveness. Stay informed about changes in local laws, economic conditions, and political landscapes. Make necessary adjustments to the strategy based on performance, emerging opportunities, and evolving development priorities.<br>Estimated Time: Quarterly reviews, 1 week per review"

        },
            'Asia': {
                0:"**Fundraising Strategy Development:**<br>Develop a comprehensive fundraising strategy tailored to the Asia region, considering the cultural and political diversity across different countries. Research and identify potential funding sources, including grants, donations, corporate partnerships, and government funding programs specific to each country.<br>Estimated Time: 2 weeks",

                1:"**Financial Sustainability Planning:**<br>Develop a financial sustainability plan that considers the economic and political landscape of each country in Asia. Take into account local regulations and legal frameworks related to fundraising, ensuring compliance with relevant laws and reporting requirements.<br>Estimated Time: 2 weeks",

                2:"**Grant Applications and Donor Outreach:**<br>Identify potential grant opportunities and key donors relevant to your organization's work in each country. Customize grant applications and proposals to align with local priorities and funding criteria. Establish strong relationships with local donors and philanthropic organizations.<br>Estimated Time: Ongoing",

                3:"**Fundraising Events and Campaigns:**<br>Plan and execute fundraising events and campaigns that resonate with the diverse cultures and languages across Asia. Tailor your messaging and engagement strategies to appeal to local communities and ensure cultural sensitivity in all communications.<br>Estimated Time: 3-4 weeks per event",

                4:"**Diversification of Funding Sources:**<br>Avoid relying heavily on a single funding source. Seek to diversify your funding sources across different countries in Asia. Take into account local regulations and political dynamics when exploring partnerships with local businesses, foundations, and governmental bodies.<br>Estimated Time: Ongoing",

                5:"**Regular Review and Adjustment of Fundraising Strategy:**<br>Conduct regular reviews of the fundraising strategy for each country in Asia to assess its effectiveness. Monitor changes in local laws, economic conditions, and political landscapes to ensure ongoing compliance and adaptability. Make necessary adjustments to the strategy based on performance and emerging opportunities.<br>Estimated Time: Quarterly reviews, 1 week per review"
            },
            'Europe': {
                0:"**Fundraising Strategy Development:**<br>Develop a comprehensive fundraising strategy that outlines potential funding sources, including grants, donations, partnerships, etc. This strategy should be adaptable to long-term and short-term needs.<br>Estimated Time: 2 weeks",

                1:"**Financial Sustainability Planning:**<br>Develop a financial sustainability plan, incorporating projected income and expenses for short and long-term. This will aid in understanding the funding required and ensuring the fundraising strategy is sufficient.<br>Estimated Time: 2 weeks",

                2:"**Grant Applications and Donor Outreach:**<br>Identify potential grant opportunities and key donors relevant to your organization's work. Allocate resources to submit robust applications or proposals, and maintain strong relationships with these entities.<br>Estimated Time: Ongoing",

                3:"**Fundraising Events and Campaigns:**<br>Regularly organize fundraising events and campaigns to increase public awareness and raise funds. This can range from online campaigns, charity events, or public outreach initiatives.<br>Estimated Time: 3-4 weeks per event",

                4:"**Diversification of Funding Sources:**<br>Diversify your funding sources as much as possible. Relying heavily on a single source can increase risk if that funding source is suddenly unavailable. Seek multiple revenue streams to ensure steady funding.<br>Estimated Time: Ongoing",

                5:"**Regular Review and Adjustment of Fundraising Strategy:**<br>Conduct regular reviews of the fundraising strategy to measure its effectiveness and adjust accordingly. This ensures the strategy evolves with changes in the financial landscape and organizational needs.<br>Estimated Time: Quarterly reviews, 1 week per review"
            },
            'North America': {
                0:"**Fundraising Strategy Development:**<br>Develop a comprehensive fundraising strategy tailored to the North American context, considering the diverse fundraising practices and preferences within the region. Identify potential funding sources, including grants, donations, corporate sponsorships, and individual giving. This strategy should be adaptable to long-term and short-term needs, considering the cultural and social nuances of North America.<br>Estimated Time: 2 weeks",

                1:"**Financial Sustainability Planning:**<br>Develop a financial sustainability plan specific to the North American context, taking into account projected income and expenses, economic factors, and potential funding sources within the region. This will aid in understanding the funding required and ensuring the fundraising strategy is aligned with long-term stability in North America.<br>Estimated Time: 2 weeks",

                2:"**Grant Applications and Donor Outreach:**<br>Identify potential grant opportunities and key donors within North America, including foundations, corporations, and individual philanthropists. Tailor your outreach and messaging to align with North American philanthropic priorities and values. Build strong relationships with local entities and donors, understanding their preferences and funding criteria.<br>Estimated Time: Ongoing",

                3:"**Fundraising Events and Campaigns:**<br>Organize fundraising events and campaigns that resonate with the North American audience, considering cultural and social trends, local communities, and causes that are relevant within the region. Utilize digital platforms, social media, and networking events to engage supporters and generate funds.<br>Estimated Time: 3-4 weeks per event",

                4:"**Diversification of Funding Sources:**<br>Diversify your funding sources within the North American context, considering partnerships with corporations, sponsorships, major gifts, online crowdfunding, and peer-to-peer fundraising. Adapt your fundraising approach to the preferences and practices prevalent in North America while aligning with data protection and privacy regulations.<br>Estimated Time: Ongoing",

                5:"**Regular Review and Adjustment of Fundraising Strategy:**<br>Conduct regular reviews of the fundraising strategy specific to the North American context to measure its effectiveness and adjust accordingly. This includes analyzing fundraising data, evaluating donor engagement, and staying updated on emerging trends and best practices within the North American philanthropic landscape.<br>Estimated Time: Quarterly reviews, 1 week per review"
            },
            'South America': {
                0:"**Fundraising Strategy Development:**<br Develop a comprehensive fundraising strategy that outlines potential funding sources, including grants, donations, partnerships, and specific fundraising practices prevalent in South America. This strategy should be adaptable to long-term and short-term needs, considering cultural nuances and preferences in fundraising approaches.<br>Estimated Time: 2 weeks",

                1:"**Financial Sustainability Planning:**<br>Develop a financial sustainability plan specific to the South American context, taking into account projected income and expenses, local economic factors, and potential funding sources within the region. This will aid in understanding the funding required and ensuring the fundraising strategy is aligned with long-term stability.<br>Estimated Time: 2 weeks",

                2:"**Grant Applications and Donor Outreach:**<br>Identify potential grant opportunities and key donors relevant to your organization's work in South America. Allocate resources to submit robust applications or proposals, considering specific cultural and language considerations in donor outreach. Maintain strong relationships with local entities and donors, understanding their priorities and preferences for funding allocation.<br>Estimated Time: Ongoing",

                3:"**Fundraising Events and Campaigns:**<br>Regularly organize fundraising events and campaigns tailored to the South American audience, considering cultural festivities, local traditions, and public engagement preferences. These can include online campaigns, charity events, or public outreach initiatives that resonate with the local community.<br>Estimated Time: 3-4 weeks per event",

                4:"**Diversification of Funding Sources:**<br>Diversify your funding sources within the South American context, considering regional funding opportunities, corporate partnerships, and community-driven initiatives. Relying heavily on a single source can increase risk if that funding source is suddenly unavailable. Seek multiple revenue streams to ensure steady funding, aligning with local funding practices and regulations.<br>Estimated Time: Ongoing",

                5:"**Regular Review and Adjustment of Fundraising Strategy:**<br>Conduct regular reviews of the fundraising strategy specific to the South American context to measure its effectiveness and adjust accordingly. This ensures the strategy evolves with changes in the financial landscape, cultural preferences, and organizational needs within the region.<br>Estimated Time: Quarterly reviews, 1 week per review"
            },
            'Australia': {
                0:"**Fundraising Strategy Development:**<br>Develop a comprehensive fundraising strategy tailored to the Australian context, considering the diverse fundraising practices and preferences within the country. Identify potential funding sources, including grants, donations, corporate sponsorships, and individual giving. This strategy should be adaptable to long-term and short-term needs, considering the cultural and social nuances of Australia.<br>Estimated Time: 2 weeks",

                1:"**Financial Sustainability Planning:**<br>Develop a financial sustainability plan specific to the Australian context, taking into account projected income and expenses, economic factors, and potential funding sources within the country. This will aid in understanding the funding required and ensuring the fundraising strategy is aligned with long-term stability in Australia.<br>Estimated Time: 2 weeks",

                2:"**Grant Applications and Donor Outreach:**<br>Identify potential grant opportunities and key donors within Australia, including government agencies, foundations, corporations, and individual philanthropists. Tailor your outreach and messaging to align with Australian philanthropic priorities and values. Build strong relationships with local entities and donors, understanding their preferences and funding criteria.<br>Estimated Time: Ongoing",

                3:"**Fundraising Events and Campaigns:**<br>Organize fundraising events and campaigns that resonate with the Australian audience, considering cultural and social trends, local communities, and causes that are relevant within the country. Utilize digital platforms, social media, and community engagement initiatives to engage supporters and generate funds.<br>Estimated Time: 3-4 weeks per event",

                4:"**Diversification of Funding Sources:**<br>Diversify your funding sources within the Australian context, considering partnerships with corporations, sponsorships, major gifts, online crowdfunding, and community fundraising. Adapt your fundraising approach to the preferences and practices prevalent in Australia while aligning with data protection and privacy regulations.<br>Estimated Time: Ongoing",

                5:"**Regular Review and Adjustment of Fundraising Strategy:**<br>Conduct regular reviews of the fundraising strategy specific to the Australian context to measure its effectiveness and adjust accordingly. This includes analyzing fundraising data, evaluating donor engagement, and staying updated on emerging trends and best practices within the Australian philanthropic landscape.<br>Estimated Time: Quarterly reviews, 1 week per review"
            }
        }
    },
    {
        'question': 'To what extent your helpline maintain confidentiality and ensure the privacy of children seeking help?',
        'topic': "Security / data protection",
        'weight': 0.159,
        'answers': {
            '0. Security audit': 0,
            '1. Data Encryption': 1,
            '2. Staff Training': 2,
            '3. Privacy Policy Update': 3,
            '4. Third-party Risk Assessment': 4,
            '5. Contingency Planning': 5
        },
        'recomendations': {
            'Africa': {
                0:"**Security Audit:**<br> Conduct an in-depth security audit that aligns with the data protection and privacy laws specific to each African country. Ensure compliance with local regulations and identify any gaps or vulnerabilities in maintaining confidentiality and privacy standards.<br>Estimated Time: 3-4 weeks",

                1:"**Data Encryption:**<br>Implement strong encryption measures that comply with the data protection laws of each African country. Ensure data is securely encrypted both in transit and at rest, following local encryption standards and protocols.<br>Estimated Time: 2-4 weeks",

                2:"**Staff Training:**<br>Provide comprehensive training programs to helpline staff on confidentiality, data privacy laws, and cultural sensitivities specific to each African country. Consider the diverse linguistic and cultural backgrounds of staff members and users when delivering training.<br>Estimated Time: 2 weeks",

                3:"**Privacy Policy Update:**<br>Review and update the privacy policy to align with the data protection laws and cultural expectations of each African country where the helpline operates. Clearly communicate the privacy policy to users in local languages.<br>Estimated Time: 1-2 weeks",

                4:"**Third-party Risk Assessment:**<br>Assess the security measures and confidentiality practices of third parties, if applicable. Evaluate their compliance with local data protection laws and regulations. Ensure that any third-party relationships maintain the required confidentiality standards.<br>Estimated Time: Varies based on the number and complexity of third-party relationships",

                5:"**Contingency Planning:**<br>Develop a comprehensive contingency plan for potential breaches of confidentiality, considering the specific legal requirements and cultural norms of each African country. Include notification procedures, steps to mitigate breaches, and actions to prevent recurrence.<br>Estimated Time: 2-3 weeks"
        },
            'Asia': {
                0:"**Security Audit:**<br>Conduct an in-depth security audit that aligns with the data protection and privacy laws specific to each country in Asia. Ensure compliance with local regulations and identify any gaps or vulnerabilities in maintaining confidentiality and privacy standards.<br>Estimated Time: 3-4 weeks",

                1:"**Data Encryption:**<br>Implement strong encryption measures that comply with the data protection laws of each Asian country. Ensure data is securely encrypted both in transit and at rest, following local encryption standards and protocols.<br>Estimated Time: 2-4 weeks",
                
                2:"**Staff Training:**<br>Provide comprehensive training programs to helpline staff on confidentiality, data privacy laws, and cultural sensitivities specific to each Asian country. Ensure staff members are well-versed in handling sensitive data and maintaining privacy.<br>Estimated Time: 2 weeks",
                
                3:"**Privacy Policy Update:**<br>Review and update the privacy policy to align with the data protection laws and cultural expectations of each Asian country where the helpline operates. Clearly communicate the privacy policy to users in local languages.<br>Estimated Time: 1-2 weeks",
                
                4:"**Third-party Risk Assessment:**<br>Assess the security measures and confidentiality practices of third parties, if applicable. Evaluate their compliance with local data protection laws and regulations. Ensure that any third-party relationships maintain the required confidentiality standards.<br>Estimated Time: Varies based on the number and complexity of third-party relationships",
                
                5:"**Contingency Planning:**<br>Develop a comprehensive contingency plan for potential breaches of confidentiality, considering the specific legal requirements and cultural norms of each Asian country. Include notification procedures, steps to mitigate breaches, and actions to prevent recurrence.<br>Estimated Time: 2-3 weeks"
            },
            'Europe': {
                0:"**Security Audit:**<br>Conduct an in-depth security audit to ensure that your helpline is maintaining the required confidentiality and privacy standards. This will identify any gaps or vulnerabilities.<br>Estimated Time: 3-4 weeks",

                1:"**Data Encryption:**<br>Implement strong encryption for all data, both in transit and at rest. This includes strong password protocols, HTTPS for all web communications, and secure handling of user data.<br>Estimated Time: 2-4 weeks",

                2:"**Staff Training:**<br>Train all helpline staff on confidentiality and data privacy. This should include both general principles and specific protocols for your helpline.<br>Estimated Time: 2 weeks",

                3:"**Privacy Policy Update:**<br>Ensure that your privacy policy is robust, up-to-date, and clearly communicated to users. This should be reviewed annually, at a minimum.<br>Estimated Time: 1-2 weeks",

                4:"**Third-party Risk Assessment:**<br>If you work with third parties, assess their security measures and confidentiality practices. Your own confidentiality is only as strong as the weakest link in your chain.<br>Estimated Time: Varies based on the number and complexity of third-party relationships",

                5:"**Contingency Planning:**<br>Develop a contingency plan for potential breaches of confidentiality, including notification procedures, steps to mitigate the breach, and actions to prevent recurrence.<br>Estimated Time: 2-3 weeks"
            },
            'North America': {
                0:"**Security Audit:**<br>Conduct an in-depth security audit specific to North America to ensure that your helpline maintains the required confidentiality and privacy standards. Consider regional data protection regulations, industry best practices, and potential vulnerabilities specific to the region.<br>Estimated Time: 3-4 weeks",

                1:"**Data Encryption:**<br>Implement strong encryption measures in accordance with North American data protection regulations. This includes secure password protocols, HTTPS for web communications, and encryption of user data both in transit and at rest. Ensure compliance with relevant data protection laws such as the General Data Protection Regulation (GDPR) in the case of handling data from European Union residents.<br>Estimated Time: 2-4 weeks",

                2:"**Staff Training:**<br>Provide comprehensive training to helpline staff in North America on confidentiality, data privacy, and cultural considerations. Address specific data protection regulations and industry standards applicable in the region. Train staff members to handle sensitive information and understand the importance of maintaining privacy.<br>Estimated Time: 2 weeks",

                3:"**Privacy Policy Update:**<br>Review and update your privacy policy to align with North American data protection regulations, such as the California Consumer Privacy Act (CCPA) and the Personal Information Protection and Electronic Documents Act (PIPEDA) in Canada. Clearly communicate the privacy policy to helpline users in a language and format that is easily understandable to the target audience.<br>Estimated Time: 1-2 weeks",

                4:"**Third-party Risk Assessment:**<br>Assess the security measures and confidentiality practices of any third-party partners or service providers involved in the helpline operations in North America. Ensure that they comply with regional data protection regulations and maintain strict confidentiality standards. Consider additional requirements if handling personal information of European Union residents under GDPR.<br>Estimated Time: Varies based on the number and complexity of third-party relationships",

                5:"**Contingency Planning:**<br>Develop a contingency plan specific to North America to address potential breaches of confidentiality. This plan should include procedures for notifying affected individuals, mitigating the breach, and implementing preventive measures to avoid recurrence. Consider regional legal requirements for breach notifications, such as those outlined in the Data Breach Notification Laws in the United States.<br>Estimated Time: 2-3 weeks"
            },
            'South America': {
                0:"**Security Audit:**<br>Conduct an in-depth security audit specific to South America to ensure that your helpline maintains the required confidentiality and privacy standards. This audit should consider regional data protection regulations, cultural sensitivities, and potential vulnerabilities unique to the region.<br>Estimated Time: 3-4 weeks",

                1:"**Data Encryption:**<br>Implement strong encryption measures specific to South American data protection regulations. This includes secure password protocols, HTTPS for web communications, and encryption of user data both in transit and at rest. Consider any regional or country-specific encryption standards or requirements.<br>Estimated Time: 2-4 weeks",

                2:"**Staff Training:**<br>Provide comprehensive training to helpline staff in South America on confidentiality, data privacy, and cultural considerations. Ensure that staff members are aware of the specific privacy protocols and regulations relevant to the region.<br>Estimated Time: 2 weeks",

                3:"**Privacy Policy Update:**<br>Review and update your privacy policy to align with South American data protection regulations and cultural sensitivities. Clearly communicate the privacy policy to helpline users in a language and format that is easily understandable to the target audience.<br>Estimated Time: 1-2 weeks",

                4:"**Third-party Risk Assessment:**<br>Assess the security measures and confidentiality practices of any third-party partners or service providers involved in the helpline operations in South America. Ensure that they adhere to regional data protection regulations and maintain strict confidentiality standards.<br>Estimated Time: Varies based on the number and complexity of third-party relationships",

                5:"**Contingency Planning:**<br>Develop a contingency plan specific to South America to address potential breaches of confidentiality. This plan should include procedures for notifying affected individuals, mitigating the breach, and implementing preventive measures to avoid recurrence. Consider any regional legal requirements for breach notifications.<br>Estimated Time: 2-3 weeks"
            },
            'Australia': {
                0:"**Security Audit:**<br>Conduct an in-depth security audit specific to North America to ensure that your helpline maintains the required confidentiality and privacy standards. Consider regional data protection regulations, industry best practices, and potential vulnerabilities specific to the region.Estimated Time: 3-4 weeks",

                1:"**Data Encryption:**<br>Implement strong encryption measures in accordance with North American data protection regulations. This includes secure password protocols, HTTPS for web communications, and encryption of user data both in transit and at rest. Ensure compliance with relevant data protection laws, such as the General Data Protection Regulation (GDPR) for handling data from European Union residents.<br>Estimated Time: 2-4 weeks",

                2:"**Staff Training:**<br>Provide comprehensive training to helpline staff in North America on confidentiality, data privacy, and cultural considerations. Address specific data protection regulations and industry standards applicable in the region. Train staff members to handle sensitive information and understand the importance of maintaining privacy.<br>Estimated Time: 2 weeks",

                3:"**Privacy Policy Update:**<br>Review and update your privacy policy to align with North American data protection regulations, such as the California Consumer Privacy Act (CCPA) in the United States and the Personal Information Protection and Electronic Documents Act (PIPEDA) in Canada. Clearly communicate the privacy policy to helpline users in a language and format that is easily understandable to the target audience.<br>Estimated Time: 1-2 weeks",

                4:"**Third-party Risk Assessment:**<br>Assess the security measures and confidentiality practices of any third-party partners or service providers involved in the helpline operations in North America. Ensure that they comply with regional data protection regulations and maintain strict confidentiality standards. Consider additional requirements if handling personal information of European Union residents under GDPR.<br>Estimated Time: Varies based on the number and complexity of third-party relationships",

                5:"**Contingency Planning:**<br>Develop a contingency plan specific to North America to address potential breaches of confidentiality. This plan should include procedures for notifying affected individuals, mitigating the breach, and implementing preventive measures to avoid recurrence. Consider regional legal requirements for breach notifications, such as those outlined in the Data Breach Notification Laws in the United States and Canada.<br>Estimated Time: 2-3 weeks"
            }
        }
    },
    {
        'question': "How satisfied are you with the timeliness and responsiveness of helpline services in addressing children's needs?",
        'topic': "High response time",
        'weight': 0.093,
        'answers': {
            '0. Response time monitoring': 0,
            '1. Staff Training': 1,
            '2. Staff Augmentation': 2,
            '3. Technology Improvements': 3,
            '4- Process Improvement': 4,
            '5. User Feedback Collection': 5
        },
        'recomendations': {
            'Africa': {
                
                0:"**Response Time Monitoring:**<br>Implement response time monitoring systems that comply with data protection and privacy laws specific to each African country. Track how quickly helpline staff are responding to calls or messages while ensuring adherence to local regulations.<br>Estimated Time: 1-2 weeks",

                1:"**Staff Training:**<br>Conduct comprehensive training for helpline staff that considers cultural sensitivities, local languages, and communication styles prevalent in each African country. Enhance their ability to provide quick and culturally appropriate assistance to callers.<br>Estimated Time: 2-3 weeks",

                2:"**Staff Augmentation:**<br>Evaluate the demand patterns and consider increasing the number of staff or volunteers during peak call times to prevent bottlenecks and reduce response time. Take into account local labor laws and availability of resources.<br>Estimated Time: 1-2 months",

                3:"**Technology Improvements:**<br>Explore technological solutions that align with data protection laws and regulations of each African country. Look for software or tools that can automate or streamline parts of the helpline process, such as categorizing calls or messages for more efficient handling.<br>Estimated Time: 2-3 months",

                4:"**Process Improvement:**<br>Review the current helpline process to identify bottlenecks or inefficiencies specific to each African country. Consider cultural and linguistic factors that may affect response time and find ways to improve the process accordingly.<br>Estimated Time: Ongoing",

                5:"**User Feedback Collection:**<br>Regularly collect feedback from helpline users in each African country, taking into account cultural preferences and communication channels. Focus on responsiveness and incorporate user feedback to continuously improve the helpline service.<br>Estimated Time: Ongoing"
        },
            'Asia': {
                0:"**Response Time Monitoring:**<br>Implement response time monitoring systems that align with data protection and privacy laws specific to each Asian country. Track how quickly helpline staff are responding to calls or messages while ensuring compliance with local regulations.<br>Estimated Time: 1-2 weeks",

                1:"**Staff Training:**<br>Conduct intensive training for helpline staff that encompasses cultural sensitivities, local languages, and communication styles prevalent in each Asian country. Enhance their ability to provide quick and culturally appropriate assistance to callers.<br>Estimated Time: 2-3 weeks",

                2:"**Staff Augmentation:**<br>Evaluate the demand patterns and consider increasing the number of staff or volunteers during peak call times to prevent bottlenecks and reduce response time. Take into account local labor laws and availability of resources.<br>Estimated Time: 1-2 months",

                3:"**Technology Improvements:**<br>Explore technological solutions that align with data protection laws and regulations of each Asian country. Look for software or tools that can automate or streamline parts of the helpline process, such as categorizing calls or messages for more efficient handling.<br>Estimated Time: 2-3 months",

                4:"**Process Improvement:**<br>Review the current helpline process to identify bottlenecks or inefficiencies specific to each Asian country. Consider cultural and linguistic factors that may affect response time and find ways to improve the process accordingly.<br>Estimated Time: Ongoing",

                5:"**User Feedback Collection:**<br>Regularly collect feedback from helpline users in each Asian country, taking into account cultural preferences and communication channels. Focus on responsiveness and incorporate user feedback to continuously improve the helpline service.<br>Estimated Time: Ongoing"
            },
            'Europe': {
                0:"**Response Time Monitoring:**<br>Implement response time monitoring systems that track how quickly helpline staff are responding to calls or messages.<br>Estimated Time: 1-2 weeks",

                1:"**Staff Training:**<br>Conduct intensive training for helpline staff to improve their ability to provide quick and efficient service to callers.<br>Estimated Time: 2-3 weeks",

                2:"**Staff Augmentation:**<br> Consider increasing the number of staff or volunteers during peak call times, to prevent bottlenecks and reduce response time.<br>Estimated Time: 1-2 months",

                3:"**Technology Improvements:**<br>Look for technological solutions to automate or streamline parts of the helpline process. This might include software that quickly categorizes calls or messages, so they can be dealt with more efficiently.<br>Estimated Time: 2-3 months",

                4:"**Process Improvement:**<br>Review the current process to identify bottlenecks or inefficiencies that could be contributing to high response times, and find ways to improve them.<br>Estimated Time: Ongoing",

                5:"**User Feedback Collection:**<br>Regularly collect feedback from users on their experience with the helpline, focusing on responsiveness. This feedback can be used to continuously improve the service.<br>Estimated Time: Ongoing"
            },
            'North America': {
                0:"**Response Time Monitoring:**<br>Implement response time monitoring systems specific to North America. Track and analyze how quickly helpline staff are responding to calls or messages, considering the cultural preferences and expectations of users in North America.<br>Estimated Time: 1-2 weeks",

                1:"**Staff Training:**<br>Conduct intensive training for helpline staff in North America to enhance their skills and improve their ability to provide quick and efficient service to callers. Consider cultural nuances and communication styles prevalent in North America to ensure effective and empathetic responses.<br>Estimated Time: 2-3 weeks",

                2:"**Staff Augmentation:**<br>Assess the demand patterns in North America and consider increasing the number of staff or volunteers during peak call times. This helps prevent bottlenecks and reduces response time by ensuring adequate resources are available to meet the demands of users in North America.<br>Estimated Time: 1-2 months",
                
                    
                3:"**Technology Improvements:**<br>Explore technological solutions tailored to the North American context. Look for software or tools that can automate or streamline parts of the helpline process, such as call categorization or prioritization. Implementing such technologies can significantly improve response time and efficiency.<br>Estimated Time: 2-3 months",
                
                4:"**Process Improvement:**<br>Continuously review and optimize the helpline's processes in North America to identify and address bottlenecks or inefficiencies contributing to high response times. Consider cultural sensitivities and local preferences to adapt the processes effectively and improve overall response time.<br>Estimated Time: Ongoing",
                
                
                5:"**User Feedback Collection:**<br>Establish mechanisms to regularly collect feedback from users in North America, specifically focusing on their experience with the helpline's responsiveness. Utilize this feedback to gain insights into user expectations and continuously improve the service, ensuring timely responses.<br>Estimated Time: Ongoing"
            },
            'South America': {
                0:"**Response Time Monitoring:**<br>Implement response time monitoring systems that track how quickly helpline staff in South America are responding to calls or messages. Analyze and optimize response times based on the cultural expectations and preferences of South American users.<br>Estimated Time: 1-2 weeks",
                
                1:"**Staff Training:**<br>Conduct intensive training programs for helpline staff in South America to enhance their skills and improve their ability to provide quick and efficient service to callers. Emphasize cultural sensitivity and understanding of the diverse communities in South America.<br>Estimated Time: 2-3 weeks",
                
                
                2:"**Staff Augmentation:**<br>Assess the demand patterns specific to South America and consider increasing the number of staff or volunteers during peak call times. This ensures sufficient resources are available to handle high call volumes and reduce response time.<br>Estimated Time: 1-2 months",
                
                
                3:"**Technology Improvements:**<br>Explore technological solutions tailored to the South American context. Implement software or tools that can automate processes, streamline call handling, and improve overall efficiency. Consider integrating multilingual capabilities to better serve diverse populations in South America.<br>Estimated Time: 2-3 months",
                
                
                4:"**Process Improvement:**<br>Continuously review and optimize the helpline's processes in South America to identify and address bottlenecks or inefficiencies that contribute to high response times. Adapt processes to align with the cultural, linguistic, and regulatory requirements of South American users.<br>Estimated Time: Ongoing",
                
                5:"**User Feedback Collection:**<br>Establish mechanisms to regularly collect feedback from users in South America, focusing on their experience with the helpline's responsiveness. Leverage user insights to make informed decisions and continuously improve response times and service quality.<br>Estimated Time: Ongoing"
            },
            'Australia': {
                0:"**Response Time Monitoring:**<br>Implement response time monitoring systems specific to the Australian context. Track and analyze how quickly helpline staff are responding to calls or messages, considering the cultural preferences and expectations of Australian users.<br>Estimated Time: 1-2 weeks",
                

                1:"**Staff Training:**<br>Conduct intensive training for helpline staff in Australia to enhance their skills and improve their ability to provide quick and efficient service to callers. Emphasize the importance of timely responses and provide strategies for managing high call volumes effectively.<br>Estimated Time: 2-3 weeks",
                
                2:"**Staff Augmentation:**<br>Assess the demand patterns and consider increasing the number of staff or volunteers during peak call times in Australia. This helps prevent bottlenecks and reduces response time by ensuring adequate resources are available when needed.<br>Estimated Time: 1-2 months",
                
                3:"**Technology Improvements:**<br>Explore technological solutions tailored to the Australian helpline's needs. Look for software or tools that can automate or streamline parts of the helpline process, such as call categorization or prioritization. Implementing such technologies can significantly improve response time and efficiency.<br>Estimated Time: 2-3 months",
                

                4:"**Process Improvement:**<br>Continuously review and optimize the helpline's processes in Australia to identify and address bottlenecks or inefficiencies contributing to high response times. Regularly solicit feedback from staff and users to identify areas for improvement and implement changes accordingly.<br>Estimated Time: Ongoing",
                


                5:"**User Feedback Collection:**<br>Establish mechanisms to regularly collect feedback from users in Australia, specifically focusing on their experience with the helpline's responsiveness. Utilize this feedback to gain insights into user expectations and continuously improve the service, ensuring timely responses.<br>Estimated Time: Ongoing"
            }
        }
    },
    {
        'question': 'How confident are you in the overall quality and impact of helpline services for improving the well-being and safety of children?',
        'topic': "Multi-platform accessibilty",
        'weight': 0.089,
        'answers': {
            '0. Developing multi-platform accessibility': 0,
            '1. User Interface (UI) / User Experience (UX) Optimization': 1,
            '2. Language Localization': 2,
            '3. User Testing': 3,
            '4. Feedback Mechanism': 4,
            '5. Personalization': 5
        },
        'recomendations': {
            'Africa': {
                0:"**Developing Multi-platform Accessibility:**<br>Ensure your helpline service is accessible on multiple platforms (websites, mobile applications, social media, etc.) that comply with data protection and privacy laws specific to each African country. Consider compatibility with various devices commonly used in the region.<br>Estimated Time: 1-2 months",

                1:"**User Interface (UI) / User Experience (UX) Optimization:**<br>Conduct UI/UX testing and optimization with consideration for cultural preferences, design aesthetics, and usability standards prevalent in each African country. Continuously improve the helpline's user-friendliness and effectiveness.<br>Estimated Time: 1-2 months, ongoing",

                2:"**Language Localization:**<br>Incorporate local languages specific to each African country into the helpline platform to ensure accessibility for non-English speaking users. Comply with language-related laws and regulations in each country.<br>Estimated Time: 2 weeks per language, ongoing",

                3:"**User Testing:**<br>Conduct user testing sessions across different African countries to gain insights into the user's journey and experience. Identify any potential issues or areas of improvement specific to each country's cultural preferences and technological infrastructure.<br>Estimated Time: 2 weeks, ongoing",

                4:"**Feedback Mechanism:**<br>Develop a feedback mechanism that respects data protection and privacy laws in each African country, allowing users to rate their experience and provide suggestions for improvement. Ensure compliance with local regulations for collecting and processing user feedback.<br>Estimated Time: 1 week to implement, ongoing",

                5:"**Personalization:**<br>Explore ways to personalize the user experience based on past interactions, preferences, and user behavior while adhering to data protection and privacy laws specific to each African country. Implement personalization features that respect cultural norms and legal frameworks.<br>Estimated Time: 3-6 months"

        },
            'Asia': {
               0:"**Developing Multi-platform Accessibility:**<br>Ensure your helpline service is accessible on multiple platforms (websites, mobile applications, social media, etc.) that comply with data protection and privacy laws specific to each Asian country. Ensure compatibility with various devices prevalent in the region.<br>Estimated Time: 1-2 months",

                1:"**User Interface (UI) / User Experience (UX) Optimization:**<br>Conduct UI/UX testing and optimization with consideration for cultural preferences, design aesthetics, and usability standards prevalent in each Asian country. Continuously improve the helpline's user-friendliness and effectiveness.<br>Estimated Time: 1-2 months, ongoing",

                2:"**Language Localization:**<br>Incorporate local languages specific to each Asian country into the helpline platform to ensure accessibility for non-English speaking users. Comply with language-related laws and regulations in each country.<br>Estimated Time: 2 weeks per language, ongoing",

                3:"**User Testing:**<br>Conduct user testing sessions across different Asian countries to gain insights into the user's journey and experience. Identify any potential issues or areas of improvement specific to each country's cultural preferences and technological infrastructure.<br>Estimated Time: 2 weeks, ongoing",

                4:"**Feedback Mechanism:**<br>Develop a feedback mechanism that respects data protection and privacy laws in each Asian country, allowing users to rate their experience and provide suggestions for improvement. Ensure compliance with local regulations for collecting and processing user feedback.<br>Estimated Time: 1 week to implement, ongoing",

                5:"**Personalization:**<br>Explore ways to personalize the user experience based on past interactions, preferences, and user behavior while adhering to data protection and privacy laws specific to each Asian country. Implement personalization features that respect cultural norms and legal frameworks.<br>Estimated Time: 3-6 months",
            },
            'Europe': {
                0:"**Developing Multi-platform Accessibility:**<br>Ensure your helpline service is accessible on multiple platforms (websites, mobile applications, social media, etc.) and compatible with various devices.<br>Estimated Time: 1-2 months",

                1:"**User Interface (UI) / User Experience (UX) Optimization:**<br>Implement a process of constant UI/UX testing and optimization to make the helpline more user-friendly and effective.<br>Estimated Time: 1-2 months, ongoing",

                2:"**Language Localization:**<br>Incorporate local languages into the platform to ensure it's accessible to non-English speaking users.<br>Estimated Time: 2 weeks per language, ongoing",

                3:"**User Testing:**<br>Perform user testing sessions to gain insights into the user's journey and experience, and to spot any potential issues or areas of improvement.<br>Estimated Time: 2 weeks, ongoing",

                4:"**Feedback Mechanism:**<br>Develop a feedback mechanism where users can rate their experience and provide suggestions for improvement.<br>Estimated Time: 1 week to implement, ongoing",

                5:"**Personalization:**<br>Explore ways to personalize the user experience based on past interactions, preferences, and user behavior.<br>Estimated Time: 3-6 months",
            },
            'North America': {
               0:"**Developing Multi-platform Accessibility:**<br>Ensure your helpline service in North America is accessible on multiple platforms (websites, mobile applications, social media, etc.) and compatible with various devices commonly used in the region.<br>Estimated Time: 1-2 months",
                
                
                1:"**User Interface (UI) / User Experience (UX) Optimization:**<br>Implement a process of constant UI/UX testing and optimization to make the helpline more user-friendly and effective for North American users. Consider cultural preferences and user behavior specific to North America.<br>Estimated Time: 1-2 months, ongoing",
                
                2:"**Language Localization:**<br>Incorporate local languages commonly spoken in North America into the helpline platform to ensure it's accessible to non-English speaking users. Consider languages such as Spanish, French, and other regional languages.<br>Estimated Time: 2 weeks per language, ongoing",
                
                
                3:"**User Testing:**<br>Conduct user testing sessions specifically with North American users to gain insights into their journey and experience with the helpline. Identify potential issues or areas of improvement specific to the North American user base.<br>Estimated Time: 2 weeks, ongoing",
                
                4:"**Feedback Mechanism:**<br>Develop a feedback mechanism where North American users can rate their experience and provide suggestions for improvement. Use the feedback to continuously enhance the helpline service based on the specific needs and preferences of North American users.<br>Estimated Time: 1 week to implement, ongoing",
                
                5:"**Personalization:**<br>Explore ways to personalize the user experience for North American users based on their past interactions, preferences, and behavior. Tailor the helpline service to cater to their specific needs, enhancing user engagement and satisfaction.<br>Estimated Time: 3-6 months"
            },
            'South America': {
                0:"**Developing Multi-platform Accessibility:**<br>Ensure your helpline service in South America is accessible on multiple platforms (websites, mobile applications, social media, etc.) and compatible with various devices commonly used in the region.<br>Estimated Time: 1-2 months",
                
                1:"**User Interface (UI) / User Experience (UX) Optimization:**<br>Implement a process of constant UI/UX testing and optimization to make the helpline more user-friendly and effective for South American users. Consider cultural preferences and user behavior specific to South America.<br>Estimated Time: 1-2 months, ongoing",
                
                2:"**Language Localization:**<br>Incorporate local languages commonly spoken in South America into the helpline platform to ensure it's accessible to non-English speaking users. Consider languages such as Spanish, Portuguese, and other regional languages.<br>Estimated Time: 2 weeks per language, ongoing",
                
                3:"**User Testing:**<br>Conduct user testing sessions specifically with South American users to gain insights into their journey and experience with the helpline. Identify potential issues or areas of improvement specific to the South American user base.<br>Estimated Time: 2 weeks, ongoing",
                
                
                4:"**Feedback Mechanism:**<br>Develop a feedback mechanism where South American users can rate their experience and provide suggestions for improvement. Use the feedback to continuously enhance the helpline service based on the specific needs and preferences of South American users.<br>Estimated Time: 1 week to implement, ongoing",
                
                5:"**Personalization:**<br>Explore ways to personalize the user experience for South American users based on their past interactions, preferences, and behavior. Tailor the helpline service to cater to their specific needs, enhancing user engagement and satisfaction.<br>Estimated Time: 3-6 months"
            },
            'Australia': {
                0:"**Developing Multi-platform Accessibility:**<br> Ensure your helpline service in Australia is accessible on multiple platforms (websites, mobile applications, social media, etc.) and compatible with various devices commonly used in the country.<br>Estimated Time: 1-2 months",
                
                1:"**User Interface (UI) / User Experience (UX) Optimization:**<br>Implement a process of constant UI/UX testing and optimization to make the helpline more user-friendly and effective for Australian users. Consider cultural preferences and user behavior specific to Australia.<br>Estimated Time: 1-2 months, ongoing",
                
                2:"**Language Localization:**<br>Incorporate local languages commonly spoken in Australia, such as English and indigenous languages, into the helpline platform to ensure it's accessible to a diverse range of users.<br>Estimated Time: 2 weeks per language, ongoing",
                
                
                3:"**User Testing:**<br>Conduct user testing sessions specifically with Australian users to gain insights into their journey and experience with the helpline. Identify potential issues or areas of improvement specific to the Australian user base.<br>Estimated Time: 2 weeks, ongoing",
                
                
                4:"**Feedback Mechanism:**<br>Develop a feedback mechanism where Australian users can rate their experience and provide suggestions for improvement. Use the feedback to continuously enhance the helpline service based on the specific needs and preferences of Australian users.<br>Estimated Time: 1 week to implement, ongoing",
                
                5:"**Personalization:**<br>Explore ways to personalize the user experience for Australian users based on their past interactions, preferences, and behavior. Tailor the helpline service to cater to their specific needs, enhancing user engagement and satisfaction.<br>Estimated Time: 3-6 months"
            }
        }
    },
    {
        'question': 'How knowledgeable are the helpline staff about the specific issues and challenges faced by children in your country?',
        'topic': "Low Customer Satisfaction",
        'weight': 0.051,
        'answers': {
            '0. Staff training programs': 0,
            '1. Peer Learning Sessions': 1,
            '2. Hiring Specialized Professionals': 2,
            '3. Continuous Feedback Mechanism': 3,
            '4. Collaboration with Child Welfare Organizations': 4,
            '5. Psychosocial Support for Staff': 5
        },
        'recomendations': {
            'Africa': {
                0:"**Staff Training Programs:**<br Develop comprehensive training programs for the staff that address the unique issues and challenges faced by children in each African country. Customize the training content to align with local cultural norms, legal frameworks, and language preferences.<br>Estimated Time: 4 weeks for initial training, then ongoing",

                1:"**Peer Learning Sessions:**<br>Encourage peer learning sessions where staff members can share their experiences and learn from each other, considering the cultural diversity and regional differences within the African context. Promote cross-cultural understanding and sensitivity.<br>Estimated Time: Ongoing",

                2:"**Hiring Specialized Professionals:**<br>Prioritize hiring staff with expertise in child psychology, social work, or relevant fields who have a deep understanding of the local cultural context and specific challenges faced by children in African countries. This will enhance the quality of assistance provided and ensure culturally appropriate support.<br>Estimated Time: Variable, depending on hiring process",

                3:"**Continuous Feedback Mechanism:**<br>Implement a feedback mechanism to assess staff performance and identify areas for improvement, respecting data protection and privacy laws in each African country. Incorporate feedback from both peers and helpline users to continuously enhance service quality.<br>Estimated Time: 2 weeks to implement, ongoing",

                4:"**Collaboration with Child Welfare Organizations:**<br>Foster partnerships and collaborations with local child welfare organizations in each African country. Engage in knowledge sharing, joint training initiatives, and stay updated on current issues and best practices relevant to the local context.<br>Estimated Time: Ongoing",

                5:"**Psychosocial Support for Staff:**<br>Prioritize the well-being of staff members by providing necessary psychosocial support services, such as counseling or debriefing sessions, to prevent burnout and help them cope with the emotional toll of their work. Adapt support programs to address cultural sensitivities and mental health perspectives prevalent in each African country.<br>Estimated Time: Ongoing"
        },
            'Asia': {
                0:"**Staff Training Programs:**<br>Develop comprehensive training programs for the staff that cover the wide range of issues and challenges faced by children in each Asian country. Customize the training content to align with local cultural norms, legal frameworks, and language preferences.<br>Estimated Time: 4 weeks for initial training, then ongoing",

                1:"**Peer Learning Sessions:**<br>Encourage peer learning sessions where staff members can share their experiences and learn from each other, considering the cultural diversity and regional differences within the Asian context. Promote cross-cultural understanding and sensitivity.<br>Estimated Time: Ongoing",

                2:"**Hiring Specialized Professionals:**<br>Where possible, prioritize hiring staff with expertise in child psychology, social work, or relevant fields who have a deep understanding of the local cultural context. This will enhance the quality of assistance provided and ensure culturally appropriate support.<br>Estimated Time: Variable, depending on hiring process",

                3:"**Continuous Feedback Mechanism:**<br>Implement a feedback mechanism to assess staff performance and identify areas for improvement, respecting data protection and privacy laws in each Asian country. Incorporate feedback from both peers and helpline users to continuously enhance service quality.<br>Estimated Time: 2 weeks to implement, ongoing",

                4:"**Collaboration with Child Welfare Organizations:**<br>Foster partnerships and collaborations with local child welfare organizations in each Asian country. Engage in knowledge sharing, joint training initiatives, and stay updated on current issues and best practices relevant to the local context.<br>Estimated Time: Ongoing",

                5:"**Psychosocial Support for Staff:**<br>Prioritize the well-being of staff members by providing necessary psychosocial support services, such as counseling or debriefing sessions, to prevent burnout and help them cope with the emotional toll of their work. Adapt support programs to address cultural sensitivities and mental health perspectives prevalent in each Asian country.<br>Estimated Time: Ongoing"

            },
            'Europe': {
                0:"**Staff Training Programs:**<br>Develop comprehensive training programs for the staff that cover the wide range of issues and challenges faced by children in your country.<br>Estimated Time: 4 weeks for initial training, then ongoing",

                1:"**Peer Learning Sessions:**<br>Encourage peer learning sessions where staff members can share their experiences and learn from each other.<br>Estimated Time: Ongoing",

                2:"**Hiring Specialized Professionals:**<br>Where possible, hire staff with expertise in child psychology, social work, or relevant fields to enhance the quality of assistance provided.<br>Estimated Time: Variable, depending on hiring process",

                3:"**Continuous Feedback Mechanism:**<br>Implement a feedback mechanism to assess staff performance and identify areas for improvement. This could involve both peer feedback and feedback from helpline users.<br>Estimated Time: 2 weeks to implement, ongoing",

                4:"**Collaboration with Child Welfare Organizations:**<br>Collaborate with local child welfare organizations for staff training, knowledge sharing, and to stay updated on current issues and best practices.<br>Estimated Time: Ongoing",

                5:"**Psychosocial Support for Staff:**<br>Provide psychosocial support for staff members to prevent burnout and to help them cope with the emotional toll of their work.<br>Estimated Time: Ongoing"
            },
            'North America': {
                0:"**Staff Training Programs:**<br>Develop comprehensive training programs for the staff that cover the wide range of issues and challenges faced by children in North America.<br>Estimated Time: 4 weeks for initial training, then ongoing",
                
                1:"**Peer Learning Sessions:**<br>Encourage peer learning sessions where staff members can share their experiences and learn from each other. Foster a collaborative environment that promotes continuous learning and improvement.<br>Estimated Time: Ongoing",
                
                2:"**Hiring Specialized Professionals:**<br>Where possible, hire staff with expertise in child psychology, social work, or relevant fields to enhance the quality of assistance provided. Seek professionals who have a deep understanding of the specific challenges and cultural context of North America.<br>Estimated Time: Variable, depending on the hiring process",
                
                3:"**Continuous Feedback Mechanism:**<br>Implement a feedback mechanism to assess staff performance and identify areas for improvement. This could involve both peer feedback and feedback from helpline users. Regularly review and provide constructive feedback to staff members to enhance their skills and effectiveness.<br>Estimated Time: 2 weeks to implement, ongoing",
                
                4:"**Collaboration with Child Welfare Organizations:**<br>Collaborate with local child welfare organizations for staff training, knowledge sharing, and to stay updated on current issues and best practices. Establish partnerships and regular communication channels to ensure your staff remains knowledgeable about the latest developments in child welfare in North America.<br>Estimated Time: Ongoing",
                
                5:"**Psychosocial Support for Staff:**<br>Provide psychosocial support for staff members to prevent burnout and help them cope with the emotional toll of their work. Offer resources such as counseling, debriefing sessions, and self-care programs to support the well-being and retention of your staff.<br>Estimated Time: Ongoing"
            },
            'South America': {
                0:"**Staff Training Programs:**<br Develop comprehensive training programs for the staff that cover the wide range of issues and challenges faced by children in South America. Take into account the specific cultural, social, and linguistic aspects of the region to ensure the training is relevant and effective.<br>Estimated Time: 4 weeks for initial training, then ongoing",
                
                1:"**Peer Learning Sessions:**<br>Encourage peer learning sessions where staff members can share their experiences and learn from each other. Create a collaborative environment that fosters continuous learning and improvement, taking into consideration the unique cultural and regional factors of South America.<br>Estimated Time: Ongoing",
                
                2:"**Hiring Specialized Professionals:**<br>Where possible, hire staff with expertise in child psychology, social work, or relevant fields, who are familiar with the specific challenges faced by children in South America. Seek professionals who have a deep understanding of the cultural diversity and context of the region.<br>Estimated Time: Variable, depending on the hiring process",
                
                
                3:"**Continuous Feedback Mechanism:**<br>Implement a feedback mechanism to assess staff performance and identify areas for improvement. This could involve both peer feedback and feedback from helpline users. Regularly review and provide constructive feedback to staff members to enhance their skills and effectiveness, considering the cultural nuances and diverse needs of the South American population.<br>Estimated Time: 2 weeks to implement, ongoing",
                
                4:"**Collaboration with Child Welfare Organizations:**<br>Collaborate with local child welfare organizations in South America for staff training, knowledge sharing, and to stay updated on current issues and best practices. Establish partnerships and regular communication channels to ensure your staff remains knowledgeable about the regional challenges and culturally appropriate approaches.<br>Estimated Time: Ongoing",
                
                5:"**Psychosocial Support for Staff:**<br>Provide psychosocial support for staff members to prevent burnout and help them cope with the emotional toll of their work. Offer resources such as counseling, debriefing sessions, and self-care programs that are sensitive to the cultural and regional context of South America.<br>Estimated Time: Ongoing"

            },
            'Australia': {
                0:"**Developing Multi-platform Accessibility:**<br>Ensure your helpline service in Australia is accessible on multiple platforms (websites, mobile applications, social media, etc.) and compatible with various devices commonly used in the country.<br>stimated Time: 1-2 months",
                
                1:"**User Interface (UI) / User Experience (UX) Optimization:**<br>Implement a process of constant UI/UX testing and optimization to make the helpline more user-friendly and effective for Australian users. Consider cultural preferences and user behavior specific to Australia.<br>Estimated Time: 1-2 months, ongoing",
                
                2:"**Language Localization:**<br>Incorporate local languages commonly spoken in Australia, such as English and indigenous languages, into the helpline platform to ensure it's accessible to a diverse range of users.<br>Estimated Time: 2 weeks per language, ongoing",
                
                
                3:"**User Testing:**<br>Conduct user testing sessions specifically with Australian users to gain insights into their journey and experience with the helpline. Identify potential issues or areas of improvement specific to the Australian user base.<br>Estimated Time: 2 weeks, ongoing",
                
                
                4:"**Feedback Mechanism:**<br>Develop a feedback mechanism where Australian users can rate their experience and provide suggestions for improvement. Use the feedback to continuously enhance the helpline service based on the specific needs and preferences of Australian users.vEstimated Time: 1 week to implement, ongoing",
                
                
                5:"**Personalization:**<br>Explore ways to personalize the user experience for Australian users based on their past interactions, preferences, and behavior. Tailor the helpline service to cater to their specific needs, enhancing user engagement and satisfaction.<br>Estimated Time: 3-6 months"
            }
        }
    },
    {
        'question': 'To what extent are helpline services tailored to meet the diverse cultural and linguistic needs of children in your country?',
        'topic': "Staffed with well-trained professionals ",
        'weight': 0.161,
        'answers': {
            '0. Diversity and inclusion training': 0,
            '1. Multilingual Staff Hiring': 1,
            '2. Partnerships with Cultural Organisations': 2,
            '3. Cultural Sensitivity Audits': 3,
            '4. Community Outreach Programs': 4,
            '5. Continuous Improvement of Training Programs': 5
        },
        'recomendations': {
            'Africa': {
                0:"**Diversity and Inclusion Training:**<br>Implement Diversity and Inclusion training programs that are culturally sensitive and address the unique diversity within the African context. Train staff to understand and respect cultural differences, enabling them to offer sensitive and effective help to children from various cultural backgrounds.<br>Estimated Time: 1-2 weeks",


                1:"**Multilingual Staff Hiring:**<br>Prioritize hiring staff proficient in local languages spoken across different African countries. This will enhance accessibility and ensure effective communication with children who may not be fluent in the official or colonial languages.<br>Estimated Time: Depends on the hiring process",


                2:"**Partnerships with Cultural Organizations:**<br>Establish partnerships with local cultural organizations and community leaders in different African countries to foster cultural sensitivity, gain insights into specific cultural practices, and understand the unique needs and challenges faced by children in each cultural context.<br>Estimated Time: Ongoing",

                3:"**Cultural Sensitivity Audits:**<br>Conduct regular audits of helpline interactions to ensure they are culturally sensitive, inclusive, and respectful of local customs and practices. Use these audits to identify areas for improvement and provide feedback and training to staff members.<br>Estimated Time: Ongoing, with more comprehensive audits every 6-12 months",

                4:"**Community Outreach Programs:**<br>Implement targeted community outreach programs in diverse cultural communities across Africa. Collaborate with local leaders, community-based organizations, and traditional authorities to better understand the unique needs and challenges faced by children from different cultural backgrounds. Tailor the helpline services to address these specific cultural contexts.<br>Estimated Time: Variable, depending on the scope and scale of outreach initiatives",

                5:"**Continuous Improvement of Training Programs:**<br>Continually revise and update the training programs based on feedback from staff members, community members, and cultural experts in the African context. Regularly assess the training content to ensure it remains culturally relevant, inclusive, and effective in addressing the needs of diverse populations.<br>Estimated Time: Ongoing"
        },
            'Asia': {
                
                0:"**Diversity and Inclusion Training:**<br>Implement Diversity and Inclusion training programs tailored to the diverse cultural landscape of the Asia region. Train staff to understand and respect cultural differences, enabling them to offer sensitive and effective help to children from various cultural backgrounds.vEstimated Time: 1-2 weeks",

                1:"**1. Multilingual Staff Hiring:**<br>Prioritize hiring staff proficient in different languages spoken in the region, considering the linguistic diversity of the countries served. This will enhance accessibility and ensure effective communication with children who may not be fluent in the official or dominant language.<br>Estimated Time: Depends on the hiring process",


                2:"**Partnerships with Cultural Organizations:**<br>Forge partnerships with local cultural organizations across different Asian countries to facilitate staff training and stay informed about specific cultural practices, customs, and sensitivities. These collaborations will enable a more culturally informed and responsive approach.<br>Estimated Time: Ongoing",


                3:"**Cultural Sensitivity Audits:**<br>Conduct regular audits of helpline interactions to ensure they are culturally sensitive and inclusive. Use these audits to identify areas for improvement and provide feedback and training to staff members.<br>Estimated Time: Ongoing, with more comprehensive audits every 6-12 months",

                4:"**Community Outreach Programs:**<br>Implement targeted community outreach programs in diverse cultural communities across the region. Engage with local community leaders, cultural associations, and religious institutions to better understand the unique needs and challenges faced by children from different cultures. This will help tailor the helpline services to the specific cultural contexts.<br>Estimated Time: Variable, depending on the scope and scale of outreach initiatives",

                5:"**Continuous Improvement of Training Programs:**<br>Continually revise and update the training programs based on feedback from staff members, community members, and cultural experts. Regularly assess the training content to ensure it remains culturally relevant, inclusive, and effective in addressing the needs of diverse populations.<br>Estimated Time: Ongoing"
            },
            'Europe': {
                0:"**Diversity and Inclusion Training:**<br>Implement Diversity and Inclusion training to help staff understand and respect cultural differences. This will enable them to offer more sensitive and effective help to children from various cultural backgrounds.<br>Estimated Time: 1-2 weeks",

                1:"**Multilingual Staff Hiring:**<br>Hire staff proficient in different languages spoken in your country, to cater to the linguistic diversity of the children reaching out for help.<br>Estimated Time: Depends on the hiring process",

                2:"**Partnerships with Cultural Organisations:**<br>Partner with cultural organizations for training staff and to stay informed about specific cultural practices and sensitivities.<br>Estimated Time: Ongoing",

                3:"**Cultural Sensitivity Audits:**<br>Conduct regular audits of helpline interactions to ensure that they are culturally sensitive and inclusive. Use these audits to identify areas for improvement.<br>Estimated Time: Ongoing, with more comprehensive audits every 6-12 months",

                4:"**Community Outreach Programs:**<br>Implement community outreach programs in different cultural communities. This will help the organization understand the unique needs and challenges faced by children from different cultures.<br>Estimated Time: Variable",

                5:"**Continuous Improvement of Training Programs:**<br>Continually revise and update the training programs based on feedback from staff and community members. This will ensure that the training remains relevant and effective.<br>Estimated Time: Ongoing"
            },
            'North America': {
                0:"**Diversity and Inclusion Training:**<br>Implement diversity and inclusion training to help staff understand and respect cultural differences. This training will enable them to offer more sensitive and effective help to children from various cultural backgrounds in North America.<br>Estimated Time: 1-2 weeks",
                

                1:"**Multilingual Staff Hiring:**<br>Hire staff proficient in different languages spoken in North America to cater to the linguistic diversity of the children reaching out for help. This will ensure that language barriers do not hinder access to support services.<br>Estimated Time: Depends on the hiring process",
                

                2:"**Partnerships with Cultural Organizations:**<br>Establish partnerships with cultural organizations in North America for staff training and to stay informed about specific cultural practices and sensitivities. These partnerships will provide valuable insights and resources for promoting cultural sensitivity.<br>Estimated Time: Ongoing",
                

                3:"**Cultural Sensitivity Audits:**<br>Conduct regular audits of helpline interactions to ensure that they are culturally sensitive and inclusive. Use these audits to identify areas for improvement and provide feedback to staff members. This ongoing evaluation process will contribute to the continuous improvement of service quality.<br>Estimated Time: Ongoing, with more comprehensive audits every 6-12 months",
                
                4:"**Community Outreach Programs:**<br>Implement community outreach programs in different cultural communities in North America. This will help the organization understand the unique needs and challenges faced by children from different cultures and enable the development of culturally appropriate strategies.<br>Estimated Time: Variable",
                

                5:"**Continuous Improvement of Training Programs:**<br>Continually revise and update the training programs based on feedback from staff and community members. This will ensure that the training remains relevant and effective in promoting diversity and inclusion within the helpline service.<br>Estimated Time: Ongoing"
            },
            'South America': {
                0:"**Diversity and Inclusion Training:**<br>Implement diversity and inclusion training to help staff understand and respect cultural differences. This training will enable them to offer more sensitive and effective help to children from various cultural backgrounds in South America.<br>Estimated Time: 1-2 weeks",
                

                1:"**Multilingual Staff Hiring:**<br>Hire staff proficient in different languages spoken in South America to cater to the linguistic diversity of the children reaching out for help. This will ensure that language barriers do not hinder access to support services.<br>Estimated Time: Depends on the hiring process",
                

                2:"**Partnerships with Cultural Organizations:**<br>Establish partnerships with cultural organizations in South America for staff training and to stay informed about specific cultural practices and sensitivities. These partnerships will provide valuable insights and resources for promoting cultural sensitivity.<br>Estimated Time: Ongoing",
                

                3:"**Cultural Sensitivity Audits:**<br>Conduct regular audits of helpline interactions to ensure that they are culturally sensitive and inclusive. Use these audits to identify areas for improvement and provide feedback to staff members. This ongoing evaluation process will contribute to the continuous improvement of service quality.<br>Estimated Time: Ongoing, with more comprehensive audits every 6-12 months",
                
                4:"**Community Outreach Programs:**<br>Implement community outreach programs in different cultural communities in South America. This will help the organization understand the unique needs and challenges faced by children from different cultures and enable the development of culturally appropriate strategies.<br>Estimated Time: Variable",
                
                5:"**Continuous Improvement of Training Programs:**<br>Continually revise and update the training programs based on feedback from staff and community members. This will ensure that the training remains relevant and effective in promoting diversity and inclusion within the helpline service.<br>Estimated Time: Ongoing"
            },
            'Australia': {
                0:"**Diversity and Inclusion Training:**<br>Introduce and implement diversity and inclusion training to help staff understand and respect cultural differences. This training will enable them to offer more sensitive and effective help to children from various cultural backgrounds in Australia.<br>Estimated Time: 1-2 weeks",
                

                1:"**Multilingual Staff Hiring:** Hire staff proficient in different languages spoken in Australia to cater to the linguistic diversity of the children reaching out for help. This will ensure that language barriers do not hinder access to support services.<br>Estimated Time: Depends on the hiring process",
                

                2:"**Partnerships with Cultural Organizations:**<br>Establish partnerships with cultural organizations in Australia for staff training and to stay informed about specific cultural practices and sensitivities. These partnerships will provide valuable insights and resources for promoting cultural sensitivity.<br>Estimated Time: Ongoing",
                
                3:"**Cultural Sensitivity Audits:**<br>Conduct regular audits of helpline interactions to ensure that they are culturally sensitive and inclusive. Use these audits to identify areas for improvement and provide feedback to staff members. This ongoing evaluation process will contribute to the continuous improvement of service quality.<br>Estimated Time: Ongoing, with more comprehensive audits every 6-12 months",
                

                4:"**Community Outreach Programs:**<br>Implement community outreach programs in different cultural communities in Australia. This will help the organization understand the unique needs and challenges faced by children from different cultures and enable the development of culturally appropriate strategies.<br>Estimated Time: Variable",
                

                5:"**Continuous Improvement of Training Programs:**<br>Continually revise and update the training programs based on feedback from staff and community members. This will ensure that the training remains relevant and effective in promoting diversity and inclusion within the helpline service.<br>Estimated Time: Ongoing"
            }
        }
    },
    {
        'question': 'How effective are helplines in providing age-appropriate guidance and support to children based on their developmental stages (by adults or peers)?',
        'topic': "Quality of communication",
        'weight': 0.067,
        'answers': {
            '0. Developmental training for staff': 0,
            '1. Script Development for Different Age Groups': 1,
            '2. Peer Support Program': 2,
            '3. Feedback System': 3,
            '4. Collaboration with Child Psychologists': 4,
            '5. Regular Review and Update of Training Material': 5
        },
        'recomendations': {
            'Africa': {
                
                0:"**Developmental Training for Staff:**<br>Implement training sessions for helpline staff that focus on understanding the psychological and emotional development of children at different age stages within the context of the Africa region. This will enhance their ability to provide age-appropriate support that aligns with the cultural and social norms prevalent in the region.<br>Estimated Time: 1-2 weeks",


                1:"**Script Development for Different Age Groups:**<br>Develop comprehensive guidelines or scripts for helpline workers that cater to different age groups prevalent in the African region. Consider cultural nuances, languages, and social expectations to ensure effective and culturally sensitive communication.<br>Estimated Time: 1-2 weeks",


                2:"**Peer Support Program:**<br>Consider implementing a peer support program where older children or adolescents are trained to provide guidance and support to younger children. Ensure proper training and supervision to maintain the safety and effectiveness of the program within the cultural context of Africa.<br>Estimated Time: 2-3 months",

                3:"**Feedback System: Establish a robust feedback system where children and their caregivers can provide feedback on the support they received. Adapt the system to be culturally sensitive and accessible, considering languages, technology infrastructure, and social norms prevalent in the region.<br>Estimated Time: 1 week to set up, ongoing to maintain",

                4:"**Collaboration with Child Psychologists:**<br> Collaborate with local child psychologists or mental health professionals within the Africa region who have expertise in child development and cultural dynamics. Engage them as advisors to provide insights into children's developmental stages and cultural sensitivities, and to refine communication strategies.<br>Estimated Time: 1-2 weeks for initial consultations, ongoing collaboration",

                5:"**Regular Review and Update of Training Material:**<br>Continuously review and update training materials based on the latest child development research, staff feedback, and feedback from children within the cultural context of the Africa region. Adapt the materials to address specific cultural norms, languages, and regional dynamics.<br>Estimated Time: Ongoing, with reviews every 3-6 months"
        },
            'Asia': {
                0:"**Developmental Training for Staff:**<br>Implement training sessions for helpline staff that focus on understanding the psychological and emotional development of children at different age stages within the context of the Asia region. This will enhance their ability to provide age-appropriate support that aligns with the cultural and social norms prevalent in the region.<br>Estimated Time: 1-2 weeks",


                1:"**Script Development for Different Age Groups:**<br>Develop comprehensive guidelines or scripts for helpline workers that cater to different age groups prevalent in the Asian region. Consider cultural nuances, languages, and social expectations to ensure effective and culturally sensitive communication.<br>Estimated Time: 1-2 weeks",

                2:"**Peer Support Program:**<br>Consider implementing a peer support program where older children or adolescents are trained to provide guidance and support to younger children. Ensure proper training and supervision to maintain the safety and effectiveness of the program within the cultural context of Asia.<br>Estimated Time: 2-3 months",

                3:"**Feedback System:**<br>Establish a robust feedback system where children and their caregivers can provide feedback on the support they received. Adapt the system to be culturally sensitive and accessible, considering languages, technology infrastructure, and social norms prevalent in the region.<br>Estimated Time: 1 week to set up, ongoing to maintain",

                4:"**Collaboration with Child Psychologists:**<br>Collaborate with local child psychologists or mental health professionals within the Asian region who have expertise in child development and cultural dynamics. Engage them as advisors to provide insights into children's developmental stages and cultural sensitivities, and to refine communication strategies.<br>Estimated Time: 1-2 weeks for initial consultations, ongoing collaboration",

                5:"**Regular Review and Update of Training Material:**<br>Continuously review and update training materials based on the latest child development research, staff feedback, and feedback from children within the cultural context of the Asia region. Adapt the materials to address specific cultural norms, languages, and regional dynamics.<br>Estimated Time: Ongoing, with reviews every 3-6 months",

            },
            'Europe': {
                0:"**Developmental Training for Staff:**<br>Implement training sessions for helpline staff to understand the psychological and emotional development of children at different age stages. This will enhance their ability to provide age-appropriate support.<br>Estimated Time: 1-2 weeks",


                1:"**Script Development for Different Age Groups:**<br>Develop a guideline or script for helpline workers that cater to different age groups. This will provide a practical reference for age-appropriate communication.<br>Estimated Time: 1-2 weeks",


                2:"**Peer Support Programn:**<br>Implement a peer support program where older children or adolescents are trained to provide guidance to younger children. This can sometimes be more effective as children may feel more comfortable talking to their peers.<br>Estimated Time: 2-3 months",


                3:"**Feedback System:::<br>Establish a feedback system where children (or their caregivers) can provide feedback on the support they received. This will give insight into whether the support is age-appropriate and effective.<br>Estimated Time: 1 week to set up, ongoing to maintain",
                

                4:"**Collaboration with Child Psychologists:**<br>Collaborate with child psychologists who can provide professional insights into children's developmental stages and advise on best practices for communication.<br>Estimated Time: 1-2 weeks for initial consultations, ongoing collaboration",

                5:"**Regular Review and Update of Training Material:**<br>Regularly review and update training material based on the latest child development research, staff feedback, and feedback from children.<br>Estimated Time: Ongoing, with reviews every 3-6 months"
            },
            'North America': {
                0:"**Developmental Training for Staff:**<br>Implement training sessions for helpline staff to understand the psychological and emotional development of children at different age stages. This will enhance their ability to provide age-appropriate support in accordance with the developmental needs of children.<br>Estimated Time: 1-2 weeks",
                

                1:"**Script Development for Different Age Groups:**<br>Develop guidelines or scripts for helpline workers that cater to different age groups, taking into account specific natural disasters, such as hurricanes, earthquakes, or wildfires. These resources will serve as practical references for age-appropriate communication, ensuring consistent and effective support tailored to the unique challenges faced during and after such disasters.<br>Estimated Time: 1-2 weeks",
                

                2:"**Multilingual Staff Hiring:**<br>Hire staff proficient in different languages spoken in North America, considering the linguistic diversity of the region. This will ensure that children from various language backgrounds can access the helpline service and receive support in their preferred language.<br>Estimated Time: Depends on the hiring process",
                

                3:"**Collaboration with Cultural Organizations:**<br>Partner with cultural organizations representing diverse communities in North America to provide training to staff on cultural sensitivity and understanding. This collaboration will ensure that helpline workers are equipped to offer support that respects and appreciates the cultural differences and practices of the children they assist.<br>Estimated Time: Ongoing",
                
                4:"**Compliance with Data Protection Regulations:**<br> Ensure that the helpline service complies with data protection regulations specific to North America, such as the General Data Protection Regulation (GDPR) in Canada. Implement measures to safeguard the personal information and privacy of children and their families who seek assistance.<br>Estimated Time: Ongoing, with regular assessments and updates",
                
                5:"**Regular Review and Update of Training Material:**<br>Regularly review and update training material based on the latest child development research, staff feedback, and feedback from children, taking into account the specific cultural contexts and challenges in North America. This will ensure that the training programs remain relevant, effective, and aligned with the diverse needs of children in the region.<br>Estimated Time: Ongoing, with reviews every 3-6 months"
            },
            'South America': {
                0:"**Developmental Training for Staff:**<br>Implement training sessions for helpline staff to understand the psychological and emotional development of children at different age stages within South America. This will enhance their ability to provide age-appropriate support in accordance with the developmental needs of children.<br>Estimated Time: 1-2 weeks",


                1:"**Script Development for Different Age Groups:**<br>Develop guidelines or scripts for helpline workers that cater to different age groups, taking into account specific natural disasters, such as earthquakes, floods, volcanic eruptions, or tropical storms. These resources will serve as practical references for age-appropriate communication, ensuring consistent and effective support tailored to the unique challenges faced during and after such disasters.<br>Estimated Time: 1-2 weeks",


                2:"**Multilingual Staff Hiring:**<br>Hire staff proficient in different languages spoken in South America, considering the linguistic diversity of the region. This will ensure that children from various language backgrounds can access the helpline service and receive support in their preferred language.<br>Estimated Time: Depends on the hiring process",


                3:"**Collaboration with Cultural Organizations:**<br>Partner with cultural organizations representing diverse communities in South America to provide training to staff on cultural sensitivity and understanding. This collaboration will ensure that helpline workers are equipped to offer support that respects and appreciates the cultural differences and practices of the children they assist.<br>Estimated Time: Ongoing",


                4:"**Compliance with Data Protection Regulations:**<br>Ensure that the helpline service complies with data protection regulations specific to South America. Implement measures to safeguard the personal information and privacy of children and their families who seek assistance.<br>Estimated Time: Ongoing, with regular assessments and updates",


                5:"**Regular Review and Update of Training Material:**<br>Regularly review and update training material based on the latest child development research, staff feedback, and feedback from children, taking into account the specific cultural contexts and challenges in South America. This will ensure that the training programs remain relevant, effective, and aligned with the diverse needs of children in the region.<br>Estimated Time: Ongoing, with reviews every 3-6 months"
            },
            'Australia': {
                0:"**Developmental Training for Staff:**<br>Implement training sessions for helpline staff in the Australia region to understand the psychological and emotional development of children at different age stages. This will enhance their ability to provide age-appropriate support, taking into account the specific developmental needs and challenges faced by children in Australia.<br>Estimated Time: 1-2 weeks",


                1:"**Script Development for Different Age Groups:**<br>Develop a guideline or script for helpline workers that cater to different age groups prevalent in Australia. This will provide a practical reference for age-appropriate communication, considering the cultural and linguistic diversity within the country.<br>Estimated Time: 1-2 weeks",


                2:"**Peer Support Program:**<br>Implement a peer support program in the Australia region, where older children or adolescents are trained to provide guidance to younger children. This can be more effective as children may feel more comfortable talking to their peers, considering the cultural and social dynamics specific to Australia.<br>Estimated Time: 2-3 months",


                3:"**Feedback System:**<br>Establish a feedback system in the Australia region where children (or their caregivers) can provide feedback on the support they received. This will give insight into whether the support is age-appropriate and effective, taking into consideration the cultural sensitivities and expectations of the diverse communities in Australia.<br>Estimated Time: 1 week to set up, ongoing to maintain",


                4:"**Collaboration with Child Psychologists:**<br>Collaborate with child psychologists in Australia who can provide professional insights into children's developmental stages and advise on best practices for communication, considering the specific cultural, linguistic, and legal context of Australia.<br>Estimated Time: 1-2 weeks for initial consultations, ongoing collaboration",


                5:"**Regular Review and Update of Training Material:**<br>Regularly review and update training material based on the latest child development research, staff feedback, and feedback from children in the Australia region. Consider the cultural diversity and unique needs of Australian children when updating the material.<br>Estimated Time: Ongoing, with reviews every 3-6 months"
            }
        }
    },
    {
        'question': 'How satisfied are you with the accessibility of helplines for children in terms of availability and ease of contact?',
        'topic': "Ineffective Response / Service routing",
        'weight': 0.09,
        'answers': {
            '0. 24/7 Availability initiative': 0,
            '1. Effective Call Routing System': 1,
            '2. Multi-channel Contact Options': 2,
            '3. Promotion and Awareness Campaign': 3,
            '4. Usability Testing': 4,
            '5. Language Accessibility': 5
        },
        'recomendations': {
            'Africa': {
                0:"**24/7 Availability Initiative:**<br>Strive to provide 24/7 availability for the helpline in the Africa region, taking into account regional time zones, cultural practices, and infrastructure limitations. Explore options such as shifts, rota systems, or employing remote staff in different time zones.<br>Estimated Time: 2-4 weeks for planning and implementation",


                1:"**Effective Call Routing System:**<br>Implement an advanced call routing system that considers the linguistic and cultural diversity within the Africa region. Direct callers to staff members who can provide assistance in the appropriate language or cultural context.<br>Estimated Time: 1-2 months for procurement and setup",


                2:"**Multi-channel Contact Options:**<br>Expand the helpline to include text, email, and online chat options, considering the prevalence and accessibility of different communication channels in the Africa region. Take into account the preferences and comfort levels of children when selecting channels.<br>Estimated Time: 1-2 months for setup and testing",


                3:"**Promotion and Awareness Campaign:**<br>Launch a targeted promotional campaign tailored to the Africa region to increase awareness about the helpline and the different contact options available. Consider cultural nuances, languages, and communication channels preferred by the target audience.<br>Estimated Time: 1-2 months",


                4:"**Usability Testing:**<br>Conduct regular usability testing specific to the Africa region to identify potential issues in the contact process that may hinder accessibility. Consider factors such as language barriers, technological limitations, and cultural sensitivities during the testing process.<br>Estimated Time: Ongoing, with tests every 3-6 months",


                5:"**Language Accessibility:**<br>Ensure the helpline is accessible to non-native speakers in the Africa region by providing translation services or employing bilingual/multilingual staff who can communicate in the predominant languages spoken in the respective countries.<br>Estimated Time: Ongoing, as per requirement and availability of resources"
        },
            'Asia': {
                0:"**Localized 24/7 Availability Initiative:**<br>Strive to provide 24/7 availability for the helpline in line with local Asian time zones. This might require shifts, rota systems, or employing remote staff in different Asian regions.<br>Estimated Time: 2-4 weeks for planning and implementation",


                1:"**Localized Effective Call Routing System:**<br>Implement an advanced call routing system that caters to the varied linguistic and cultural nuances of Asia. This system should efficiently direct callers to the right staff member based on their needs.<br>Estimated Time: 1-2 months for procurement and setup",


                2:"**Localized Multi-channel Contact Options:**<br>Expand the helpline to include text, email, and online chat options with multi-language support considering the linguistic diversity in Asia. This could help children who may feel more comfortable using these channels.<br>Estimated Time: 1-2 months for setup and testing",


                3:"**Localized Promotion and Awareness Campaign:**<br>Launch a promotional campaign in local languages and through culturally relevant mediums to increase awareness about the helpline and the different ways Asian children can reach out for help.<br>Estimated Time: 1-2 months",

                4:"**Localized Usability Testing:**<br>Conduct regular usability testing with a diverse Asian user base to identify potential issues in the contact process that could be hindering accessibility.<br>Estimated Time: Ongoing, with tests every 3-6 months",

                5:"**Regional Language Accessibility:**<br>Given the vast number of languages spoken across Asia, ensure the helpline is accessible to non-native English speakers by providing translation services or employing bilingual/multilingual staff fluent in various Asian languages.<br>Estimated Time: Ongoing, as per requirement and availability of resources"
            },
            'Europe': {
                0:"**24/7 Availability Initiative:**<br>Strive to provide 24/7 availability for the helpline, potentially through shifts, rota systems, or employing remote staff in different time zones.<br>Estimated Time: 2-4 weeks for planning and implementation",

                1:"**Effective Call Routing System:**<br>Implement an advanced call routing system that efficiently directs callers to the right staff member based on their needs. This improves overall response effectiveness.<br>Estimated Time: 1-2 months for procurement and setup",


                2:"**Multi-channel Contact Options:**<br>Expand the helpline to include text, email, and online chat options, as some children may feel more comfortable using these channels.<br>Estimated Time: 1-2 months for setup and testing",


                3:"**Promotion and Awareness Campaign:**<br>Launch a promotional campaign to increase awareness about the helpline and the different ways children can reach out for help.<br>Estimated Time: 1-2 months",

                4:"**Usability Testing:**<br>Conduct regular usability testing to identify potential issues in the contact process that could be hindering accessibility.<br>Estimated Time: Ongoing, with tests every 3-6 months",


                5:"**Language Accessibility:**<br>Ensure the helpline is accessible to non-native speakers by providing translation services or employing bilingual/multilingual staff.<br>Estimated Time: Ongoing, as per requirement and availability of resources"
            },
            'North America': {
                0:"**24/7 Availability Initiative:**<br>Strive to provide 24/7 availability for the helpline in the America region, taking into account the different time zones across the continent. Explore options such as shifts, rota systems, or employing remote staff in different time zones to ensure accessibility at any time.<br>Estimated Time: 2-4 weeks for planning and implementation",


                1:"**Effective Call Routing System:**<br>Implement an advanced call routing system that considers the linguistic and cultural diversity within the America region. Direct callers to staff members who can provide assistance in the appropriate language or cultural context, taking into account the multiculturalism prevalent in the region.<br>Estimated Time: 1-2 months for procurement and setup",


                2:"**Multi-channel Contact Options:**<br>Expand the helpline to include text, email, and online chat options, considering the prevalence and accessibility of different communication channels in the America region. Take into account the preferences and comfort levels of children when selecting channels, while adhering to relevant privacy and data protection laws in each country.<br>Estimated Time: 1-2 months for setup and testing",


                3:"**Promotion and Awareness Campaign:**<br>Launch a targeted promotional campaign in the America region to increase awareness about the helpline and the different contact options available. Consider cultural nuances, languages, and communication channels preferred by the target audience, while ensuring compliance with advertising regulations and ethical guidelines in each country.<br>Estimated Time: 1-2 months",


                4:"**Usability Testing:**<br>Conduct regular usability testing specific to the America region to identify potential issues in the contact process that may hinder accessibility. Consider factors such as language barriers, technological limitations, and cultural sensitivities during the testing process, while complying with user testing standards and ethical guidelines.<br>Estimated Time: Ongoing, with tests every 3-6 months",


                5:"**Language Accessibility:**<br>Ensure the helpline is accessible to non-native English speakers in the America region by providing translation services or employing bilingual/multilingual staff who can communicate in the languages commonly spoken by diverse communities within each country in the region.<br>Estimated Time: Ongoing, as per requirement and availability of resources"
            },
            'South America': {
                0:"**Localized 24/7 Availability Initiative:**<br>Adapt the availability of the helpline to cater to the specific time zones across South America. This can be achieved through implementing shifts, rota systems, or employing remote staff in different regions.<br>Estimated Time: 2-4 weeks for planning and implementation",


                1:"**Localized Effective Call Routing System:**<br>Deploy an advanced call routing system that accommodates the cultural and linguistic diversity of South America, ensuring callers are directed to the right staff member based on their needs.<br>Estimated Time: 1-2 months for procurement and setup",


                2:"**Localized Multi-channel Contact Option:**<br>Broaden the helpline to include text, email, and online chat options, supporting Spanish, Portuguese, and other indigenous languages. This allows children to use the communication channel they are most comfortable with.<br>Estimated Time: 1-2 months for setup and testing",


                3:"**Localized Promotion and Awareness Campaign:**<br>Initiate a promotional campaign that uses culturally relevant, locally popular mediums, and languages to raise awareness about the helpline and the multiple ways South American children can reach out for help.<br>Estimated Time: 1-2 months",


                4:"**Localized Usability Testing:**<br>Regularly conduct usability testing with a diverse user base representative of South America's cultural and linguistic variety. This can identify potential contact process issues hindering accessibility.<br>Estimated Time: Ongoing, with tests every 3-6 months",


                5:"**Regional Language Accessibility:**<br>Given the linguistic diversity in South America, especially with Spanish and Portuguese being widely spoken, ensure the helpline is accessible by providing translation services or employing bilingual/multilingual staff fluent in the prominent languages of South America.<br>Estimated Time: Ongoing, as per requirement and availability of resources"
            },
            'Australia': {
                0:"**24/7 Availability Initiative:**<br>Strive to provide 24/7 availability for the helpline in the Australia region, considering the specific time zones across the country. Explore options such as shifts, rota systems, or employing remote staff in different time zones to ensure accessibility at any time.<br>Estimated Time: 2-4 weeks for planning and implementation",


                1:"**Effective Call Routing System:**<br>Implement an advanced call routing system that considers the linguistic and cultural diversity within Australia. Direct callers to staff members who can provide assistance in the appropriate language or cultural context, taking into account the multiculturalism prevalent in Australia.<br>Estimated Time: 1-2 months for procurement and setup",


                2:"**Multi-channel Contact Options:<br>Expand the helpline to include text, email, and online chat options, considering the prevalence and accessibility of different communication channels in Australia. Take into account the preferences and comfort levels of children when selecting channels, while adhering to relevant privacy and data protection laws.<br>Estimated Time: 1-2 months for setup and testing",


                3:"**Promotion and Awareness Campaign:**<br>Launch a targeted promotional campaign in the Australia region to increase awareness about the helpline and the different contact options available. Consider cultural nuances, languages, and communication channels preferred by the target audience, while ensuring compliance with advertising regulations and ethical guidelines.<br>Estimated Time: 1-2 months",

                4:"**Usability Testing:**<br>Conduct regular usability testing specific to the Australia region to identify potential issues in the contact process that may hinder accessibility. Consider factors such as language barriers, technological limitations, and cultural sensitivities during the testing process, while complying with user testing standards and ethical guidelines.<br>Estimated Time: Ongoing, with tests every 3-6 months",

                5:"**Language Accessibility:**<br>Ensure the helpline is accessible to non-native English speakers in the Australia region by providing translation services or employing bilingual/multilingual staff who can communicate in the languages commonly spoken by diverse communities within Australia.<br>Estimated Time: Ongoing, as per requirement and availability of resources"

            }
        }
    }
]

# Define the background image URL
background_image_url = 'https://example.com/background_image.jpg'

# Streamlit app layout
def home_page():
    
    st.title('KidConnect Evaluation Test')
    st.markdown('#### The following test aims to evaluate how well your helpline is performing. Please follow these steps to complete the assesment')
    st.markdown('STEP 1: From the sidebar, choose your region so that the recomendations given are tailored to your location.')
    st.markdown('STEP 2: There are 10 questions to be answered from different areas of interest, each question has 6 possible answers, each response is numbered from 0 to 5, being 0 the area that needs the most improvement and 5 the least.')
    st.markdown('STEP 3: Hit the submit button, you will get a level of improvement score from 0 to 10, being 0 the least improvement needed and 10 the most.')
    st.markdown('STEP 4: Below the score you will find tailored recomendations for each of the 10 areas of interest of the answered questions, read them to get insights.')
    st.markdown('STEP 5: From the sidebar, visit the additional resources page to find further help on the topics from this website')
    st.markdown('##### Good Luck!')
    
    st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        align-items: flex-start;
        height: 20vh;
    }
    
    .image-container img {
        max-height: 100%;
        width: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="image-container">
            <img src="https://kidshelpline.com.au/sites/default/files/bdl_image/KHL_Logotype_Older_Primary_Lozenge_Central.png" alt="Image">
        </div>
        """,
        unsafe_allow_html=True)

def show_africa_page():
    st.title('Africa Page')
    st.markdown("Recomendations will be tailored to Africa's Reality")
    st.markdown("**Remember**: 0 is the area that needs the most improvement and 5 is the area that needs the least")

    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum((answer['answer']-5) * question['weight']*(-2) for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'### Level of Improvement Needed: **{score}**')
        
        # Create star plot
        plot_data = np.array([(x['answer']-5)*-2 for x in answers.values()])
        num_questions = len(questions)
        angles = np.linspace(0, 2 * np.pi, num_questions, endpoint=False).tolist()
        angles += angles[:1]  # Repeat the first angle to close the plot
        plot_data = np.append(plot_data, plot_data[:1])  # Repeat the first data point to close the plot

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        ax.plot(angles, plot_data, color='red', linewidth=1)
        ax.fill(angles, plot_data, color='red', alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([question['topic'] for question in questions], fontsize=6)
        ax.set_yticks([2, 4, 6, 8, 10])

        st.pyplot(fig)

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)

def show_asia_page():
    st.title("Asia Page")
    st.markdown("Recomendations will be tailored to Asia's Reality")
    st.markdown("**Remember**: 0 is the area that needs the most improvement and 5 is the area that needs the least")
    # Add content specific to Asia
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum((answer['answer']-5) * question['weight']*(-2) for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'### Level of Improvement Needed: **{score}**')
        
        # Create star plot
        plot_data = np.array([(x['answer']-5)*-2 for x in answers.values()])
        num_questions = len(questions)
        angles = np.linspace(0, 2 * np.pi, num_questions, endpoint=False).tolist()
        angles += angles[:1]  # Repeat the first angle to close the plot
        plot_data = np.append(plot_data, plot_data[:1])  # Repeat the first data point to close the plot

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        ax.plot(angles, plot_data, color='red', linewidth=1)
        ax.fill(angles, plot_data, color='red', alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([question['topic'] for question in questions], fontsize=6)
        ax.set_yticks([2, 4, 6, 8, 10])

        st.pyplot(fig)

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                
def show_europe_page():
    st.title("Europe Page")
    st.markdown("Recomendations will be tailored to Europe's Reality")
    st.markdown("**Remember**: 0 is the area that needs the most improvement and 5 is the area that needs the least")
    # Add content specific to Europe
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum((answer['answer']-5) * question['weight']*(-2) for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'### Level of Improvement Needed: **{score}**')
        
        # Create star plot
        plot_data = np.array([(x['answer']-5)*-2 for x in answers.values()])
        num_questions = len(questions)
        angles = np.linspace(0, 2 * np.pi, num_questions, endpoint=False).tolist()
        angles += angles[:1]  # Repeat the first angle to close the plot
        plot_data = np.append(plot_data, plot_data[:1])  # Repeat the first data point to close the plot

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        ax.plot(angles, plot_data, color='red', linewidth=1)
        ax.fill(angles, plot_data, color='red', alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([question['topic'] for question in questions], fontsize=6)
        ax.set_yticks([2, 4, 6, 8, 10])

        st.pyplot(fig)

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                

def show_north_america_page():
    st.title("North America Page")
    st.markdown("Recomendations will be tailored to North America's Reality")
    st.markdown("**Remember**: 0 is the area that needs the most improvement and 5 is the area that needs the least")
    # Add content specific to North America
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum((answer['answer']-5) * question['weight']*(-2) for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'### Level of Improvement Needed: **{score}**')
        
        # Create star plot
        plot_data = np.array([(x['answer']-5)*-2 for x in answers.values()])
        num_questions = len(questions)
        angles = np.linspace(0, 2 * np.pi, num_questions, endpoint=False).tolist()
        angles += angles[:1]  # Repeat the first angle to close the plot
        plot_data = np.append(plot_data, plot_data[:1])  # Repeat the first data point to close the plot

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        ax.plot(angles, plot_data, color='red', linewidth=1)
        ax.fill(angles, plot_data, color='red', alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([question['topic'] for question in questions], fontsize=6)
        ax.set_yticks([2, 4, 6, 8, 10])

        st.pyplot(fig)

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                

def show_south_america_page():
    st.title("South America Page")
    st.markdown("Recomendations will be tailored to South America's Reality")
    st.markdown("**Remember**: 0 is the area that needs the most improvement and 5 is the area that needs the least")
    # Add content specific to South America
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum((answer['answer']-5) * question['weight']*(-2) for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'### Level of Improvement Needed: **{score}**')
        
        # Create star plot
        plot_data = np.array([(x['answer']-5)*-2 for x in answers.values()])
        num_questions = len(questions)
        angles = np.linspace(0, 2 * np.pi, num_questions, endpoint=False).tolist()
        angles += angles[:1]  # Repeat the first angle to close the plot
        plot_data = np.append(plot_data, plot_data[:1])  # Repeat the first data point to close the plot

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        ax.plot(angles, plot_data, color='red', linewidth=1)
        ax.fill(angles, plot_data, color='red', alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([question['topic'] for question in questions], fontsize=6)
        ax.set_yticks([2, 4, 6, 8, 10])

        st.pyplot(fig)

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)
                

def show_australia_page():
    st.title("Australia Page")
    st.markdown("Recomendations will be tailored to Australia's Reality")
    st.markdown("**Remember**: 0 is the area that needs the most improvement and 5 is the area that needs the least")
    # Add content specific to Australia
    
    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.selectbox('Select your answer', list(question['answers'].keys()))
        answers[i] = {
            'answer': question['answers'][answer],
            'topic': question['topic'],
            'recomendation': question['recomendations'][selection][question['answers'][answer]]
        }

    # Calculate final score
    score = sum((answer['answer']-5) * question['weight']*(-2) for question, answer in zip(questions, answers.values()))

    # Display final score and recommendations on submit
    if st.button('Submit'):
        st.subheader('Quiz Result')
        st.markdown(f'### Level of Improvement Needed: **{score}**')
        
        # Create star plot
        plot_data = np.array([(x['answer']-5)*-2 for x in answers.values()])
        num_questions = len(questions)
        angles = np.linspace(0, 2 * np.pi, num_questions, endpoint=False).tolist()
        angles += angles[:1]  # Repeat the first angle to close the plot
        plot_data = np.append(plot_data, plot_data[:1])  # Repeat the first data point to close the plot

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        ax.plot(angles, plot_data, color='red', linewidth=1)
        ax.fill(angles, plot_data, color='red', alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([question['topic'] for question in questions], fontsize=6)
        ax.set_yticks([2, 4, 6, 8, 10])

        st.pyplot(fig)

        st.subheader('Recommendations')
        for i, answer in answers.items():
            with st.expander(answer['topic']):
                st.markdown(answer['recomendation'], unsafe_allow_html=True)

# Additional resources page
def additional_resources():
    
    st.title('Additional Resources')
    st.markdown('##### If you need additional help with the topics of this helpline evaluation, please refer to the following resources:')
    
    links_resources = [
        {
            "title": "Keeping the Promise: Ending Violence Against Children by 2030",
            "url": "https://violenceagainstchildren.un.org/sites/violenceagainstchildren.un.org/files/keeping_the_promise.pdf"
        },
        {
            "title": "UNICEF Technical Guide - Child HelpLines",
            "url": "https://www.unicef.org/albania/media/2971/file/UNICEF%20Technical%20Guide%20-%20Child%20HelpLines.pdf"
        },
        {
            "title": "Child Helpline International - eLearning Platform",
            "url": "https://childhelplineinternational.org/elearning-platform-our-courses/"
        },
        {
            "title": "Building Your Child Helpline : A user-friendly guide to starting or scaling-up a child helpline",
            "url": "https://resourcecentre.savethechildren.net/document/building-your-child-helpline-user-friendly-guide-starting-or-scaling-child-helpline/"
        }
    ]

    for link in links_resources:
        title = f"{link['title']}"
        st.write(f"- {title} [Visit]({link['url']})")
    
    st.title('Places for Donation')
    st.markdown('##### If you find yourself charitable and want to contribute to one of the causes related to the causes that helplines assist, please visit the following sites:')
    
    links_donations = [
        {
            "title": "BackaBuddy - Where cause meets crowd",
            "url": "https://www.backabuddy.co.za/"
        },
        {
            "title": "GoFundMe",
            "url": "https://www.gofundme.com/en-gb"
        }
    ]
    
    for link in links_donations:
        title = f"{link['title']}"
        st.write(f"- {title} [Visit]({link['url']})")
                
# Run the app
if __name__ == '__main__':
    # Display page selection
    # Create the index
    st.sidebar.title("Index")
    selection = st.sidebar.radio("Select a page", ["Home Page", "Africa", "Asia", "Europe", "North America", "South America", "Australia", "Additional Resources"])

    if selection == "Africa":
        show_africa_page()
    elif selection == "Asia":
        show_asia_page()
    elif selection == "Europe":
        show_europe_page()
    elif selection == "North America":
        show_north_america_page()
    elif selection == "South America":
        show_south_america_page()
    elif selection == "Australia":
        show_australia_page()
    elif selection == "Additional Resources":
        additional_resources()
    else:
        home_page()



